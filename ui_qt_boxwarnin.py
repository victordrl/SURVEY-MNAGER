# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_boxwarninLoLMOM.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog_W(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(413, 97)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.f_dialog_box = QFrame(Dialog)
        self.f_dialog_box.setObjectName(u"f_dialog_box")
        self.f_dialog_box.setStyleSheet(u"	background: rgba(70, 70, 70, 0.4);\n"
"	border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_dialog_box.setFrameShape(QFrame.Shape.NoFrame)
        self.f_dialog_box.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_dialog_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.f_dialog_box)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold Condensed"])
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background: rgba(70, 70, 70, 0);")

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.f_dialog_box)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
        self.b_aceptar.clicked.connect(self.aceptar_dialogo)

    def aceptar_dialogo(self):
        # Realizar acciones necesarias antes de cerrar el diálogo
        self.accept()  
          
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Contrase\u00f1a o Usuario incorrectos</p><p align=\"center\">intente de nuevo</p></body></html>", None))
    # retranslateUi

