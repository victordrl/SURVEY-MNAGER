# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_profemXrpMH.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_f_profe(object):
    def setupUi(self, f_profe):
        if not f_profe.objectName():
            f_profe.setObjectName(u"f_profe")
        f_profe.resize(837, 590)
        f_profe.setMinimumSize(QSize(830, 590))
        self.verticalLayout = QVBoxLayout(f_profe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.f_up = QFrame(f_profe)
        self.f_up.setObjectName(u"f_up")
        self.f_up.setMinimumSize(QSize(0, 40))
        self.f_up.setMaximumSize(QSize(16777215, 50))
        self.f_up.setStyleSheet(u"	background: rgba(70, 70, 70, 0.4);\n"
"	border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_up.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_up.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.f_up)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_escuela_img = QLabel(self.f_up)
        self.label_escuela_img.setObjectName(u"label_escuela_img")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_escuela_img.sizePolicy().hasHeightForWidth())
        self.label_escuela_img.setSizePolicy(sizePolicy)
        self.label_escuela_img.setMaximumSize(QSize(30, 30))
        self.label_escuela_img.setPixmap(QPixmap(u"App_Icon/school_40dp_FILL0_wght400_GRAD0_opsz40 (1).png"))
        self.label_escuela_img.setScaledContents(True)
        self.label_escuela_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_escuela_img)

        self.escuela_profe = QLabel(self.f_up)
        self.escuela_profe.setObjectName(u"escuela_profe")
        self.escuela_profe.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiLight Condensed"])
        font.setPointSize(18)
        self.escuela_profe.setFont(font)
        self.escuela_profe.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.escuela_profe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.escuela_profe)

        self.horizontalSpacer_3 = QSpacerItem(568, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.nombre_profe = QLabel(self.f_up)
        self.nombre_profe.setObjectName(u"nombre_profe")
        self.nombre_profe.setMinimumSize(QSize(400, 0))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift SemiLight Condensed"])
        font1.setPointSize(14)
        self.nombre_profe.setFont(font1)
        self.nombre_profe.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.nombre_profe.setMargin(5)
        self.nombre_profe.setIndent(5)

        self.horizontalLayout_4.addWidget(self.nombre_profe)

        self.perfil_profe = QLabel(self.f_up)
        self.perfil_profe.setObjectName(u"perfil_profe")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.perfil_profe.sizePolicy().hasHeightForWidth())
        self.perfil_profe.setSizePolicy(sizePolicy1)
        self.perfil_profe.setMinimumSize(QSize(45, 45))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift SemiLight Condensed"])
        font2.setPointSize(16)
        self.perfil_profe.setFont(font2)
        self.perfil_profe.setPixmap(QPixmap(u"App_Icon/account_circle_40dp_FILL0_wght400_GRAD0_opsz40 (1) 70x70.png"))
        self.perfil_profe.setScaledContents(False)

        self.horizontalLayout_4.addWidget(self.perfil_profe)


        self.verticalLayout.addWidget(self.f_up)

        self.f_dawn = QFrame(f_profe)
        self.f_dawn.setObjectName(u"f_dawn")
        self.f_dawn.setMinimumSize(QSize(0, 35))
        self.f_dawn.setMaximumSize(QSize(16777215, 40))
        self.f_dawn.setStyleSheet(u"	background: rgba(70, 70, 70, 0.4);\n"
"	border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_dawn.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_dawn.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.f_dawn)
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 0, 0, 0)
        self.label_fecha_img = QLabel(self.f_dawn)
        self.label_fecha_img.setObjectName(u"label_fecha_img")
        sizePolicy.setHeightForWidth(self.label_fecha_img.sizePolicy().hasHeightForWidth())
        self.label_fecha_img.setSizePolicy(sizePolicy)
        self.label_fecha_img.setMinimumSize(QSize(30, 30))
        self.label_fecha_img.setMaximumSize(QSize(30, 30))
        self.label_fecha_img.setPixmap(QPixmap(u"App_Icon/date_range_40dp_FILL0_wght400_GRAD0_opsz40.png"))
        self.label_fecha_img.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.label_fecha_img)

        self.label_fecha = QLabel(self.f_dawn)
        self.label_fecha.setObjectName(u"label_fecha")
        self.label_fecha.setMinimumSize(QSize(120, 0))
        font3 = QFont()
        font3.setFamilies([u"Tw Cen MT Condensed"])
        font3.setPointSize(14)
        self.label_fecha.setFont(font3)
        self.label_fecha.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.label_fecha.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_fecha)

        self.comboBox_fecha_inicio = QComboBox(self.f_dawn)
        self.comboBox_fecha_inicio.setObjectName(u"comboBox_fecha_inicio")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_fecha_inicio.sizePolicy().hasHeightForWidth())
        self.comboBox_fecha_inicio.setSizePolicy(sizePolicy2)
        self.comboBox_fecha_inicio.setMinimumSize(QSize(120, 20))
        font4 = QFont()
        font4.setFamilies([u"Tw Cen MT Condensed"])
        font4.setPointSize(12)
        self.comboBox_fecha_inicio.setFont(font4)
        self.comboBox_fecha_inicio.setStyleSheet(u"QComboBox {\n"
"	background: rgba(70, 70, 70, 1);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background: rgba(40, 85, 165, 0.7);\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::drop-down :hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::drop-down :pressed {\n"
"     background-color: rgba(55, 55, 145, 0.7);\n"
"}")

        self.horizontalLayout_28.addWidget(self.comboBox_fecha_inicio)

        self.comboBox_fecha_final = QComboBox(self.f_dawn)
        self.comboBox_fecha_final.setObjectName(u"comboBox_fecha_final")
        sizePolicy2.setHeightForWidth(self.comboBox_fecha_final.sizePolicy().hasHeightForWidth())
        self.comboBox_fecha_final.setSizePolicy(sizePolicy2)
        self.comboBox_fecha_final.setMinimumSize(QSize(120, 20))
        self.comboBox_fecha_final.setFont(font4)
        self.comboBox_fecha_final.setStyleSheet(u"QComboBox {\n"
"	background: rgba(70, 70, 70,1);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background: rgba(40, 85, 165, 0.7);\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton::drop-down :hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::drop-down :pressed {\n"
"     background-color: rgba(55, 55, 145, 0.7);\n"
"}")

        self.horizontalLayout_28.addWidget(self.comboBox_fecha_final)

        self.horizontalSpacer_6 = QSpacerItem(669, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_6)

        self.b_recarga_grafica = QPushButton(self.f_dawn)
        self.b_recarga_grafica.setObjectName(u"b_recarga_grafica")
        sizePolicy.setHeightForWidth(self.b_recarga_grafica.sizePolicy().hasHeightForWidth())
        self.b_recarga_grafica.setSizePolicy(sizePolicy)
        self.b_recarga_grafica.setMinimumSize(QSize(35, 35))
        self.b_recarga_grafica.setMaximumSize(QSize(35, 35))
        self.b_recarga_grafica.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(40, 85, 165, 0.7);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgba(55, 55, 145, 0.7);\n"
