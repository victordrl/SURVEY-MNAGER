# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_statgenerallrWkDC.ui'
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
    QVBoxLayout, QWidget)

class Ui_f_stat_general(object):
    def setupUi(self, f_stat_general):
        if not f_stat_general.objectName():
            f_stat_general.setObjectName(u"f_stat_general")
        f_stat_general.resize(1142, 618)
        self.verticalLayout = QVBoxLayout(f_stat_general)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.f_up = QFrame(f_stat_general)
        self.f_up.setObjectName(u"f_up")
        self.f_up.setMinimumSize(QSize(0, 40))
        self.f_up.setMaximumSize(QSize(16777215, 50))
        self.f_up.setStyleSheet(u"	background: rgba(70, 70, 70, 0.4);\n"
"	border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_up.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_up.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.f_up)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.f_up)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(450, 16777215))
        self.frame_3.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_escuela_img = QLabel(self.frame_3)
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

        self.horizontalLayout_26.addWidget(self.label_escuela_img)

        self.escuela_profe = QLabel(self.frame_3)
        self.escuela_profe.setObjectName(u"escuela_profe")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.escuela_profe.sizePolicy().hasHeightForWidth())
        self.escuela_profe.setSizePolicy(sizePolicy1)
        self.escuela_profe.setMinimumSize(QSize(50, 0))
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiLight Condensed"])
        font.setPointSize(18)
        self.escuela_profe.setFont(font)
        self.escuela_profe.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.escuela_profe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.escuela_profe)

        self.comboBox_escuelas = QComboBox(self.frame_3)
        self.comboBox_escuelas.setObjectName(u"comboBox_escuelas")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_escuelas.sizePolicy().hasHeightForWidth())
        self.comboBox_escuelas.setSizePolicy(sizePolicy2)
        self.comboBox_escuelas.setMinimumSize(QSize(200, 0))
        self.comboBox_escuelas.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT Condensed"])
        font1.setPointSize(14)
        self.comboBox_escuelas.setFont(font1)
        self.comboBox_escuelas.setStyleSheet(u"QComboBox {\n"
"	background: rgba(70, 70, 70, 0.7);\n"
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
"QComboBox QAbstractItemView {\n"
"    background: rgba(70, 70, 70,1);\n"
"    selection-background-color: rgba(40, 85, 165, 0.7);\n"
"}\n"
"\n"
"QPushButton::drop-down :hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::drop-down :pressed {\n"
"     background-color: rgba(55, 55, 145, 0.7);\n"
"}")
        self.comboBox_escuelas.setDuplicatesEnabled(False)
        self.comboBox_escuelas.setModelColumn(0)

        self.horizontalLayout_26.addWidget(self.comboBox_escuelas)


        self.horizontalLayout_27.addWidget(self.frame_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_7)

        self.frame_2 = QFrame(self.f_up)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(550, 16777215))
        self.frame_2.setStyleSheet(u"\n"
"background: rgba(70, 70, 70, 0);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_profesores_img = QLabel(self.frame_2)
        self.label_profesores_img.setObjectName(u"label_profesores_img")
        sizePolicy.setHeightForWidth(self.label_profesores_img.sizePolicy().hasHeightForWidth())
        self.label_profesores_img.setSizePolicy(sizePolicy)
        self.label_profesores_img.setMinimumSize(QSize(35, 35))
        self.label_profesores_img.setMaximumSize(QSize(30, 30))
        self.label_profesores_img.setPixmap(QPixmap(u"App_Icon/patient_list_40dp_FILL0_wght400_GRAD0_opsz40 (1).png"))
        self.label_profesores_img.setScaledContents(True)
        self.label_profesores_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_profesores_img)

        self.label_profesores = QLabel(self.frame_2)
        self.label_profesores.setObjectName(u"label_profesores")
        sizePolicy1.setHeightForWidth(self.label_profesores.sizePolicy().hasHeightForWidth())
        self.label_profesores.setSizePolicy(sizePolicy1)
        self.label_profesores.setMinimumSize(QSize(100, 0))
        self.label_profesores.setFont(font)
        self.label_profesores.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.label_profesores.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_profesores)

        self.f_chek_menu = QFrame(self.frame_2)
        self.f_chek_menu.setObjectName(u"f_chek_menu")
        sizePolicy2.setHeightForWidth(self.f_chek_menu.sizePolicy().hasHeightForWidth())
        self.f_chek_menu.setSizePolicy(sizePolicy2)
        self.f_chek_menu.setStyleSheet(u"background: rgba(70, 70, 70, 0.7);\n"
"")
        self.f_chek_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_chek_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_chek_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_25.addWidget(self.f_chek_menu)


        self.horizontalLayout_27.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.f_up)

        self.f_info = QFrame(f_stat_general)
        self.f_info.setObjectName(u"f_info")
        self.f_info.setMinimumSize(QSize(0, 35))
        self.f_info.setMaximumSize(QSize(16777215, 40))
        self.f_info.setStyleSheet(u"	background: rgba(70, 70, 70, 0.4);\n"
"	border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_info.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.f_info)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_fechas_img = QLabel(self.f_info)
        self.label_fechas_img.setObjectName(u"label_fechas_img")
        sizePolicy.setHeightForWidth(self.label_fechas_img.sizePolicy().hasHeightForWidth())
        self.label_fechas_img.setSizePolicy(sizePolicy)
        self.label_fechas_img.setMinimumSize(QSize(30, 30))
        self.label_fechas_img.setMaximumSize(QSize(30, 30))
        self.label_fechas_img.setPixmap(QPixmap(u"App_Icon/date_range_40dp_FILL0_wght400_GRAD0_opsz40.png"))
        self.label_fechas_img.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_fechas_img)

        self.label_fechas = QLabel(self.f_info)
        self.label_fechas.setObjectName(u"label_fechas")
        self.label_fechas.setMinimumSize(QSize(120, 0))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift SemiLight Condensed"])
        font2.setPointSize(14)
        self.label_fechas.setFont(font2)
        self.label_fechas.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.label_fechas.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_fechas)

        self.comboBox_fecha_inicio = QComboBox(self.f_info)
        self.comboBox_fecha_inicio.setObjectName(u"comboBox_fecha_inicio")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_fecha_inicio.sizePolicy().hasHeightForWidth())
        self.comboBox_fecha_inicio.setSizePolicy(sizePolicy3)
        self.comboBox_fecha_inicio.setMinimumSize(QSize(120, 20))
        font3 = QFont()
        font3.setFamilies([u"Tw Cen MT Condensed"])
        font3.setPointSize(12)
        self.comboBox_fecha_inicio.setFont(font3)
        self.comboBox_fecha_inicio.setStyleSheet(u"QComboBox {\n"
"	background: rgba(70, 70, 70, 0.7);\n"
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
"}QPushButton::drop-down :hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::drop-down :pressed {\n"
"     background-color: rgba(55, 55, 145, 0.7);\n"
"}")

        self.horizontalLayout.addWidget(self.comboBox_fecha_inicio)

        self.comboBox_fecha_final = QComboBox(self.f_info)
        self.comboBox_fecha_final.setObjectName(u"comboBox_fecha_final")
        sizePolicy3.setHeightForWidth(self.comboBox_fecha_final.sizePolicy().hasHeightForWidth())
        self.comboBox_fecha_final.setSizePolicy(sizePolicy3)
        self.comboBox_fecha_final.setMinimumSize(QSize(120, 20))
        self.comboBox_fecha_final.setFont(font3)
        self.comboBox_fecha_final.setStyleSheet(u"QComboBox {\n"
"	background: rgba(70, 70, 70, 0.7);\n"
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

        self.horizontalLayout.addWidget(self.comboBox_fecha_final)

        self.horizontalSpacer = QSpacerItem(100, 19, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_general_barra = QPushButton(self.f_info)
        self.b_general_barra.setObjectName(u"b_general_barra")
        sizePolicy1.setHeightForWidth(self.b_general_barra.sizePolicy().hasHeightForWidth())
        self.b_general_barra.setSizePolicy(sizePolicy1)
        self.b_general_barra.setMinimumSize(QSize(100, 0))
        self.b_general_barra.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift SemiLight Condensed"])
        font4.setPointSize(12)
        self.b_general_barra.setFont(font4)
        self.b_general_barra.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgba(40, 85, 165, 0.7);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"App_Icon/bar_chart_40dp_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_general_barra.setIcon(icon)
        self.b_general_barra.setCheckable(True)
        self.b_general_barra.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.b_general_barra)

        self.b_general_linea = QPushButton(self.f_info)
        self.b_general_linea.setObjectName(u"b_general_linea")
        sizePolicy1.setHeightForWidth(self.b_general_linea.sizePolicy().hasHeightForWidth())
        self.b_general_linea.setSizePolicy(sizePolicy1)
        self.b_general_linea.setMinimumSize(QSize(100, 0))
        self.b_general_linea.setMaximumSize(QSize(16777215, 30))
        self.b_general_linea.setFont(font4)
        self.b_general_linea.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgba(40, 85, 165, 0.7);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"App_Icon/timeline_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_general_linea.setIcon(icon1)
        self.b_general_linea.setCheckable(True)
        self.b_general_linea.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.b_general_linea)

        self.horizontalSpacer_6 = QSpacerItem(245, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.b_actualizar_grafi = QPushButton(self.f_info)
        self.b_actualizar_grafi.setObjectName(u"b_actualizar_grafi")
        sizePolicy.setHeightForWidth(self.b_actualizar_grafi.sizePolicy().hasHeightForWidth())
        self.b_actualizar_grafi.setSizePolicy(sizePolicy)
        self.b_actualizar_grafi.setMinimumSize(QSize(35, 35))
        self.b_actualizar_grafi.setMaximumSize(QSize(35, 35))
        self.b_actualizar_grafi.setStyleSheet(u"QPushButton{\n"
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
        icon2 = QIcon()
        icon2.addFile(u"App_Icon/autorenew_40dp_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_actualizar_grafi.setIcon(icon2)
        self.b_actualizar_grafi.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.b_actualizar_grafi)


        self.verticalLayout.addWidget(self.f_info)

        self.f_cuerpo = QFrame(f_stat_general)
        self.f_cuerpo.setObjectName(u"f_cuerpo")
        self.f_cuerpo.setStyleSheet(u"	background: rgba(70, 70, 70, 0.4);\n"
"	border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_cuerpo.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_cuerpo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.f_cuerpo)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(10, 10, 10, 10)
        self.f_graf_barra = QFrame(self.f_cuerpo)
        self.f_graf_barra.setObjectName(u"f_graf_barra")
        self.f_graf_barra.setFrameShape(QFrame.Shape.NoFrame)
        self.f_graf_barra.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.f_graf_barra)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_21.addWidget(self.f_graf_barra)

        self.f_graf_linea = QFrame(self.f_cuerpo)
        self.f_graf_linea.setObjectName(u"f_graf_linea")
        self.f_graf_linea.setFrameShape(QFrame.Shape.NoFrame)
        self.f_graf_linea.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.f_graf_linea)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_21.addWidget(self.f_graf_linea)


        self.verticalLayout.addWidget(self.f_cuerpo)


        self.retranslateUi(f_stat_general)

        QMetaObject.connectSlotsByName(f_stat_general)
    # setupUi

    def retranslateUi(self, f_stat_general):
        f_stat_general.setWindowTitle(QCoreApplication.translate("f_stat_general", u"Frame", None))
        self.label_escuela_img.setText("")
        self.escuela_profe.setText(QCoreApplication.translate("f_stat_general", u"Escuela ", None))
        self.label_profesores_img.setText("")
        self.label_profesores.setText(QCoreApplication.translate("f_stat_general", u"Profesores", None))
        self.label_fechas_img.setText("")
        self.label_fechas.setText(QCoreApplication.translate("f_stat_general", u"Rango de Fechas :", None))
        self.b_general_barra.setText(QCoreApplication.translate("f_stat_general", u"Barras", None))
        self.b_general_linea.setText(QCoreApplication.translate("f_stat_general", u"Lineas", None))
        self.b_actualizar_grafi.setText("")
    # retranslateUi

