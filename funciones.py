import sys
from PySide6.QtWidgets import QApplication, QGraphicsItem, QWidget, QVBoxLayout,QGraphicsItem,QGraphicsSimpleTextItem
from PySide6.QtCharts import QChart, QChartView,QValueAxis,QBarCategoryAxis, QBarSeries, QBarSet, QCategoryAxis, QLineSeries
from PySide6.QtGui import QPainter, QPainterPath, QFontMetricsF, QPen, QColor
from ui_qt_perfil import *
from PySide6.QtCore import Qt,QPointF, QRectF
from BDconsultas import *

class Perfil(QFrame):
    def __init__(self, app_instance,name,idP,esc,cedula):
        super(Perfil, self).__init__()
        self.ui = Ui_f_shear_profe()   
        self.ui.setupUi(self)
        self.nombre=name
        self.id=idP
        self.escuela=esc
        self.cedula=cedula
        
        # REFERENCIA A LA APP MAIN
        self.app_instance = app_instance
        self.informacion()
        # CONECCCIONES DE PERFILES DE BUSQUEDA
        self.ui.stats_profe.clicked.connect(self.nuevaEstadisticas)
        
        #self.ui.b_stat_profe.cliked.connect(self.nuevaEstadisticas)
        
    # INICIALIZAION DE DATOS
    def informacion(self):
        self.ui.s_nombre_profe.setText(self.nombre)
        self.ui.s_escuela_profe.setText(self.escuela)
        #self.ui.img_profe.pixmap(img) 
        
    # FUNCION PARA AGREGAR UNA TAB DEL PERFIL
    def nuevaEstadisticas(self):
        self.app_instance.nuevaEstadisticas(self.id)

class Busqueda:
    #aqui se lee la info desde la BDD buscando coincidencias
    def __init__(self,app_instance,texto):
        self.instancia=app_instance
        self.nombre=texto
        self.lectura()
        
    def lectura(self):
        self.lista=consultaNombre(self.nombre)
    
    def recuadro(self):
        recuadros=[]
        for i in range(len(self.lista)):
           aux=Perfil(self.instancia,self.lista[i][1],self.lista[i][0],self.lista[i][2],self.lista[i][3])
           recuadros.append(aux)
        return recuadros

class Callout(QGraphicsItem):
    def __init__(self, chart):
        super().__init__()
        self.chart = chart
        self.text = ""
        self.anchor = QPointF()
        self.rect = QRectF()

    def set_text(self, text):
        self.text = text
        metrics = QFontMetricsF(self.chart.font())
        self.rect = metrics.boundingRect(QRectF(0, 0, 150, 50), Qt.AlignLeft, self.text)
        self.rect.translate(5, 5)
        self.prepareGeometryChange()
        self.update()

    def set_anchor(self, point):
        self.anchor = point
        self.prepareGeometryChange()
        self.update()

    def boundingRect(self):
        return self.rect.adjusted(-5, -5, 5, 5)

    def paint(self, painter, option, widget):
        path = QPainterPath()
        path.addRoundedRect(self.rect, 5, 5)
        painter.setBrush(Qt.white)
        painter.setPen(Qt.black)
        painter.drawPath(path)
        painter.drawText(self.rect, self.text)

    def updateGeometry(self):
        self.prepareGeometryChange()
        self.update()

