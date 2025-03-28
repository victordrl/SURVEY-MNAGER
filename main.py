from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QWidget, QCheckBox, QLineEdit, QMenu, QWidgetAction, QWidget, QMessageBox, QDialog, QSizePolicy
from PySide6.QtGui import QFontDatabase
from ui_qt_form import Ui_MainWindow
from ui_qt_login import Ui_Logni
from ui_qt_profe import Ui_f_profe
from ui_qt_statgeneral import Ui_f_stat_general
from ui_qt_boxpssw import Ui_Dialog
from ui_qt_boxwarnin import Ui_Dialog_W
from funciones import *
from Bot_mail import *
from BD import checkLogin

class App(QMainWindow):
    
    def __init__(self, inicio_app,user,password):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.inicio = inicio_app
        self.user=user
        self.password=password
        
        # CONECCIONES DEL MENU PRINCIPAL
        self.ui.b_logo.clicked.connect(self.mostrarPaginaInicio)
        self.ui.b_perfil.clicked.connect(self.mostrarPaginaPerfil)
        self.ui.b_encuesta.toggled.connect(self.mostrarPaginaEncuesta)
        self.ui.b_stats.toggled.connect(self.mostrarPaginaEstadisticas)
        self.ui.b_shear.toggled.connect(self.mostrarPaginaBusqueda)
        self.ui.b_config.clicked.connect(self.mostrarPaginaConfiguracion)
        
        # CONECCIONES DE ENCUESTAS
        self.ui.b_enviar_encuesta.clicked.connect(self.activarBot)
        self.ui.b_edit_encuesta.clicked.connect(self.mostrarPaginaEdicion)
        
        self.ui.b_atras_agegar_estud.clicked.connect(self.devolverPaginaEditar)
        self.ui.b_atras_agegar_profe.clicked.connect(self.devolverPaginaEditar)
        self.ui.b_atras_encuesta.clicked.connect(self.devolverPaginaEditar)
        
        self.ui.b_guardar_encuesta.clicked.connect(self.gurardarEdicionEncuesta)
        self.ui.b_guardar_agegar_estud.clicked.connect(self.gurardarEdicionEstudiante)
        self.ui.b_guardar_agegar_profe.clicked.connect(self.gurardarEdicionProfesor)
        
        self.ui.b_cancelar_encuesta.clicked.connect(self.cancelarEdicion)
        
        self.ui.b_categoria_1.toggled.connect(self.mostrarCatergoria_1)
        self.ui.b_categoria_2.toggled.connect(self.mostrarCatergoria_2)
        self.ui.b_categoria_3.toggled.connect(self.mostrarCatergoria_3)
        self.ui.b_categoria_4.toggled.connect(self.mostrarCatergoria_4)
        
        self.ui.b_editar_estudiantes.clicked.connect(self.mostrarEditEstudiantes)
        self.ui.b_editar_profes.clicked.connect(self.mostrarEditProfes)
        
        # CONECCIONES DE BUSQUEDA
        self.ui.b_shear_2.clicked.connect(self.resultadoBusqueda)
        self.ui.lineEdit.returnPressed.connect(self.resultadoBusqueda)
        
        # CONECCIONES DE ESTADISTICAS
        self.estadisticaGeneral()
        self.ui.tabWidget.tabCloseRequested.connect(lambda index: self.closeTab(index))
        #self.ui.tabWidget.tabCloseRequested.connect(lambda index: self.ui.tabWidget.removeTab(index))
        
        # CONECCIONES DE PERFIL
        self.pasarInfoUser()
        self.ui.b_cerrar_secion.clicked.connect(self.cerrarSesion)
        self.ui.b_ver_password.toggled.connect(self.verPassword)
        self.ui.b_cambiar_pasworld.clicked.connect(self.cambiarPassword)
        self.ui.tabWidget.tabCloseRequested.connect(lambda index: self.ui.tabWidget.removeTab(index))

    # FUNCIONES DE MENU
    def mostrarPaginaInicio(self):
        # Desactivar autoExclusive
        self.ui.b_encuesta.setAutoExclusive(False)
        self.ui.b_stats.setAutoExclusive(False)
        self.ui.b_shear.setAutoExclusive(False)
        self.ui.b_config.setAutoExclusive(False)

        # Desmarcar los botones
        self.ui.b_encuesta.setChecked(False)
        self.ui.b_stats.setChecked(False)
        self.ui.b_shear.setChecked(False)
        self.ui.b_config.setChecked(False)

        # Volver a activar autoExclusive si es necesario
        self.ui.b_encuesta.setAutoExclusive(True)
        self.ui.b_stats.setAutoExclusive(True)
        self.ui.b_shear.setAutoExclusive(True)
        self.ui.b_config.setAutoExclusive(True)
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def mostrarPaginaPerfil(self):
        self.ui.stackedWidget.setCurrentIndex(2)
   
    def mostrarPaginaEncuesta(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(5)
            
    def mostrarPaginaBusqueda(self, checked):
        if checked:
            self.ui.stackedWidget.setCurrentIndex(1)
   
    def mostrarPaginaEstadisticas(self, checked):
        if checked:
            self.estadisticaGeneral()
            self.ui.stackedWidget.setCurrentIndex(4)
    
    def mostrarPaginaConfiguracion(self):
        #self.ui.stackedWidget.setCurrentIndex(3)
        print("cambio de modo oscuro/claro")
            
    # FUNCIONES DE ENCUESTAS
    def activarBot(self):
        dialogo = QDialog(self)
        dialog_ui = Ui_Dialog()
        dialog_ui.setupUi(dialogo)
        d = dialogo.exec_()
        if d == QDialog.Accepted:
            texto_lineedit = dialog_ui.lineEdit.text()
            print(f"Texto del QLineEdit: {texto_lineedit}")
            correos()
    
    def mostrarPaginaEdicion(self):
        self.ui.stackedWidget_2.setCurrentIndex(3)
    
    def mostrarEditEstudiantes(self):
        self.ui.stackedWidget_2.setCurrentIndex(2)
        
    def mostrarEditProfes(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        
        
    # Botones superior
    def devolverPaginaEditar(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        
    def cancelarEdicion(self):
        for i in range(self.ui.stackedWidget_3.count()):
            pagina = self.ui.stackedWidget_3.widget(i)
            for child in pagina.findChildren(QLineEdit):
                child.clear()
        print ('borrar')
    
    def gurardarEdicionEncuesta(self):
        datos = []
        for i in range(self.ui.stackedWidget_3.count()):
            pagina = self.ui.stackedWidget_3.widget(i)
            for child in pagina.findChildren(QLineEdit):
                datos.append(child.text())
        
        print ('guardar')
        print (datos)
        return datos
    def gurardarEdicionEstudiante(self):
        pass
    
    def gurardarEdicionProfesor(self):
        pass
    
    # Botones de ediciones
    def mostrarCatergoria_1(self, checked):
        if checked:
            self.ui.stackedWidget_3.setCurrentIndex(0)
            
    def mostrarCatergoria_2(self, checked):
        if checked:
            self.ui.stackedWidget_3.setCurrentIndex(1)
            
    def mostrarCatergoria_3(self, checked):
        if checked:
            self.ui.stackedWidget_3.setCurrentIndex(2)
            
    def mostrarCatergoria_4(self, checked):
        if checked:
            self.ui.stackedWidget_3.setCurrentIndex(3)
        
    
    # FUNCIONES DE ESTADISTICAS      
    def nuevaEstadisticas(self,id):
        nombre=consultaId(id)
        self.estadisticaGeneral()
        
        for index in range(self.ui.tabWidget.count()):
            if self.ui.tabWidget.tabText(index) == nombre[0][1]:
                return
            
        f_aux_stat = Estadisticas(id)
        f_aux_stat.listaGraficas()
        self.ui.tabWidget.addTab(f_aux_stat,nombre[0][1])
         
    def estadisticaGeneral(self):
        if self.ui.tabWidget.count() == 0:
            f_aux_stat = GeneralTab()
            self.ui.tabWidget.addTab(f_aux_stat,'General')
                
                
    def closeTab(self, index):
        self.estadisticaGeneral()
        self.ui.tabWidget.removeTab(index)
        self.estadisticaGeneral()
    
    # FUNCIONES DE BUSQUEDAS
    def resultadoBusqueda(self):
        search=self.ui.lineEdit.text()
        
        for i in reversed(range(self.ui.scrollAreaContents.layout().count())):
            widget = self.ui.scrollAreaContents.layout().itemAt(i).widget()
            if widget:
                widget.deleteLater()
        
        self.busqueda=Busqueda(self,search)
        lista=self.busqueda.recuadro()
        for i in range (len(lista)):
            self.ui.scrollAreaContents.layout().insertWidget(0, lista[i])
       
    # FUNCIONES DE PERFIL 
    def verPassword(self,checked):
        if checked:
            self.ui.lineedit_password.setEchoMode(QLineEdit.Normal)    
        else:
            self.ui.lineedit_password.setEchoMode(QLineEdit.Password)
    
    def cerrarSesion(self):
        self.inicio.show()
        self.close()
        
    def cambiarPassword(self):
        dialogo = QDialog(self)
        dialog_ui = Ui_Dialog()
        dialog_ui.setupUi(dialogo)
        d = dialogo.exec_()
        if d == QDialog.Accepted:
            texto_lineedit = dialog_ui.lineEdit.text()
            print(f"Texto del QLineEdit: {texto_lineedit}")
    
    def pasarInfoUser(self):
        data=userData(self.user,self.password)
        print(self.user,self.password)
        for i in range(len(data)):
           # if(data[i][1]==self.user and data[i][2]==self.password):
                self.ui.label_nick.setText('  ' + data[i][1])
                self.ui.lineedit_password.setText(data[i][2])
                self.ui.label_nombre.setText('  ' + data[i][3])
                self.ui.label_apellido.setText('  ' + data[i][4])
                self.ui.label_escuela.setText('Escuela :' + data[i][5])
                self.ui.label_telefono.setText('Telefono :' + data[i][6])
                self.ui.label_correo.setText('Correo :' + data[i][7])
                self.ui.label_direccion.setText('Direccion : ' + data[i][8])
             #   break
    
class Estadisticas(QFrame):
    def __init__(self,idP):
        super(Estadisticas, self).__init__()
        self.ui = Ui_f_profe()
        self.ui.setupUi(self)
        self.id=idP
        self.informacion()
        # CONECCION DE LAS TAB EN AMBAS GRAFICAS
        self.ui.b_recarga_grafica.clicked.connect(self.actualizarGrafica)
        self.ui.tab_graf_barra.currentChanged.connect(self.conectarGrafica)
        self.ui.tab_graf_linea.currentChanged.connect(self.conectarGrafica)
         
        self.profes = ['nombre apellido 1','nombre apellido 2','nombre apellido 3','nombre apellido 4','nombre apellido 5']
        self.f = ['10-12-2023', '10-01-2024']
        
        self.fechasFinales(self.f)
        self.fechasIniciales(self.f)
    
    # INICIALIZAION DE DATOS
    def informacion(self):
        datos=consultaId(self.id)
        self.ui.nombre_profe.setText(datos[0][1]+" - "+datos[0][3])
        self.ui.escuela_profe.setText(datos[0][2])
        # self.ui.perfil_profe.pixmap(img)
        
    # FUNCION DE CONEXION
    def conectarGrafica(self, indice):
        if self.sender() == self.ui.tab_graf_barra:
            self.ui.tab_graf_linea.setCurrentIndex(indice)
        elif self.sender() == self.ui.tab_graf_linea:
            self.ui.tab_graf_barra.setCurrentIndex(indice)
     
    def listaGraficas(self):
        cantM=tMaterias(self.id)
        self.tabGrafica(1,0)
        for i in range(len(cantM)):
            self.tabGrafica(0,cantM[i][0])
    
    def tabGrafica(self,graf,materia):
        if(materia==0):
            nombre="Materias"
        else:
            nombre=consultaIdMateria(materia)
            nombre=nombre[0][0]
        tab_contein = GraphicTab(0,self.id,graf,materia)
        self.ui.tab_graf_barra.addTab(tab_contein, nombre)

        tab_contein = GraphicTab(1,self.id,graf,materia)
        self.ui.tab_graf_linea.addTab(tab_contein, nombre)
    
    def actualizarGrafica(self):
        print('Actualizar')
        pass
    def fechasIniciales(self,fechas):
        self.ui.comboBox_fecha_inicio.addItems(fechas)
    
    def fechasFinales(self,fechas):
        self.ui.comboBox_fecha_final.addItems(fechas)
 
 
class GeneralTab(QFrame):
    def __init__(self):
        super(GeneralTab, self).__init__()
        self.ui = Ui_f_stat_general()
        self.ui.setupUi(self)
        
        
        self.botones_chequeados = []
        # Primero, declara el botón check_all
        self.b_checks = QPushButton("Profesores de Escuela", self)
        self.b_checks.setCheckable(True)  
        self.b_checks.setFont(QFont('Tw Cen MT Condensed',14))
        self.b_checks.setStyleSheet("""
            QPushButton{
                color: white;
                background-color: rgba(70, 70, 70, 0);
            }
        """)

        self.check_profe = QMenu(self)
        self.check_profe.setMinimumSize(350,0)
        self.check_profe.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.check_profe.setStyleSheet("""
            QMenu{
                color: white;
                background-color: rgb(70, 70, 70);
                border-radius: 10px; 
            }
        """)
        
        self.accion = QWidgetAction(self)
        self.b_all = QCheckBox("ALL", self)
        self.b_all.setMinimumSize(350,0)
        self.b_all.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.b_all.setFont(QFont("Bahnschrift SemiLight Condensed", 10))
        self.b_all.setStyleSheet("""
            QCheckBox {
                color: white;
                background-color: rgb(70, 70, 70);
                border-radius: 5px; 
            }
            QCheckBox::indicator {
                border: none;
                background-color: rgb(120, 120, 120);
                border-radius: 5px; 
            }
            QCheckBox::indicator:checked {
                border: none;
                border-radius: 5px; 
                background-color: rgba(40, 85, 165, 0.7);
            }
        """)
        self.accion.setDefaultWidget(self.b_all)

        self.b_checks.setMenu(self.check_profe)
        
        self.ui.verticalLayout_2.addWidget(self.b_checks)
        
        self.profes = ['nombre apellido 1','nombre apellido 2','nombre apellido 3','nombre apellido 4','nombre apellido 5']
        self.escuelas = ['Ingeneria','Fases','Derechos']
        self.f = ['10-12-2023', '10-01-2024']
        
        self.profesOpciones(self.profes)
        self.escuelasOpciones(self.escuelas)
        self.fechasFinales(self.f)
        self.fechasIniciales(self.f)
        
        self.ui.b_general_barra.toggled.connect(self.mostrarBarras)
        self.ui.b_general_linea.toggled.connect(self.mostrarLineas)
        self.ui.b_actualizar_grafi.clicked.connect(self.actualizarGrafica)
        
        self.b_all.stateChanged.connect(self.actualizarBotones)
        
    def actualizarBotones(self, state):
        for accion in self.check_profe.actions():
            widget = accion.defaultWidget()
            if isinstance(widget, QCheckBox):
                widget.setChecked(state)
    
    def botonesChequeados(self):
        for accion in self.check_profe.actions():
            widget = accion.defaultWidget()
            if isinstance(widget, QCheckBox) and widget.isChecked():
                self.botones_chequeados.append(widget.text())
        print(self.botones_chequeados)


    def profesOpciones(self,lista_nombres):
        self.check_profe.clear()
        self.check_profe.addAction(self.accion)
        for nombre in lista_nombres:
            accion = QWidgetAction(self)
            checkbox = QCheckBox(nombre, self)
            checkbox.setFont(QFont("Bahnschrift SemiLight Condensed", 10))
            checkbox.setStyleSheet("""
                QCheckBox {
                    color: white;
                    background-color: rgb(70, 70, 70);
                    border-radius: 5px; 
                }
                QCheckBox::indicator {
                    border: none;
                    background-color: rgb(120, 120, 120);
                    border-radius: 5px; 
                }
                QCheckBox::indicator:checked {
                    border: none;
                    border-radius: 5px; 
                    background-color: rgba(40, 85, 165, 0.7);
                }
            """)
            accion.setDefaultWidget(checkbox)
            self.check_profe.addAction(accion)
               
    def escuelasOpciones(self,esc):
        self.ui.comboBox_escuelas.addItems(esc)
        
    def fechasIniciales(self,fechas):
        self.ui.comboBox_fecha_inicio.addItems(fechas)
    
    def fechasFinales(self,fechas):
        self.ui.comboBox_fecha_final.addItems(fechas)
    
    def mostrarBarras(self,checked):
        if checked:
            self.ui.f_graf_linea.hide()
            self.ui.f_graf_barra.show()
            
    def mostrarLineas(self,checked):
        if checked:
            self.ui.f_graf_barra.hide()
            self.ui.f_graf_linea.show()
            
    def actualizarGrafica(self):
        self.botonesChequeados()
        print('Actualizar')
        pass
    
class Inicio(QWidget):
    def __init__(self):
        super(Inicio, self).__init__()
        self.ui = Ui_Logni()
        self.ui.setupUi(self)
        self.logeado = False
        
        self.ui.b_login.clicked.connect(self.logear)
        self.ui.lineedit_password_log.returnPressed.connect(self.logear)
        self.ui.lineedit_user_log.returnPressed.connect(self.logear)
        
        self.ui.b_register.clicked.connect(self.mostrarRegistrar)
        self.ui.lineedit_password_reg.returnPressed.connect(self.registrar)
        self.ui.lineedit_user_reg.returnPressed.connect(self.registrar)
        
        self.ui.b_volver.clicked.connect(self.mostrarLogin)
        
    def logear(self):
        # LOGIN ANTES DE ABRIR LA APP
        boolean=checkLogin(self.ui.lineedit_user_log.text(),self.ui.lineedit_password_log.text())
        if(boolean==1):
            self.logeado = True
            login.hide()
            
            window = App(login,self.ui.lineedit_user_log.text(),self.ui.lineedit_password_log.text())
            window.user = self.ui.lineedit_password_log.text()
            window.password = self.ui.lineedit_password_log.text()
            self.ui.lineedit_user_log.clear()
            self.ui.lineedit_password_log.clear()
            self.ui.lineedit_password_reg.clear()
            self.ui.lineedit_user_reg.clear()
            self.ui.lineedit_confirmed.clear()
            window.show()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error de inicio de sesión")
            msg_box.setText("Usuario o contraseña incorrectos. Por favor, reintente o verifique los datos.")
            msg_box.exec_()
    
    def registrar(self):
        pass
    
    def mostrarRegistrar(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def mostrarLogin(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
if __name__ == "__main__":
    app = QApplication([])
    login = Inicio()
    login.show()
    app.exec()
    