"}")
        icon = QIcon()
        icon.addFile(u"App_Icon/autorenew_40dp_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_recarga_grafica.setIcon(icon)
        self.b_recarga_grafica.setIconSize(QSize(32, 32))

        self.horizontalLayout_28.addWidget(self.b_recarga_grafica)


        self.verticalLayout.addWidget(self.f_dawn)

        self.f_cuerpo = QFrame(f_profe)
        self.f_cuerpo.setObjectName(u"f_cuerpo")
        self.f_cuerpo.setStyleSheet(u"	background: rgba(70, 70, 70, 0.4);\n"
"	border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_cuerpo.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_cuerpo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.f_cuerpo)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.f_graf_barra = QFrame(self.f_cuerpo)
        self.f_graf_barra.setObjectName(u"f_graf_barra")
        self.f_graf_barra.setFrameShape(QFrame.Shape.NoFrame)
        self.f_graf_barra.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.f_graf_barra)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.tab_graf_barra = QTabWidget(self.f_graf_barra)
        self.tab_graf_barra.setObjectName(u"tab_graf_barra")
        self.tab_graf_barra.setStyleSheet(u"background: rgba(50, 50, 50, 0);")

        self.horizontalLayout_3.addWidget(self.tab_graf_barra)


        self.horizontalLayout.addWidget(self.f_graf_barra)

        self.f_graf_linea = QFrame(self.f_cuerpo)
        self.f_graf_linea.setObjectName(u"f_graf_linea")
        self.f_graf_linea.setFrameShape(QFrame.Shape.NoFrame)
        self.f_graf_linea.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.f_graf_linea)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.tab_graf_linea = QTabWidget(self.f_graf_linea)
        self.tab_graf_linea.setObjectName(u"tab_graf_linea")
        self.tab_graf_linea.setStyleSheet(u"background: rgba(50, 50, 50, 0);")

        self.horizontalLayout_2.addWidget(self.tab_graf_linea)


        self.horizontalLayout.addWidget(self.f_graf_linea)


        self.verticalLayout.addWidget(self.f_cuerpo)


        self.retranslateUi(f_profe)

        self.tab_graf_barra.setCurrentIndex(-1)
        self.tab_graf_linea.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(f_profe)
    # setupUi

    def retranslateUi(self, f_profe):
        f_profe.setWindowTitle(QCoreApplication.translate("f_profe", u"Frame", None))
        self.label_escuela_img.setText("")
        self.escuela_profe.setText(QCoreApplication.translate("f_profe", u"Escuela ...", None))
        self.nombre_profe.setText(QCoreApplication.translate("f_profe", u"Nombre", None))
        self.perfil_profe.setText("")
        self.label_fecha_img.setText("")
        self.label_fecha.setText(QCoreApplication.translate("f_profe", u"Rango de Fechas :", None))
        self.b_recarga_grafica.setText("")
    # retranslateUi

