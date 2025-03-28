import sys
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación con QWidgetAction")

        # Crear un menú
        menu = QMenu("Menú con QWidgetAction", self.menuBar())
        self.menuBar().addMenu(menu)

        # Crear un widget personalizado (por ejemplo, un botón)
        custom_widget = QCheckBox("Haz clic aquí")
        custom_widget.clicked.connect(self.on_custom_widget_clicked)

        # Crear un QWidgetAction y asignarle el widget personalizado
        widget_action = QWidgetAction(self)
        widget_action.setDefaultWidget(custom_widget)

        # Agregar el QWidgetAction al menú
        menu.addAction(widget_action)

        # Add a loop to create and add 10 checkboxes to the menu
        for i in range(10):
            checkbox = QCheckBox(f"Checkbox {i+1}")
            checkbox.clicked.connect(lambda c=checkbox, i=i: self.on_checkbox_clicked(c, i))
            widget_action = QWidgetAction(self)
            widget_action.setDefaultWidget(checkbox)
            menu.addAction(widget_action)

    def on_custom_widget_clicked(self):
        print("¡Widget personalizado clickeado!")

    def on_checkbox_clicked(self, checkbox, index):
        print(f"Checkbox {index+1} clickeado!")


      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
