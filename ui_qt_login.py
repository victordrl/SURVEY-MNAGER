# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_loginADlhQV.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Logni(object):
    def setupUi(self, Logni):
        if not Logni.objectName():
            Logni.setObjectName(u"Logni")
        Logni.resize(420, 600)
        Logni.setMinimumSize(QSize(420, 600))
        Logni.setMaximumSize(QSize(420, 600))
        Logni.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(25, 25, 25)\n"
"}")
        self.verticalLayout = QVBoxLayout(Logni)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(Logni)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pag_0 = QWidget()
        self.pag_0.setObjectName(u"pag_0")
        self.verticalLayout_5 = QVBoxLayout(self.pag_0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.f_login = QFrame(self.pag_0)
        self.f_login.setObjectName(u"f_login")
        self.f_login.setStyleSheet(u"QWidget{\n"
"	/*background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"	stop:0 rgb(55, 55, 55),\n"
"	stop: 0.3 rgb(105, 105, 105),\n"
"	stop: 0.7 rgb(105, 105, 105),\n"
"	stop:1 rgb(55, 55, 55));*/\n"
"	\n"
"	background: rgba(70, 70, 70, 0.4);\n"
"	border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);\n"
"}")
        self.f_login.setFrameShape(QFrame.Shape.NoFrame)
        self.f_login.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_login)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.f_encabezado = QFrame(self.f_login)
        self.f_encabezado.setObjectName(u"f_encabezado")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_encabezado.sizePolicy().hasHeightForWidth())
        self.f_encabezado.setSizePolicy(sizePolicy)
        self.f_encabezado.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.f_encabezado.setFrameShape(QFrame.Shape.NoFrame)
        self.f_encabezado.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.f_encabezado)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_logo = QLabel(self.f_encabezado)
        self.label_logo.setObjectName(u"label_logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy1)
        self.label_logo.setMinimumSize(QSize(100, 100))
        self.label_logo.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.label_logo.setPixmap(QPixmap(u"App_Icon/cropped-UGMA-LOGO-1-Photoroom (3)_p.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_logo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_UNP = QLabel(self.f_encabezado)
        self.label_UNP.setObjectName(u"label_UNP")
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiLight Condensed"])
        font.setPointSize(18)
        self.label_UNP.setFont(font)

        self.verticalLayout_4.addWidget(self.label_UNP, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_GMA = QLabel(self.f_encabezado)
        self.label_GMA.setObjectName(u"label_GMA")
        self.label_GMA.setFont(font)

        self.verticalLayout_4.addWidget(self.label_GMA, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.f_encabezado)

        self.f_entrada_datos = QFrame(self.f_login)
        self.f_entrada_datos.setObjectName(u"f_entrada_datos")
        sizePolicy.setHeightForWidth(self.f_entrada_datos.sizePolicy().hasHeightForWidth())
        self.f_entrada_datos.setSizePolicy(sizePolicy)
        self.f_entrada_datos.setMaximumSize(QSize(300, 16777215))
        self.f_entrada_datos.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.f_entrada_datos.setFrameShape(QFrame.Shape.NoFrame)
        self.f_entrada_datos.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.f_entrada_datos)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_user = QLabel(self.f_entrada_datos)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setMinimumSize(QSize(180, 0))
        self.label_user.setMaximumSize(QSize(16777215, 39))
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT Condensed"])
        font1.setPointSize(16)
        self.label_user.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_user)

        self.lineedit_user_log = QLineEdit(self.f_entrada_datos)
        self.lineedit_user_log.setObjectName(u"lineedit_user_log")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineedit_user_log.sizePolicy().hasHeightForWidth())
        self.lineedit_user_log.setSizePolicy(sizePolicy2)
        self.lineedit_user_log.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Tw Cen MT Condensed"])
        font2.setPointSize(12)
        self.lineedit_user_log.setFont(font2)
        self.lineedit_user_log.setStyleSheet(u"background: rgba(70, 70, 70, 1);")
        self.lineedit_user_log.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineedit_user_log)

        self.label_password = QLabel(self.f_entrada_datos)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setMaximumSize(QSize(16777215, 30))
        self.label_password.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_password)

        self.lineedit_password_log = QLineEdit(self.f_entrada_datos)
        self.lineedit_password_log.setObjectName(u"lineedit_password_log")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineedit_password_log.sizePolicy().hasHeightForWidth())
        self.lineedit_password_log.setSizePolicy(sizePolicy3)
        self.lineedit_password_log.setMinimumSize(QSize(0, 30))
        self.lineedit_password_log.setFont(font2)
        self.lineedit_password_log.setStyleSheet(u"background: rgba(70, 70, 70, 1);")
        self.lineedit_password_log.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineedit_password_log.setCursorPosition(0)
        self.lineedit_password_log.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineedit_password_log)


        self.verticalLayout_2.addWidget(self.f_entrada_datos, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.f_botones = QFrame(self.f_login)
        self.f_botones.setObjectName(u"f_botones")
        sizePolicy.setHeightForWidth(self.f_botones.sizePolicy().hasHeightForWidth())
        self.f_botones.setSizePolicy(sizePolicy)
        self.f_botones.setMinimumSize(QSize(300, 50))
        self.f_botones.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.f_botones.setFrameShape(QFrame.Shape.NoFrame)
        self.f_botones.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.f_botones)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.b_login = QPushButton(self.f_botones)
        self.b_login.setObjectName(u"b_login")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.b_login.sizePolicy().hasHeightForWidth())
        self.b_login.setSizePolicy(sizePolicy4)
        self.b_login.setMinimumSize(QSize(0, 40))
        self.b_login.setFont(font1)
        self.b_login.setStyleSheet(u"QPushButton{\n"
"	background: rgb(55, 55, 55);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")

        self.horizontalLayout.addWidget(self.b_login)

        self.b_register = QPushButton(self.f_botones)
        self.b_register.setObjectName(u"b_register")
        sizePolicy4.setHeightForWidth(self.b_register.sizePolicy().hasHeightForWidth())
        self.b_register.setSizePolicy(sizePolicy4)
        self.b_register.setMinimumSize(QSize(0, 40))
        self.b_register.setFont(font1)
        self.b_register.setStyleSheet(u"QPushButton{\n"
"	background: rgb(55, 55, 55);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")

        self.horizontalLayout.addWidget(self.b_register)


        self.verticalLayout_2.addWidget(self.f_botones)


        self.verticalLayout_5.addWidget(self.f_login)

        self.stackedWidget.addWidget(self.pag_0)
        self.pag_1 = QWidget()
        self.pag_1.setObjectName(u"pag_1")
        self.verticalLayout_9 = QVBoxLayout(self.pag_1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.f_rgister = QFrame(self.pag_1)
        self.f_rgister.setObjectName(u"f_rgister")
        self.f_rgister.setStyleSheet(u"QWidget{\n"
"	/*background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"	stop:0 rgb(55, 55, 55),\n"
"	stop: 0.3 rgb(105, 105, 105),\n"
"	stop: 0.7 rgb(105, 105, 105),\n"
"	stop:1 rgb(55, 55, 55));*/\n"
"	\n"
"	background: rgba(70, 70, 70, 0.4);\n"
"	border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);\n"
"}")
        self.f_rgister.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_rgister.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.f_rgister)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.f_encabezado_r = QFrame(self.f_rgister)
        self.f_encabezado_r.setObjectName(u"f_encabezado_r")
        sizePolicy.setHeightForWidth(self.f_encabezado_r.sizePolicy().hasHeightForWidth())
        self.f_encabezado_r.setSizePolicy(sizePolicy)
        self.f_encabezado_r.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.f_encabezado_r.setFrameShape(QFrame.Shape.NoFrame)
        self.f_encabezado_r.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.f_encabezado_r)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.label_logo_r = QLabel(self.f_encabezado_r)
        self.label_logo_r.setObjectName(u"label_logo_r")
        sizePolicy2.setHeightForWidth(self.label_logo_r.sizePolicy().hasHeightForWidth())
        self.label_logo_r.setSizePolicy(sizePolicy2)
        self.label_logo_r.setMinimumSize(QSize(100, 100))
        self.label_logo_r.setPixmap(QPixmap(u"App_Icon/cropped-UGMA-LOGO-1-Photoroom (3)_p.png"))
        self.label_logo_r.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_logo_r, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_UNP_r = QLabel(self.f_encabezado_r)
        self.label_UNP_r.setObjectName(u"label_UNP_r")
        self.label_UNP_r.setFont(font)

        self.verticalLayout_7.addWidget(self.label_UNP_r, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_GMA_r = QLabel(self.f_encabezado_r)
        self.label_GMA_r.setObjectName(u"label_GMA_r")
        self.label_GMA_r.setFont(font)

        self.verticalLayout_7.addWidget(self.label_GMA_r, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_6.addWidget(self.f_encabezado_r)

        self.f_entrada_datos_r = QFrame(self.f_rgister)
        self.f_entrada_datos_r.setObjectName(u"f_entrada_datos_r")
        sizePolicy.setHeightForWidth(self.f_entrada_datos_r.sizePolicy().hasHeightForWidth())
        self.f_entrada_datos_r.setSizePolicy(sizePolicy)
        self.f_entrada_datos_r.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.f_entrada_datos_r.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_entrada_datos_r.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.f_entrada_datos_r)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.label_user_r = QLabel(self.f_entrada_datos_r)
        self.label_user_r.setObjectName(u"label_user_r")
        self.label_user_r.setMinimumSize(QSize(180, 0))
        self.label_user_r.setMaximumSize(QSize(16777215, 39))
        self.label_user_r.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_user_r)

        self.lineedit_user_reg = QLineEdit(self.f_entrada_datos_r)
        self.lineedit_user_reg.setObjectName(u"lineedit_user_reg")
        self.lineedit_user_reg.setMinimumSize(QSize(0, 30))
        self.lineedit_user_reg.setFont(font2)
        self.lineedit_user_reg.setStyleSheet(u"background: rgba(70, 70, 70, 1);")
        self.lineedit_user_reg.setCursorPosition(0)
        self.lineedit_user_reg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.lineedit_user_reg)

        self.label_password_r = QLabel(self.f_entrada_datos_r)
        self.label_password_r.setObjectName(u"label_password_r")
        self.label_password_r.setMaximumSize(QSize(16777215, 30))
        self.label_password_r.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_password_r)

        self.lineedit_password_reg = QLineEdit(self.f_entrada_datos_r)
        self.lineedit_password_reg.setObjectName(u"lineedit_password_reg")
        self.lineedit_password_reg.setMinimumSize(QSize(0, 30))
        self.lineedit_password_reg.setFont(font2)
        self.lineedit_password_reg.setStyleSheet(u"background: rgba(70, 70, 70, 1);")
        self.lineedit_password_reg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.lineedit_password_reg)

        self.label_confirmes = QLabel(self.f_entrada_datos_r)
        self.label_confirmes.setObjectName(u"label_confirmes")
        self.label_confirmes.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_confirmes)

        self.lineedit_confirmed = QLineEdit(self.f_entrada_datos_r)
        self.lineedit_confirmed.setObjectName(u"lineedit_confirmed")
        self.lineedit_confirmed.setMinimumSize(QSize(0, 30))
        self.lineedit_confirmed.setFont(font2)
        self.lineedit_confirmed.setStyleSheet(u"background: rgba(70, 70, 70, 1);")
        self.lineedit_confirmed.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineedit_confirmed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.lineedit_confirmed)


        self.verticalLayout_6.addWidget(self.f_entrada_datos_r, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.f_botones_r = QFrame(self.f_rgister)
        self.f_botones_r.setObjectName(u"f_botones_r")
        sizePolicy.setHeightForWidth(self.f_botones_r.sizePolicy().hasHeightForWidth())
        self.f_botones_r.setSizePolicy(sizePolicy)
        self.f_botones_r.setMinimumSize(QSize(300, 50))
        self.f_botones_r.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.f_botones_r.setFrameShape(QFrame.Shape.NoFrame)
        self.f_botones_r.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.f_botones_r)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.b_volver = QPushButton(self.f_botones_r)
        self.b_volver.setObjectName(u"b_volver")
        sizePolicy4.setHeightForWidth(self.b_volver.sizePolicy().hasHeightForWidth())
        self.b_volver.setSizePolicy(sizePolicy4)
        self.b_volver.setMinimumSize(QSize(0, 40))
        self.b_volver.setFont(font1)
        self.b_volver.setStyleSheet(u"QPushButton{\n"
"	background: rgb(55, 55, 55);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")

        self.horizontalLayout_2.addWidget(self.b_volver)

        self.b_register_r = QPushButton(self.f_botones_r)
        self.b_register_r.setObjectName(u"b_register_r")
        sizePolicy4.setHeightForWidth(self.b_register_r.sizePolicy().hasHeightForWidth())
        self.b_register_r.setSizePolicy(sizePolicy4)
        self.b_register_r.setMinimumSize(QSize(0, 40))
        self.b_register_r.setFont(font1)
        self.b_register_r.setStyleSheet(u"QPushButton{\n"
"	background: rgb(55, 55, 55);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")

        self.horizontalLayout_2.addWidget(self.b_register_r)


        self.verticalLayout_6.addWidget(self.f_botones_r)


        self.verticalLayout_9.addWidget(self.f_rgister)

        self.stackedWidget.addWidget(self.pag_1)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Logni)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Logni)
    # setupUi

    def retranslateUi(self, Logni):
        Logni.setWindowTitle(QCoreApplication.translate("Logni", u"Form", None))
        self.label_logo.setText("")
        self.label_UNP.setText(QCoreApplication.translate("Logni", u"UNIVERSIDAD NORORIENTAL PRIVADA", None))
        self.label_GMA.setText(QCoreApplication.translate("Logni", u"GRAN MARISCAL DE AYACUCHO", None))
        self.label_user.setText(QCoreApplication.translate("Logni", u"User :", None))
        self.label_password.setText(QCoreApplication.translate("Logni", u"Passwprd :", None))
        self.lineedit_password_log.setText("")
        self.b_login.setText(QCoreApplication.translate("Logni", u"LOGIN ", None))
        self.b_register.setText(QCoreApplication.translate("Logni", u"REGISTER", None))
        self.label_logo_r.setText("")
        self.label_UNP_r.setText(QCoreApplication.translate("Logni", u"UNIVERSIDAD NORORIENTAL PRIVADA", None))
        self.label_GMA_r.setText(QCoreApplication.translate("Logni", u"GRAN MARISCAL DE AYACUCHO", None))
        self.label_user_r.setText(QCoreApplication.translate("Logni", u"User :", None))
        self.label_password_r.setText(QCoreApplication.translate("Logni", u"Passwprd :", None))
        self.label_confirmes.setText(QCoreApplication.translate("Logni", u"Confirmed Password :", None))
        self.b_volver.setText(QCoreApplication.translate("Logni", u"VOLVER", None))
        self.b_register_r.setText(QCoreApplication.translate("Logni", u"REGISTRAR", None))
    # retranslateUi