class Graficas:
    def ejes(self,lista,graf,materia):
        self.x_labels,self.y=[],[]
        #Si es grafica de encuestas por materia
        if(graf==0): 
            cat=1
            for i in range(len(lista)):
                if(lista[i][1]==materia):
                    # self.x_labels.append(lista[i][2])
                    self.x_labels.append("Categoria %s"%(cat))
                    self.y.append(round(float(lista[i][3]),2))
                    cat+=1
                else:
                    cat=1
            self.x = range(len(self.x_labels))
        elif (graf==1):
            for i in range(len(lista)):
                self.x_labels.append(lista[i][0])
                self.y.append(round(float(lista[i][1]),2))
            self.x = range(len(self.x_labels))
        elif (graf==2):
            for i in range(len(lista)):
                self.x_labels.append(lista[i][0])
                self.y.append(round(float(lista[i][1]),2))
            self.x = range(len(self.x_labels))
        
    def g_barras(self,lista,name_x,name_y,graf,materia):
        self.ejes(lista,graf,materia)
        
        chart=QChart()
        chart.setTitle(f"Gráfico de barras: {name_x} vs {name_y}")
        chart.setTheme(QChart.ChartThemeDark)
        chart.setAnimationOptions(QChart.AllAnimations) 
        
        colors=[("darkblue"),("darkcyan"),("darkred"),("green"),("#e33000")]
        # bar_set = QBarSet(name_y)
        series=QBarSeries()
        j=0
        for i in range(len(self.x)):
            series=QBarSeries()
            
            bar_set=QBarSet(self.x_labels[i])
            bar_set.setColor(colors[j])
            bar_set.append(self.y[i])
            bar_set.setLabelColor("white")
            
            series.append(bar_set)
            series.setLabelsVisible(True)
            # series.setLabelsAngle(-90)
            series.setLabelsFormat("@value")
            # series.setLabelsPosition(QAbstractBarSeries.LabelsCenter)
            chart.addSeries(series)
            j+=1
            if(j==4):
                j=0
        
        axisX=QBarCategoryAxis()
        axisX.append(self.x_labels)
        axisX.setTitleText(name_x)
        
        chart.createDefaultAxes()
        chart.addAxis(axisX, Qt.AlignBottom)
        # chart.setAxisY(axisY)
        
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        
        return chart_view
        
    def g_lineas(self,lista,name_x,name_y,graf,materia):
        self.ejes(lista,graf,materia)
        
        chart = QChart()
        chart.setTitle(f"Gráfico de líneas: {name_x} vs {name_y}")
        chart.setTheme(QChart.ChartThemeDark)
        chart.setAnimationOptions(QChart.AllAnimations) 
        
        series = QLineSeries()
        for i, y in enumerate(self.y):
            series.append(QPointF(self.x[i], y))
        series.setColor(QColor("green"))
        
        chart.addSeries(series)
        
        axisX = QValueAxis()
        axisX.setRange(0, len(self.x_labels) - 1)
        # axisX.setLabels(self.x_labels)
        axisX.setTitleText(name_x)
        
        axisY = QValueAxis()
        axisY.setTitleText(name_y)
        axisY.setRange(0, 5)
        
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        
        series.attachAxis(axisX)
        series.attachAxis(axisY)
        
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        return chart_view
        
class GraphicTab(QWidget):
    def __init__(self,tipo,idP,graf,materia,*listado):
        super().__init__()
        self.graficas=Graficas()
        self.tipo=tipo 
        self.id=idP 
        self.graf=graf 
        self.materia=materia 
        self.listado=listado
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        #si es grafico de encuestas
        if(self.graf==0):
            lista=obtenerPromedioPorProfesor(self.id,self.graf)
            if(self.tipo==0):
                fig = self.graficas.g_barras(lista, "Pregunta", "Puntaje",self.graf,self.materia)
            elif(self.tipo==1):
                fig = self.graficas.g_lineas(lista, "Pregunta", "Puntaje",self.graf,self.materia)
        #si es grafico de materias
        elif(self.graf==1):
            lista=obtenerPromedioPorProfesor(self.id,self.graf)
            if(self.tipo==0):
                fig = self.graficas.g_barras(lista, "Materia", "Puntaje",self.graf,self.materia)
            elif(self.tipo==1):
                fig = self.graficas.g_lineas(lista, "Materia", "Puntaje",self.graf,self.materia)
        #si es grafico de profesores
        elif(self.graf==2):
            lista=generalGraf(self.listado)
            print(lista)
            if(self.tipo==0):
                fig = self.graficas.g_barras(lista, "Profesor", "Puntaje",self.graf,self.materia)
            elif(self.tipo==1):
                fig = self.graficas.g_lineas(lista, "Profesor", "Puntaje",self.graf,self.materia)
        layout.addWidget(fig)
        self.setGeometry(100, 100, 600, 400)
        if(self.tipo==0):
            self.setWindowTitle('Gráfico de Barras')
        elif(self.tipo==1):
            self.setWindowTitle('Gráfico de Líneas')
        self.show()

#Nota: Para pasar la lista debo desempaquetarla asi que debo ponerle * cuando la pase como parametro

if __name__ == "__main__":
    app = QApplication(sys.argv)
    listado=[1,2,3]
    window = GraphicTab(0,"1",2,1,*listado)
    sys.exit(app.exec())

#Consulta usara para generar la grafica general

# def generalGraf(listado):
#     general=[]
#     for i in range(len(listado)):
#         promedio=obtenerPromedioPorProfesor(listado[i],1)
#         suma=0
#         cont=0
#         for j in range(len(promedio)):
#             suma+=float(promedio[j][1])
#             cont+=1
#         nombre=consultaId(listado[i])
#         general.append([nombre[0][1],(suma/cont)])
#     return general