# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_formEtmyMH.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 640)
        MainWindow.setMinimumSize(QSize(1100, 640))
        MainWindow.setStyleSheet(u"QMainWindow { \n"
"	border: none;\n"
"}")
        self.w_central = QWidget(MainWindow)
        self.w_central.setObjectName(u"w_central")
        self.w_central.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(25, 25, 25)\n"
"}")
        self.verticalLayout = QVBoxLayout(self.w_central)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.f_cuerpo_up = QFrame(self.w_central)
        self.f_cuerpo_up.setObjectName(u"f_cuerpo_up")
        self.f_cuerpo_up.setMinimumSize(QSize(0, 45))
        self.f_cuerpo_up.setMaximumSize(QSize(16777215, 45))
        self.f_cuerpo_up.setStyleSheet(u"QFrame {\n"
"    background: rgb(35, 35, 35);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.f_cuerpo_up.setFrameShape(QFrame.Shape.NoFrame)
        self.f_cuerpo_up.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.f_cuerpo_up)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.f_logo = QFrame(self.f_cuerpo_up)
        self.f_logo.setObjectName(u"f_logo")
        self.f_logo.setMaximumSize(QSize(55, 45))
        self.f_logo.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.f_logo)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.b_logo = QPushButton(self.f_logo)
        self.b_logo.setObjectName(u"b_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_logo.sizePolicy().hasHeightForWidth())
        self.b_logo.setSizePolicy(sizePolicy)
        self.b_logo.setAutoFillBackground(False)
        self.b_logo.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(40, 85, 165, 0.7);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border: 0px solid;\n"
"    opacity: 0.5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")
        icon = QIcon()
        icon.addFile(u"App_Icon/cropped-UGMA-LOGO-1-Photoroom (4).png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_logo.setIcon(icon)
        self.b_logo.setIconSize(QSize(80, 80))
        self.b_logo.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.b_logo)


        self.horizontalLayout.addWidget(self.f_logo)

        self.f_barra = QFrame(self.f_cuerpo_up)
        self.f_barra.setObjectName(u"f_barra")
        sizePolicy.setHeightForWidth(self.f_barra.sizePolicy().hasHeightForWidth())
        self.f_barra.setSizePolicy(sizePolicy)
        self.f_barra.setMaximumSize(QSize(16777215, 45))
        self.f_barra.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.f_barra)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.b_perfil = QPushButton(self.f_barra)
        self.b_perfil.setObjectName(u"b_perfil")
        sizePolicy.setHeightForWidth(self.b_perfil.sizePolicy().hasHeightForWidth())
        self.b_perfil.setSizePolicy(sizePolicy)
        self.b_perfil.setMinimumSize(QSize(45, 45))
        self.b_perfil.setMaximumSize(QSize(40, 40))
        self.b_perfil.setStyleSheet(u"QPushButton{\n"
"	background: rgb(50, 50, 50);\n"
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
        icon1 = QIcon()
        icon1.addFile(u"App_Icon/person_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_perfil.setIcon(icon1)
        self.b_perfil.setIconSize(QSize(24, 24))
        self.b_perfil.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.b_perfil)

        self.f_perfil = QFrame(self.f_barra)
        self.f_perfil.setObjectName(u"f_perfil")
        self.f_perfil.setMaximumSize(QSize(60, 40))
        self.f_perfil.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.f_perfil)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.f_perfil, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout.addWidget(self.f_barra)


        self.verticalLayout.addWidget(self.f_cuerpo_up)

        self.f_cuerpo_dawn = QFrame(self.w_central)
        self.f_cuerpo_dawn.setObjectName(u"f_cuerpo_dawn")
        self.f_cuerpo_dawn.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.f_cuerpo_dawn)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.f_m_icon = QFrame(self.f_cuerpo_dawn)
        self.f_m_icon.setObjectName(u"f_m_icon")
        self.f_m_icon.setMinimumSize(QSize(55, 0))
        self.f_m_icon.setMaximumSize(QSize(50, 4000))
        self.f_m_icon.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.f_m_icon.setStyleSheet(u"QFrame {\n"
"    background: rgb(35, 35, 35);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.f_m_icon.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.f_m_icon)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.b_encuesta = QPushButton(self.f_m_icon)
        self.b_encuesta.setObjectName(u"b_encuesta")
        self.b_encuesta.setMinimumSize(QSize(55, 50))
        self.b_encuesta.setStyleSheet(u"QPushButton{\n"
"	background: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgba(40, 85, 165, 0.7);\n"
"	border-bottom-left-radius: 10px;\n"
" 	/*border-top-left-radius: 10px;*/\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"App_Icon/wysiwyg_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_encuesta.setIcon(icon2)
        self.b_encuesta.setIconSize(QSize(24, 24))
        self.b_encuesta.setCheckable(True)
        self.b_encuesta.setAutoExclusive(True)
        self.b_encuesta.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.b_encuesta)

        self.b_shear = QPushButton(self.f_m_icon)
        self.b_shear.setObjectName(u"b_shear")
        self.b_shear.setMinimumSize(QSize(55, 50))
        self.b_shear.setMouseTracking(True)
        self.b_shear.setStyleSheet(u"QPushButton{\n"
"	background: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgba(40, 85, 165, 0.7);\n"
"	border-bottom-left-radius: 10px;\n"
" 	border-top-left-radius: 10px;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"App_Icon/person_search_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_shear.setIcon(icon3)
        self.b_shear.setIconSize(QSize(24, 24))
        self.b_shear.setCheckable(True)
        self.b_shear.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.b_shear)

        self.b_stats = QPushButton(self.f_m_icon)
        self.b_stats.setObjectName(u"b_stats")
        self.b_stats.setMinimumSize(QSize(55, 50))
        self.b_stats.setStyleSheet(u"QPushButton{\n"
"	background: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgba(40, 85, 165, 0.7);\n"
"	border-bottom-left-radius: 10px;\n"
" 	border-top-left-radius: 10px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"App_Icon/stacked_bar_chart_40dp_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_stats.setIcon(icon4)
        self.b_stats.setIconSize(QSize(24, 24))
        self.b_stats.setCheckable(True)
        self.b_stats.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.b_stats)

        self.verticalSpacer = QSpacerItem(20, 257, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.b_config = QPushButton(self.f_m_icon)
        self.b_config.setObjectName(u"b_config")
        self.b_config.setMinimumSize(QSize(55, 50))
        self.b_config.setStyleSheet(u"QPushButton{\n"
"	background: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"App_Icon/toggle_off_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u"App_Icon/toggle_on_40dp_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.On)
        self.b_config.setIcon(icon5)
        self.b_config.setIconSize(QSize(24, 24))
        self.b_config.setCheckable(True)
        self.b_config.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.b_config)


        self.horizontalLayout_2.addWidget(self.f_m_icon)

        self.f_ventanas = QFrame(self.f_cuerpo_dawn)
        self.f_ventanas.setObjectName(u"f_ventanas")
        sizePolicy.setHeightForWidth(self.f_ventanas.sizePolicy().hasHeightForWidth())
        self.f_ventanas.setSizePolicy(sizePolicy)
        self.f_ventanas.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.f_ventanas)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.f_ventanas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pag_0 = QWidget()
        self.pag_0.setObjectName(u"pag_0")
        self.horizontalLayout_10 = QHBoxLayout(self.pag_0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.f_pag0_inicio = QFrame(self.pag_0)
        self.f_pag0_inicio.setObjectName(u"f_pag0_inicio")
        self.f_pag0_inicio.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.f_pag0_inicio)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.f_pag0_inicio)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(64, 64))
        self.label.setMaximumSize(QSize(430, 325))
        self.label.setPixmap(QPixmap(u"App_Icon/cropped-UGMA-LOGO-1-Photoroom (6).png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_10.addWidget(self.f_pag0_inicio)

        self.stackedWidget.addWidget(self.pag_0)
        self.pag_1 = QWidget()
        self.pag_1.setObjectName(u"pag_1")
        self.horizontalLayout_4 = QHBoxLayout(self.pag_1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.f_pag4_shear = QFrame(self.pag_1)
        self.f_pag4_shear.setObjectName(u"f_pag4_shear")
        self.f_pag4_shear.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pag4_shear.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.f_pag4_shear)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.f_shear_up = QFrame(self.f_pag4_shear)
        self.f_shear_up.setObjectName(u"f_shear_up")
        self.f_shear_up.setMaximumSize(QSize(16777215, 40))
        self.f_shear_up.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.f_shear_up.setStyleSheet(u"QFrame {\n"
"    background: rgba(60, 60, 60, 0.7);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.f_shear_up.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_shear_up.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.f_shear_up)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.b_shear_2 = QPushButton(self.f_shear_up)
        self.b_shear_2.setObjectName(u"b_shear_2")
        self.b_shear_2.setMinimumSize(QSize(50, 35))
        self.b_shear_2.setMaximumSize(QSize(50, 35))
        self.b_shear_2.setMouseTracking(True)
        self.b_shear_2.setStyleSheet(u"QPushButton{\n"
"	background: rgb(55, 55, 55);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"App_Icon/search_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_shear_2.setIcon(icon6)
        self.b_shear_2.setIconSize(QSize(24, 24))
        self.b_shear_2.setCheckable(False)
        self.b_shear_2.setAutoExclusive(False)

        self.horizontalLayout_11.addWidget(self.b_shear_2)

        self.lineEdit = QLineEdit(self.f_shear_up)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 35))
        self.lineEdit.setMaximumSize(QSize(400, 35))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"	stop:0 rgb(105, 105, 105),\n"
"	stop:1 rgb(55, 55, 55));\n"
"    border-bottom-left-radius: 10px;\n"
"}")
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_11.addWidget(self.lineEdit)


        self.verticalLayout_3.addWidget(self.f_shear_up, 0, Qt.AlignmentFlag.AlignHCenter)

        self.f_shear_dawn = QFrame(self.f_pag4_shear)
        self.f_shear_dawn.setObjectName(u"f_shear_dawn")
        self.f_shear_dawn.setStyleSheet(u"background: rgba(35, 35, 35,1);\n"
"border-radius: 10px;")
        self.f_shear_dawn.setFrameShape(QFrame.Shape.NoFrame)
        self.f_shear_dawn.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.f_shear_dawn)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.scrollArea = QScrollArea(self.f_shear_dawn)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/*QScrollBar:vertical {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"	stop:0 rgb(105, 105, 105),\n"
"	stop:1rgb(130, 130, 130));\n"
"	border-radius: 15px; \n"
"	width: 10px; \n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: rgb(55, 55, 55);\n"
"	border-radius: 15px; \n"
"}\n"
"\n"
"QScrollBar::handle:hover{\n"
"	background: rgb(55, 55, 145);\n"
"}*/\n"
"QScrollBar:vertical {\n"
"	background: rgb(105, 105, 105);\n"
"	border-radius: 15px; \n"
"	width: 10px; \n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: rgb(55, 55, 55);\n"
"	border-radius: 15px; \n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContents = QWidget()
        self.scrollAreaContents.setObjectName(u"scrollAreaContents")
        self.scrollAreaContents.setGeometry(QRect(0, 0, 1005, 510))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaContents)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.verticalLayout_3.addWidget(self.f_shear_dawn)


        self.horizontalLayout_4.addWidget(self.f_pag4_shear)

        self.stackedWidget.addWidget(self.pag_1)
        self.pag_2 = QWidget()
        self.pag_2.setObjectName(u"pag_2")
        self.horizontalLayout_16 = QHBoxLayout(self.pag_2)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.f_pag5_perfil = QFrame(self.pag_2)
        self.f_pag5_perfil.setObjectName(u"f_pag5_perfil")
        self.f_pag5_perfil.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pag5_perfil.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.f_pag5_perfil)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.f_marco_perfil = QFrame(self.f_pag5_perfil)
        self.f_marco_perfil.setObjectName(u"f_marco_perfil")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.f_marco_perfil.sizePolicy().hasHeightForWidth())
        self.f_marco_perfil.setSizePolicy(sizePolicy2)
        self.f_marco_perfil.setMinimumSize(QSize(500, 300))
        self.f_marco_perfil.setStyleSheet(u"")
        self.f_marco_perfil.setFrameShape(QFrame.Shape.NoFrame)
        self.f_marco_perfil.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_15 = QVBoxLayout(self.f_marco_perfil)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.f_distribucuin_perfil = QFrame(self.f_marco_perfil)
        self.f_distribucuin_perfil.setObjectName(u"f_distribucuin_perfil")
        self.f_distribucuin_perfil.setStyleSheet(u"/*background: rgba(105, 105, 105, 0.4);\n"
"border-radius: 10px; */\n"
"background: rgba(50, 50, 50, 0.4);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_distribucuin_perfil.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_distribucuin_perfil.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.f_distribucuin_perfil)
        self.gridLayout.setObjectName(u"gridLayout")
        self.f_datos = QFrame(self.f_distribucuin_perfil)
        self.f_datos.setObjectName(u"f_datos")
        sizePolicy.setHeightForWidth(self.f_datos.sizePolicy().hasHeightForWidth())
        self.f_datos.setSizePolicy(sizePolicy)
        self.f_datos.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_datos.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.f_datos)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_correo = QLabel(self.f_datos)
        self.label_correo.setObjectName(u"label_correo")
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT Condensed"])
        font1.setPointSize(16)
        self.label_correo.setFont(font1)
        self.label_correo.setMargin(5)
        self.label_correo.setIndent(5)

        self.gridLayout_2.addWidget(self.label_correo, 1, 0, 1, 1)

        self.label_padsword = QLabel(self.f_datos)
        self.label_padsword.setObjectName(u"label_padsword")
        self.label_padsword.setMinimumSize(QSize(200, 0))
        self.label_padsword.setFont(font1)
        self.label_padsword.setStyleSheet(u"background: rgba(105, 105, 105, 0);")
        self.label_padsword.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_padsword.setMargin(5)
        self.label_padsword.setIndent(5)

        self.gridLayout_2.addWidget(self.label_padsword, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_escuela = QLabel(self.f_datos)
        self.label_escuela.setObjectName(u"label_escuela")
        self.label_escuela.setFont(font1)
        self.label_escuela.setMargin(5)
        self.label_escuela.setIndent(5)

        self.gridLayout_2.addWidget(self.label_escuela, 0, 0, 1, 1)

        self.label_direccion = QLabel(self.f_datos)
        self.label_direccion.setObjectName(u"label_direccion")
        self.label_direccion.setFont(font1)
        self.label_direccion.setMargin(5)
        self.label_direccion.setIndent(5)

        self.gridLayout_2.addWidget(self.label_direccion, 1, 1, 1, 1)

        self.lineedit_password = QLineEdit(self.f_datos)
        self.lineedit_password.setObjectName(u"lineedit_password")
        sizePolicy.setHeightForWidth(self.lineedit_password.sizePolicy().hasHeightForWidth())
        self.lineedit_password.setSizePolicy(sizePolicy)
        self.lineedit_password.setMinimumSize(QSize(200, 0))
        font2 = QFont()
        font2.setFamilies([u"Tw Cen MT Condensed"])
        font2.setPointSize(14)
        self.lineedit_password.setFont(font2)
        self.lineedit_password.setStyleSheet(u"QLineEdit { \n"
"	padding-left: 5px; \n"
"}")
        self.lineedit_password.setInputMask(u"")
        self.lineedit_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineedit_password.setCursorPosition(4)
        self.lineedit_password.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineedit_password.setDragEnabled(False)
        self.lineedit_password.setReadOnly(True)
        self.lineedit_password.setPlaceholderText(u"")
        self.lineedit_password.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.lineedit_password, 2, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_telefono = QLabel(self.f_datos)
        self.label_telefono.setObjectName(u"label_telefono")
        self.label_telefono.setFont(font1)
        self.label_telefono.setMargin(5)
        self.label_telefono.setIndent(5)

        self.gridLayout_2.addWidget(self.label_telefono, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.f_datos, 1, 0, 1, 2)

        self.label_img = QLabel(self.f_distribucuin_perfil)
        self.label_img.setObjectName(u"label_img")
        sizePolicy.setHeightForWidth(self.label_img.sizePolicy().hasHeightForWidth())
        self.label_img.setSizePolicy(sizePolicy)
        self.label_img.setMinimumSize(QSize(130, 130))
        self.label_img.setPixmap(QPixmap(u"App_Icon/account_circle_40dp_FILL0_wght400_GRAD0_opsz40 (1).png"))

        self.gridLayout.addWidget(self.label_img, 0, 0, 1, 1)

        self.f_nick = QFrame(self.f_distribucuin_perfil)
        self.f_nick.setObjectName(u"f_nick")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.f_nick.sizePolicy().hasHeightForWidth())
        self.f_nick.setSizePolicy(sizePolicy3)
        self.f_nick.setMinimumSize(QSize(130, 130))
        self.f_nick.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_nick.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.f_nick)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_nick = QLabel(self.f_nick)
        self.label_nick.setObjectName(u"label_nick")
        sizePolicy.setHeightForWidth(self.label_nick.sizePolicy().hasHeightForWidth())
        self.label_nick.setSizePolicy(sizePolicy)
        self.label_nick.setMinimumSize(QSize(200, 0))
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift SemiBold Condensed"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.label_nick.setFont(font3)
        self.label_nick.setMargin(5)
        self.label_nick.setIndent(5)

        self.gridLayout_3.addWidget(self.label_nick, 0, 0, 1, 1)

        self.label_apellido = QLabel(self.f_nick)
        self.label_apellido.setObjectName(u"label_apellido")
        sizePolicy3.setHeightForWidth(self.label_apellido.sizePolicy().hasHeightForWidth())
        self.label_apellido.setSizePolicy(sizePolicy3)
        self.label_apellido.setMinimumSize(QSize(200, 0))
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift SemiLight Condensed"])
        font4.setPointSize(16)
        font4.setBold(False)
        self.label_apellido.setFont(font4)
        self.label_apellido.setStyleSheet(u"background: rgba(105, 105, 105, 0);")
        self.label_apellido.setMargin(5)
        self.label_apellido.setIndent(5)

        self.gridLayout_3.addWidget(self.label_apellido, 1, 0, 1, 1)

        self.label_nombre = QLabel(self.f_nick)
        self.label_nombre.setObjectName(u"label_nombre")
        sizePolicy3.setHeightForWidth(self.label_nombre.sizePolicy().hasHeightForWidth())
        self.label_nombre.setSizePolicy(sizePolicy3)
        self.label_nombre.setMinimumSize(QSize(200, 0))
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift SemiLight Condensed"])
        font5.setPointSize(16)
        self.label_nombre.setFont(font5)
        self.label_nombre.setStyleSheet(u"background: rgba(105, 105, 105,0);")
        self.label_nombre.setMargin(5)
        self.label_nombre.setIndent(5)

        self.gridLayout_3.addWidget(self.label_nombre, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.f_nick, 0, 1, 1, 1)


        self.verticalLayout_15.addWidget(self.f_distribucuin_perfil)

        self.frame = QFrame(self.f_marco_perfil)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background: rgba(35, 35, 35,1);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame)
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_2)

        self.b_cerrar_secion = QPushButton(self.frame)
        self.b_cerrar_secion.setObjectName(u"b_cerrar_secion")
        self.b_cerrar_secion.setMinimumSize(QSize(150, 30))
        self.b_cerrar_secion.setMaximumSize(QSize(200, 50))
        self.b_cerrar_secion.setFont(font2)
        self.b_cerrar_secion.setStyleSheet(u"QPushButton{\n"
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
        icon7 = QIcon()
        icon7.addFile(u"App_Icon/person_cancel_40dp_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_cerrar_secion.setIcon(icon7)

        self.horizontalLayout_24.addWidget(self.b_cerrar_secion)

        self.b_ver_password = QPushButton(self.frame)
        self.b_ver_password.setObjectName(u"b_ver_password")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.b_ver_password.sizePolicy().hasHeightForWidth())
        self.b_ver_password.setSizePolicy(sizePolicy4)
        self.b_ver_password.setMinimumSize(QSize(50, 30))
        self.b_ver_password.setMaximumSize(QSize(100, 50))
        font6 = QFont()
        font6.setPointSize(14)
        self.b_ver_password.setFont(font6)
        self.b_ver_password.setStyleSheet(u"QPushButton{\n"
"	background: rgb(55, 55, 55);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgba(40, 85, 165, 0.7);\n"
"	border-bottom-left-radius: 10px;\n"
" 	border-top-left-radius: 10px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"App_Icon/visibility_off_40dp_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u"App_Icon/visibility_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.On)
        self.b_ver_password.setIcon(icon8)
        self.b_ver_password.setCheckable(True)
        self.b_ver_password.setChecked(False)
        self.b_ver_password.setAutoRepeat(False)

        self.horizontalLayout_24.addWidget(self.b_ver_password)

        self.b_cambiar_pasworld = QPushButton(self.frame)
        self.b_cambiar_pasworld.setObjectName(u"b_cambiar_pasworld")
        sizePolicy4.setHeightForWidth(self.b_cambiar_pasworld.sizePolicy().hasHeightForWidth())
        self.b_cambiar_pasworld.setSizePolicy(sizePolicy4)
        self.b_cambiar_pasworld.setMinimumSize(QSize(150, 30))
        self.b_cambiar_pasworld.setMaximumSize(QSize(200, 50))
        self.b_cambiar_pasworld.setFont(font2)
        self.b_cambiar_pasworld.setStyleSheet(u"QPushButton{\n"
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
        icon9 = QIcon()
        icon9.addFile(u"App_Icon/app_registration_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_cambiar_pasworld.setIcon(icon9)

        self.horizontalLayout_24.addWidget(self.b_cambiar_pasworld)

        self.horizontalSpacer_3 = QSpacerItem(200, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_3)


        self.verticalLayout_15.addWidget(self.frame)


        self.horizontalLayout_17.addWidget(self.f_marco_perfil)


        self.horizontalLayout_16.addWidget(self.f_pag5_perfil)

        self.stackedWidget.addWidget(self.pag_2)
        self.pag_3 = QWidget()
        self.pag_3.setObjectName(u"pag_3")
        self.horizontalLayout_9 = QHBoxLayout(self.pag_3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.f_pag3_config = QFrame(self.pag_3)
        self.f_pag3_config.setObjectName(u"f_pag3_config")
        self.f_pag3_config.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pag3_config.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.f_pag3_config)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 210, 691, 361))
        self.label_4.setMinimumSize(QSize(32, 32))
        self.label_4.setPixmap(QPixmap(u"../../.designer/VS Code/PROYECTO QT PY/APP/images/images/ugma.png"))

        self.horizontalLayout_9.addWidget(self.f_pag3_config)

        self.stackedWidget.addWidget(self.pag_3)
        self.pag_4 = QWidget()
        self.pag_4.setObjectName(u"pag_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pag_4.sizePolicy().hasHeightForWidth())
        self.pag_4.setSizePolicy(sizePolicy5)
        self.horizontalLayout_7 = QHBoxLayout(self.pag_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.f_pag2_stats = QFrame(self.pag_4)
        self.f_pag2_stats.setObjectName(u"f_pag2_stats")
        self.f_pag2_stats.setStyleSheet(u"")
        self.f_pag2_stats.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pag2_stats.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.f_pag2_stats)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tabWidget = QTabWidget(self.f_pag2_stats)
        self.tabWidget.setObjectName(u"tabWidget")
        font7 = QFont()
        font7.setFamilies([u"Tw Cen MT Condensed"])
        font7.setPointSize(12)
        self.tabWidget.setFont(font7)
        self.tabWidget.setStyleSheet(u"\n"
"background: rgba(35, 35, 35,1);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setTabBarAutoHide(False)

        self.horizontalLayout_13.addWidget(self.tabWidget)


        self.horizontalLayout_7.addWidget(self.f_pag2_stats)

        self.stackedWidget.addWidget(self.pag_4)
        self.pag_5 = QWidget()
        self.pag_5.setObjectName(u"pag_5")
        self.pag_5.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.horizontalLayout_8 = QHBoxLayout(self.pag_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.f_pag1_encuesta = QFrame(self.pag_5)
        self.f_pag1_encuesta.setObjectName(u"f_pag1_encuesta")
        self.f_pag1_encuesta.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pag1_encuesta.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.f_pag1_encuesta)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget_2 = QStackedWidget(self.f_pag1_encuesta)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.e_pag_0 = QWidget()
        self.e_pag_0.setObjectName(u"e_pag_0")
        self.verticalLayout_9 = QVBoxLayout(self.e_pag_0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.f_epage0_dawn = QFrame(self.e_pag_0)
        self.f_epage0_dawn.setObjectName(u"f_epage0_dawn")
        self.f_epage0_dawn.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_epage0_dawn.setFrameShape(QFrame.Shape.NoFrame)
        self.f_epage0_dawn.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.f_epage0_dawn)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.b_edit_encuesta = QPushButton(self.f_epage0_dawn)
        self.b_edit_encuesta.setObjectName(u"b_edit_encuesta")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.b_edit_encuesta.sizePolicy().hasHeightForWidth())
        self.b_edit_encuesta.setSizePolicy(sizePolicy6)
        font8 = QFont()
        font8.setFamilies([u"Tw Cen MT Condensed"])
        font8.setPointSize(26)
        font8.setHintingPreference(QFont.PreferDefaultHinting)
        self.b_edit_encuesta.setFont(font8)
        self.b_edit_encuesta.setStyleSheet(u"QPushButton{\n"
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
        icon10 = QIcon()
        icon10.addFile(u"App_Icon/edit_document_40dp_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_edit_encuesta.setIcon(icon10)
        self.b_edit_encuesta.setIconSize(QSize(90, 90))
        self.b_edit_encuesta.setCheckable(False)

        self.gridLayout_4.addWidget(self.b_edit_encuesta, 0, 0, 1, 1)

        self.line = QFrame(self.f_epage0_dawn)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background: rgb(60, 60, 60);\n"
"border-radius: 10px; ")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line, 0, 1, 2, 1)

        self.b_enviar_encuesta = QPushButton(self.f_epage0_dawn)
        self.b_enviar_encuesta.setObjectName(u"b_enviar_encuesta")
        sizePolicy6.setHeightForWidth(self.b_enviar_encuesta.sizePolicy().hasHeightForWidth())
        self.b_enviar_encuesta.setSizePolicy(sizePolicy6)
        font9 = QFont()
        font9.setFamilies([u"Tw Cen MT Condensed"])
        font9.setPointSize(26)
        font9.setBold(False)
        self.b_enviar_encuesta.setFont(font9)
        self.b_enviar_encuesta.setStyleSheet(u"QPushButton{\n"
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
        icon11 = QIcon()
        icon11.addFile(u"App_Icon/forward_to_inbox_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_enviar_encuesta.setIcon(icon11)
        self.b_enviar_encuesta.setIconSize(QSize(90, 90))
        self.b_enviar_encuesta.setCheckable(False)

        self.gridLayout_4.addWidget(self.b_enviar_encuesta, 0, 2, 1, 1)

        self.b_editar_profes = QPushButton(self.f_epage0_dawn)
        self.b_editar_profes.setObjectName(u"b_editar_profes")
        sizePolicy6.setHeightForWidth(self.b_editar_profes.sizePolicy().hasHeightForWidth())
        self.b_editar_profes.setSizePolicy(sizePolicy6)
        self.b_editar_profes.setFont(font9)
        self.b_editar_profes.setStyleSheet(u"QPushButton{\n"
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
        icon12 = QIcon()
        icon12.addFile(u"App_Icon/groups_2_40dp_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_editar_profes.setIcon(icon12)
        self.b_editar_profes.setIconSize(QSize(90, 90))
        self.b_editar_profes.setCheckable(False)

        self.gridLayout_4.addWidget(self.b_editar_profes, 1, 0, 1, 1)

        self.b_editar_estudiantes = QPushButton(self.f_epage0_dawn)
        self.b_editar_estudiantes.setObjectName(u"b_editar_estudiantes")
        sizePolicy6.setHeightForWidth(self.b_editar_estudiantes.sizePolicy().hasHeightForWidth())
        self.b_editar_estudiantes.setSizePolicy(sizePolicy6)
        self.b_editar_estudiantes.setFont(font9)
        self.b_editar_estudiantes.setStyleSheet(u"QPushButton{\n"
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
        icon13 = QIcon()
        icon13.addFile(u"App_Icon/group_add_40dp_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_editar_estudiantes.setIcon(icon13)
        self.b_editar_estudiantes.setIconSize(QSize(90, 90))
        self.b_editar_estudiantes.setCheckable(False)

        self.gridLayout_4.addWidget(self.b_editar_estudiantes, 1, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.f_epage0_dawn)

        self.stackedWidget_2.addWidget(self.e_pag_0)
        self.e_pag_2 = QWidget()
        self.e_pag_2.setObjectName(u"e_pag_2")
        self.verticalLayout_34 = QVBoxLayout(self.e_pag_2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.f_edit_barr_profes = QFrame(self.e_pag_2)
        self.f_edit_barr_profes.setObjectName(u"f_edit_barr_profes")
        self.f_edit_barr_profes.setMinimumSize(QSize(0, 45))
        self.f_edit_barr_profes.setMaximumSize(QSize(16777215, 45))
        self.f_edit_barr_profes.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_edit_barr_profes.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_edit_barr_profes.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.f_edit_barr_profes)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.f_edit_barr_profes)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 0))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u" background-color: rgba(40, 40, 40, 0);\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)

        self.b_atras_agegar_profe = QPushButton(self.f_edit_barr_profes)
        self.b_atras_agegar_profe.setObjectName(u"b_atras_agegar_profe")
        sizePolicy.setHeightForWidth(self.b_atras_agegar_profe.sizePolicy().hasHeightForWidth())
        self.b_atras_agegar_profe.setSizePolicy(sizePolicy)
        self.b_atras_agegar_profe.setMinimumSize(QSize(45, 0))
        self.b_atras_agegar_profe.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(40, 40, 40, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	border-bottom-left-radius: 10px;\n"
" 	border-top-left-radius: 10px;\n"
" 	/*border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;*/\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"App_Icon/keyboard_return_40dp_FILL0_wght400_GRAD0_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_atras_agegar_profe.setIcon(icon14)

        self.horizontalLayout_21.addWidget(self.b_atras_agegar_profe)

        self.b_cancelar_agegar_profe = QPushButton(self.f_edit_barr_profes)
        self.b_cancelar_agegar_profe.setObjectName(u"b_cancelar_agegar_profe")
        sizePolicy.setHeightForWidth(self.b_cancelar_agegar_profe.sizePolicy().hasHeightForWidth())
        self.b_cancelar_agegar_profe.setSizePolicy(sizePolicy)
        self.b_cancelar_agegar_profe.setMinimumSize(QSize(45, 0))
        self.b_cancelar_agegar_profe.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(40, 40, 40, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(130, 55, 90, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(130, 55, 90, 1);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"App_Icon/close_small_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_cancelar_agegar_profe.setIcon(icon15)

        self.horizontalLayout_21.addWidget(self.b_cancelar_agegar_profe)

        self.b_guardar_agegar_profe = QPushButton(self.f_edit_barr_profes)
        self.b_guardar_agegar_profe.setObjectName(u"b_guardar_agegar_profe")
        sizePolicy.setHeightForWidth(self.b_guardar_agegar_profe.sizePolicy().hasHeightForWidth())
        self.b_guardar_agegar_profe.setSizePolicy(sizePolicy)
        self.b_guardar_agegar_profe.setMinimumSize(QSize(45, 0))
        self.b_guardar_agegar_profe.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(40, 40, 40, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	/*border-bottom-left-radius: 10px;\n"
" 	border-top-left-radius: 10px;*/\n"
" 	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"App_Icon/cloud_upload_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_guardar_agegar_profe.setIcon(icon16)

        self.horizontalLayout_21.addWidget(self.b_guardar_agegar_profe)


        self.verticalLayout_34.addWidget(self.f_edit_barr_profes)

        self.f_edit_dawn_profe = QFrame(self.e_pag_2)
        self.f_edit_dawn_profe.setObjectName(u"f_edit_dawn_profe")
        self.f_edit_dawn_profe.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);\n"
"border-radius: 10px;\n"
"\n"
"color: rgba(255, 255, 255, 1);")
        self.f_edit_dawn_profe.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_edit_dawn_profe.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_34.addWidget(self.f_edit_dawn_profe)

        self.stackedWidget_2.addWidget(self.e_pag_2)
        self.e_pag_3 = QWidget()
        self.e_pag_3.setObjectName(u"e_pag_3")
        self.verticalLayout_35 = QVBoxLayout(self.e_pag_3)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.f_edit_barr_estud = QFrame(self.e_pag_3)
        self.f_edit_barr_estud.setObjectName(u"f_edit_barr_estud")
        self.f_edit_barr_estud.setMinimumSize(QSize(0, 45))
        self.f_edit_barr_estud.setMaximumSize(QSize(16777215, 45))
        self.f_edit_barr_estud.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_edit_barr_estud.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_edit_barr_estud.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.f_edit_barr_estud)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.f_edit_barr_estud)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 0))
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u" background-color: rgba(40, 40, 40, 0);\n"
"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_6)

        self.b_atras_agegar_estud = QPushButton(self.f_edit_barr_estud)
        self.b_atras_agegar_estud.setObjectName(u"b_atras_agegar_estud")
        sizePolicy.setHeightForWidth(self.b_atras_agegar_estud.sizePolicy().hasHeightForWidth())
        self.b_atras_agegar_estud.setSizePolicy(sizePolicy)
        self.b_atras_agegar_estud.setMinimumSize(QSize(45, 0))
        self.b_atras_agegar_estud.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(40, 40, 40, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	border-bottom-left-radius: 10px;\n"
" 	border-top-left-radius: 10px;\n"
" 	/*border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;*/\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")
        self.b_atras_agegar_estud.setIcon(icon14)

        self.horizontalLayout_22.addWidget(self.b_atras_agegar_estud)

        self.b_cancelar_agegar_estud = QPushButton(self.f_edit_barr_estud)
        self.b_cancelar_agegar_estud.setObjectName(u"b_cancelar_agegar_estud")
        sizePolicy.setHeightForWidth(self.b_cancelar_agegar_estud.sizePolicy().hasHeightForWidth())
        self.b_cancelar_agegar_estud.setSizePolicy(sizePolicy)
        self.b_cancelar_agegar_estud.setMinimumSize(QSize(45, 0))
        self.b_cancelar_agegar_estud.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(40, 40, 40, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(130, 55, 90, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(130, 55, 90, 1);\n"
"}")
        self.b_cancelar_agegar_estud.setIcon(icon15)

        self.horizontalLayout_22.addWidget(self.b_cancelar_agegar_estud)

        self.b_guardar_agegar_estud = QPushButton(self.f_edit_barr_estud)
        self.b_guardar_agegar_estud.setObjectName(u"b_guardar_agegar_estud")
        sizePolicy.setHeightForWidth(self.b_guardar_agegar_estud.sizePolicy().hasHeightForWidth())
        self.b_guardar_agegar_estud.setSizePolicy(sizePolicy)
        self.b_guardar_agegar_estud.setMinimumSize(QSize(45, 0))
        self.b_guardar_agegar_estud.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(40, 40, 40, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	/*border-bottom-left-radius: 10px;\n"
" 	border-top-left-radius: 10px;*/\n"
" 	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")
        self.b_guardar_agegar_estud.setIcon(icon16)

        self.horizontalLayout_22.addWidget(self.b_guardar_agegar_estud)


        self.verticalLayout_35.addWidget(self.f_edit_barr_estud)

        self.f_edit_dawn_estud = QFrame(self.e_pag_3)
        self.f_edit_dawn_estud.setObjectName(u"f_edit_dawn_estud")
        self.f_edit_dawn_estud.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);\n"
"border-radius: 10px;\n"
"\n"
"color: rgba(255, 255, 255, 1);")
        self.f_edit_dawn_estud.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_edit_dawn_estud.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_35.addWidget(self.f_edit_dawn_estud)

        self.stackedWidget_2.addWidget(self.e_pag_3)
        self.e_pag_1 = QWidget()
        self.e_pag_1.setObjectName(u"e_pag_1")
        self.e_pag_1.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.e_pag_1)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.f_edit_barr = QFrame(self.e_pag_1)
        self.f_edit_barr.setObjectName(u"f_edit_barr")
        self.f_edit_barr.setMinimumSize(QSize(0, 45))
        self.f_edit_barr.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_edit_barr.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_edit_barr.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.f_edit_barr)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.f_edit_barr)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 0))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u" background-color: rgba(40, 40, 40, 0);\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer)

        self.b_atras_encuesta = QPushButton(self.f_edit_barr)
        self.b_atras_encuesta.setObjectName(u"b_atras_encuesta")
        sizePolicy.setHeightForWidth(self.b_atras_encuesta.sizePolicy().hasHeightForWidth())
        self.b_atras_encuesta.setSizePolicy(sizePolicy)
        self.b_atras_encuesta.setMinimumSize(QSize(45, 0))
        self.b_atras_encuesta.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(40, 40, 40, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	border-bottom-left-radius: 10px;\n"
" 	border-top-left-radius: 10px;\n"
" 	/*border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;*/\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")
        self.b_atras_encuesta.setIcon(icon14)

        self.horizontalLayout_18.addWidget(self.b_atras_encuesta)

        self.b_cancelar_encuesta = QPushButton(self.f_edit_barr)
        self.b_cancelar_encuesta.setObjectName(u"b_cancelar_encuesta")
        sizePolicy.setHeightForWidth(self.b_cancelar_encuesta.sizePolicy().hasHeightForWidth())
        self.b_cancelar_encuesta.setSizePolicy(sizePolicy)
        self.b_cancelar_encuesta.setMinimumSize(QSize(45, 0))
        self.b_cancelar_encuesta.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(40, 40, 40, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(130, 55, 90, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(130, 55, 90, 1);\n"
"}")
        self.b_cancelar_encuesta.setIcon(icon15)

        self.horizontalLayout_18.addWidget(self.b_cancelar_encuesta)

        self.b_guardar_encuesta = QPushButton(self.f_edit_barr)
        self.b_guardar_encuesta.setObjectName(u"b_guardar_encuesta")
        sizePolicy.setHeightForWidth(self.b_guardar_encuesta.sizePolicy().hasHeightForWidth())
        self.b_guardar_encuesta.setSizePolicy(sizePolicy)
        self.b_guardar_encuesta.setMinimumSize(QSize(45, 0))
        self.b_guardar_encuesta.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(40, 40, 40, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px soild;\n"
"	/*border-bottom-left-radius: 10px;\n"
" 	border-top-left-radius: 10px;*/\n"
" 	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(55, 55, 145, 0.7);\n"
"}")
        self.b_guardar_encuesta.setIcon(icon16)

        self.horizontalLayout_18.addWidget(self.b_guardar_encuesta)


        self.verticalLayout_7.addWidget(self.f_edit_barr)

        self.f_edit_up = QFrame(self.e_pag_1)
        self.f_edit_up.setObjectName(u"f_edit_up")
        self.f_edit_up.setMinimumSize(QSize(0, 60))
        self.f_edit_up.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 1);")
        self.f_edit_up.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_edit_up.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.f_edit_up)
        self.horizontalLayout_19.setSpacing(15)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.b_categoria_1 = QPushButton(self.f_edit_up)
        self.b_categoria_1.setObjectName(u"b_categoria_1")
        sizePolicy.setHeightForWidth(self.b_categoria_1.sizePolicy().hasHeightForWidth())
        self.b_categoria_1.setSizePolicy(sizePolicy)
        font10 = QFont()
        font10.setFamilies([u"Bahnschrift SemiLight Condensed"])
        font10.setPointSize(14)
        self.b_categoria_1.setFont(font10)
        self.b_categoria_1.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgba(40, 85, 165, 0.7);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"")
        self.b_categoria_1.setCheckable(True)
        self.b_categoria_1.setChecked(True)
        self.b_categoria_1.setAutoExclusive(True)

        self.horizontalLayout_19.addWidget(self.b_categoria_1)

        self.b_categoria_2 = QPushButton(self.f_edit_up)
        self.b_categoria_2.setObjectName(u"b_categoria_2")
        sizePolicy.setHeightForWidth(self.b_categoria_2.sizePolicy().hasHeightForWidth())
        self.b_categoria_2.setSizePolicy(sizePolicy)
        self.b_categoria_2.setFont(font10)
        self.b_categoria_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgba(40, 85, 165, 0.7);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"")
        self.b_categoria_2.setCheckable(True)
        self.b_categoria_2.setAutoExclusive(True)

        self.horizontalLayout_19.addWidget(self.b_categoria_2)

        self.b_categoria_3 = QPushButton(self.f_edit_up)
        self.b_categoria_3.setObjectName(u"b_categoria_3")
        sizePolicy.setHeightForWidth(self.b_categoria_3.sizePolicy().hasHeightForWidth())
        self.b_categoria_3.setSizePolicy(sizePolicy)
        self.b_categoria_3.setFont(font10)
        self.b_categoria_3.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgba(40, 85, 165, 0.7);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"")
        self.b_categoria_3.setCheckable(True)
        self.b_categoria_3.setAutoExclusive(True)

        self.horizontalLayout_19.addWidget(self.b_categoria_3)

        self.b_categoria_4 = QPushButton(self.f_edit_up)
        self.b_categoria_4.setObjectName(u"b_categoria_4")
        sizePolicy.setHeightForWidth(self.b_categoria_4.sizePolicy().hasHeightForWidth())
        self.b_categoria_4.setSizePolicy(sizePolicy)
        font11 = QFont()
        font11.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font11.setPointSize(14)
        font11.setBold(True)
        self.b_categoria_4.setFont(font11)
        self.b_categoria_4.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgba(40, 85, 165, 0.4);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgba(40, 85, 165, 0.7);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"")
        self.b_categoria_4.setCheckable(True)
        self.b_categoria_4.setAutoExclusive(True)

        self.horizontalLayout_19.addWidget(self.b_categoria_4)


        self.verticalLayout_7.addWidget(self.f_edit_up)

        self.f_edit_dawn = QFrame(self.e_pag_1)
        self.f_edit_dawn.setObjectName(u"f_edit_dawn")
        self.f_edit_dawn.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);\n"
"border-radius: 10px;\n"
"\n"
"color: rgba(255, 255, 255, 1);")
        self.f_edit_dawn.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_edit_dawn.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.f_edit_dawn)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 10, 10, -1)
        self.stackedWidget_3 = QStackedWidget(self.f_edit_dawn)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.pregunta_pag1 = QWidget()
        self.pregunta_pag1.setObjectName(u"pregunta_pag1")
        self.pregunta_pag1.setStyleSheet(u"background: rgba(70, 70, 70,0);")
        self.horizontalLayout_20 = QHBoxLayout(self.pregunta_pag1)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.f_cat_1 = QFrame(self.pregunta_pag1)
        self.f_cat_1.setObjectName(u"f_cat_1")
        self.f_cat_1.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.f_cat_1.setFrameShape(QFrame.Shape.NoFrame)
        self.f_cat_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.f_cat_1)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.f_pregunta_1 = QFrame(self.f_cat_1)
        self.f_pregunta_1.setObjectName(u"f_pregunta_1")
        self.f_pregunta_1.setMinimumSize(QSize(0, 90))
        self.f_pregunta_1.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_1.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.f_pregunta_1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.l_pregunta_1 = QLabel(self.f_pregunta_1)
        self.l_pregunta_1.setObjectName(u"l_pregunta_1")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.l_pregunta_1.sizePolicy().hasHeightForWidth())
        self.l_pregunta_1.setSizePolicy(sizePolicy7)
        self.l_pregunta_1.setMinimumSize(QSize(0, 30))
        self.l_pregunta_1.setFont(font10)
        self.l_pregunta_1.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.l_pregunta_1)

        self.lineedit_preg_1 = QLineEdit(self.f_pregunta_1)
        self.lineedit_preg_1.setObjectName(u"lineedit_preg_1")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_1.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_1.setSizePolicy(sizePolicy3)
        self.lineedit_preg_1.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_1.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_1.setFont(font7)
        self.lineedit_preg_1.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.lineedit_preg_1)


        self.verticalLayout_8.addWidget(self.f_pregunta_1)

        self.f_pregunta_2 = QFrame(self.f_cat_1)
        self.f_pregunta_2.setObjectName(u"f_pregunta_2")
        self.f_pregunta_2.setMinimumSize(QSize(0, 90))
        self.f_pregunta_2.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_2.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.f_pregunta_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.l_pregunta_2 = QLabel(self.f_pregunta_2)
        self.l_pregunta_2.setObjectName(u"l_pregunta_2")
        sizePolicy7.setHeightForWidth(self.l_pregunta_2.sizePolicy().hasHeightForWidth())
        self.l_pregunta_2.setSizePolicy(sizePolicy7)
        self.l_pregunta_2.setMinimumSize(QSize(0, 30))
        self.l_pregunta_2.setFont(font10)
        self.l_pregunta_2.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.l_pregunta_2)

        self.lineedit_preg_2 = QLineEdit(self.f_pregunta_2)
        self.lineedit_preg_2.setObjectName(u"lineedit_preg_2")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_2.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_2.setSizePolicy(sizePolicy3)
        self.lineedit_preg_2.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_2.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_2.setFont(font7)
        self.lineedit_preg_2.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.lineedit_preg_2)


        self.verticalLayout_8.addWidget(self.f_pregunta_2)

        self.f_pregunta_3 = QFrame(self.f_cat_1)
        self.f_pregunta_3.setObjectName(u"f_pregunta_3")
        self.f_pregunta_3.setMinimumSize(QSize(0, 90))
        self.f_pregunta_3.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_3.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.f_pregunta_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.l_pregunta_3 = QLabel(self.f_pregunta_3)
        self.l_pregunta_3.setObjectName(u"l_pregunta_3")
        sizePolicy7.setHeightForWidth(self.l_pregunta_3.sizePolicy().hasHeightForWidth())
        self.l_pregunta_3.setSizePolicy(sizePolicy7)
        self.l_pregunta_3.setMinimumSize(QSize(0, 30))
        self.l_pregunta_3.setFont(font10)
        self.l_pregunta_3.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.l_pregunta_3)

        self.lineedit_preg_3 = QLineEdit(self.f_pregunta_3)
        self.lineedit_preg_3.setObjectName(u"lineedit_preg_3")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_3.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_3.setSizePolicy(sizePolicy3)
        self.lineedit_preg_3.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_3.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_3.setFont(font7)
        self.lineedit_preg_3.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.lineedit_preg_3)


        self.verticalLayout_8.addWidget(self.f_pregunta_3)

        self.f_pregunta_4 = QFrame(self.f_cat_1)
        self.f_pregunta_4.setObjectName(u"f_pregunta_4")
        self.f_pregunta_4.setMinimumSize(QSize(0, 90))
        self.f_pregunta_4.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_4.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.f_pregunta_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.l_pregunta_4 = QLabel(self.f_pregunta_4)
        self.l_pregunta_4.setObjectName(u"l_pregunta_4")
        sizePolicy7.setHeightForWidth(self.l_pregunta_4.sizePolicy().hasHeightForWidth())
        self.l_pregunta_4.setSizePolicy(sizePolicy7)
        self.l_pregunta_4.setMinimumSize(QSize(0, 30))
        self.l_pregunta_4.setFont(font10)
        self.l_pregunta_4.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.l_pregunta_4)

        self.lineedit_preg_4 = QLineEdit(self.f_pregunta_4)
        self.lineedit_preg_4.setObjectName(u"lineedit_preg_4")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_4.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_4.setSizePolicy(sizePolicy3)
        self.lineedit_preg_4.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_4.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_4.setFont(font7)
        self.lineedit_preg_4.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.lineedit_preg_4)


        self.verticalLayout_8.addWidget(self.f_pregunta_4)


        self.horizontalLayout_20.addWidget(self.f_cat_1)

        self.stackedWidget_3.addWidget(self.pregunta_pag1)
        self.pregunta_pag2 = QWidget()
        self.pregunta_pag2.setObjectName(u"pregunta_pag2")
        self.verticalLayout_14 = QVBoxLayout(self.pregunta_pag2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.f_cat_2 = QFrame(self.pregunta_pag2)
        self.f_cat_2.setObjectName(u"f_cat_2")
        self.f_cat_2.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.f_cat_2.setFrameShape(QFrame.Shape.NoFrame)
        self.f_cat_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.f_cat_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.f_pregunta_5 = QFrame(self.f_cat_2)
        self.f_pregunta_5.setObjectName(u"f_pregunta_5")
        self.f_pregunta_5.setMinimumSize(QSize(0, 90))
        self.f_pregunta_5.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_5.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.f_pregunta_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.l_pregunta_5 = QLabel(self.f_pregunta_5)
        self.l_pregunta_5.setObjectName(u"l_pregunta_5")
        sizePolicy7.setHeightForWidth(self.l_pregunta_5.sizePolicy().hasHeightForWidth())
        self.l_pregunta_5.setSizePolicy(sizePolicy7)
        self.l_pregunta_5.setMinimumSize(QSize(0, 30))
        self.l_pregunta_5.setFont(font10)
        self.l_pregunta_5.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.l_pregunta_5)

        self.lineedit_preg_5 = QLineEdit(self.f_pregunta_5)
        self.lineedit_preg_5.setObjectName(u"lineedit_preg_5")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_5.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_5.setSizePolicy(sizePolicy3)
        self.lineedit_preg_5.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_5.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_5.setFont(font7)
        self.lineedit_preg_5.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.lineedit_preg_5)


        self.verticalLayout_12.addWidget(self.f_pregunta_5)

        self.f_pregunta_6 = QFrame(self.f_cat_2)
        self.f_pregunta_6.setObjectName(u"f_pregunta_6")
        self.f_pregunta_6.setMinimumSize(QSize(0, 90))
        self.f_pregunta_6.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_6.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.f_pregunta_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.l_pregunta_6 = QLabel(self.f_pregunta_6)
        self.l_pregunta_6.setObjectName(u"l_pregunta_6")
        sizePolicy7.setHeightForWidth(self.l_pregunta_6.sizePolicy().hasHeightForWidth())
        self.l_pregunta_6.setSizePolicy(sizePolicy7)
        self.l_pregunta_6.setMinimumSize(QSize(0, 30))
        self.l_pregunta_6.setFont(font10)
        self.l_pregunta_6.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.l_pregunta_6)

        self.lineedit_preg_6 = QLineEdit(self.f_pregunta_6)
        self.lineedit_preg_6.setObjectName(u"lineedit_preg_6")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_6.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_6.setSizePolicy(sizePolicy3)
        self.lineedit_preg_6.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_6.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_6.setFont(font7)
        self.lineedit_preg_6.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.lineedit_preg_6)


        self.verticalLayout_12.addWidget(self.f_pregunta_6)

        self.f_pregunta_7 = QFrame(self.f_cat_2)
        self.f_pregunta_7.setObjectName(u"f_pregunta_7")
        self.f_pregunta_7.setMinimumSize(QSize(0, 90))
        self.f_pregunta_7.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_7.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.f_pregunta_7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.l_pregunta_7 = QLabel(self.f_pregunta_7)
        self.l_pregunta_7.setObjectName(u"l_pregunta_7")
        sizePolicy7.setHeightForWidth(self.l_pregunta_7.sizePolicy().hasHeightForWidth())
        self.l_pregunta_7.setSizePolicy(sizePolicy7)
        self.l_pregunta_7.setMinimumSize(QSize(0, 30))
        self.l_pregunta_7.setFont(font10)
        self.l_pregunta_7.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.l_pregunta_7)

        self.lineedit_preg_7 = QLineEdit(self.f_pregunta_7)
        self.lineedit_preg_7.setObjectName(u"lineedit_preg_7")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_7.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_7.setSizePolicy(sizePolicy3)
        self.lineedit_preg_7.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_7.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_7.setFont(font7)
        self.lineedit_preg_7.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.lineedit_preg_7)


        self.verticalLayout_12.addWidget(self.f_pregunta_7)

        self.f_pregunta_8 = QFrame(self.f_cat_2)
        self.f_pregunta_8.setObjectName(u"f_pregunta_8")
        self.f_pregunta_8.setMinimumSize(QSize(0, 90))
        self.f_pregunta_8.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_8.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.f_pregunta_8)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.l_pregunta_8 = QLabel(self.f_pregunta_8)
        self.l_pregunta_8.setObjectName(u"l_pregunta_8")
        sizePolicy7.setHeightForWidth(self.l_pregunta_8.sizePolicy().hasHeightForWidth())
        self.l_pregunta_8.setSizePolicy(sizePolicy7)
        self.l_pregunta_8.setMinimumSize(QSize(0, 30))
        self.l_pregunta_8.setFont(font10)
        self.l_pregunta_8.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.l_pregunta_8)

        self.lineedit_preg_8 = QLineEdit(self.f_pregunta_8)
        self.lineedit_preg_8.setObjectName(u"lineedit_preg_8")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_8.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_8.setSizePolicy(sizePolicy3)
        self.lineedit_preg_8.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_8.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_8.setFont(font7)
        self.lineedit_preg_8.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.lineedit_preg_8)


        self.verticalLayout_12.addWidget(self.f_pregunta_8)


        self.verticalLayout_14.addWidget(self.f_cat_2)

        self.stackedWidget_3.addWidget(self.pregunta_pag2)
        self.pregunta_pag4 = QWidget()
        self.pregunta_pag4.setObjectName(u"pregunta_pag4")
        self.verticalLayout_33 = QVBoxLayout(self.pregunta_pag4)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.f_cat_4 = QFrame(self.pregunta_pag4)
        self.f_cat_4.setObjectName(u"f_cat_4")
        self.f_cat_4.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.f_cat_4.setFrameShape(QFrame.Shape.NoFrame)
        self.f_cat_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.f_cat_4)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(10, 10, 10, 10)
        self.f_pregunta_13 = QFrame(self.f_cat_4)
        self.f_pregunta_13.setObjectName(u"f_pregunta_13")
        self.f_pregunta_13.setMinimumSize(QSize(0, 90))
        self.f_pregunta_13.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_13.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.f_pregunta_13)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.l_pregunta_13 = QLabel(self.f_pregunta_13)
        self.l_pregunta_13.setObjectName(u"l_pregunta_13")
        sizePolicy7.setHeightForWidth(self.l_pregunta_13.sizePolicy().hasHeightForWidth())
        self.l_pregunta_13.setSizePolicy(sizePolicy7)
        self.l_pregunta_13.setMinimumSize(QSize(0, 30))
        self.l_pregunta_13.setFont(font10)
        self.l_pregunta_13.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.l_pregunta_13)

        self.lineedit_preg_13 = QLineEdit(self.f_pregunta_13)
        self.lineedit_preg_13.setObjectName(u"lineedit_preg_13")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_13.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_13.setSizePolicy(sizePolicy3)
        self.lineedit_preg_13.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_13.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_13.setFont(font7)
        self.lineedit_preg_13.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.lineedit_preg_13)


        self.verticalLayout_28.addWidget(self.f_pregunta_13)

        self.f_pregunta_14 = QFrame(self.f_cat_4)
        self.f_pregunta_14.setObjectName(u"f_pregunta_14")
        self.f_pregunta_14.setMinimumSize(QSize(0, 90))
        self.f_pregunta_14.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_14.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.f_pregunta_14)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.l_pregunta_14 = QLabel(self.f_pregunta_14)
        self.l_pregunta_14.setObjectName(u"l_pregunta_14")
        sizePolicy7.setHeightForWidth(self.l_pregunta_14.sizePolicy().hasHeightForWidth())
        self.l_pregunta_14.setSizePolicy(sizePolicy7)
        self.l_pregunta_14.setMinimumSize(QSize(0, 30))
        self.l_pregunta_14.setFont(font10)
        self.l_pregunta_14.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.l_pregunta_14)

        self.lineedit_preg_14 = QLineEdit(self.f_pregunta_14)
        self.lineedit_preg_14.setObjectName(u"lineedit_preg_14")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_14.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_14.setSizePolicy(sizePolicy3)
        self.lineedit_preg_14.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_14.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_14.setFont(font7)
        self.lineedit_preg_14.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.lineedit_preg_14)


        self.verticalLayout_28.addWidget(self.f_pregunta_14)

        self.f_pregunta_15 = QFrame(self.f_cat_4)
        self.f_pregunta_15.setObjectName(u"f_pregunta_15")
        self.f_pregunta_15.setMinimumSize(QSize(0, 90))
        self.f_pregunta_15.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_15.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.f_pregunta_15)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.l_pregunta_15 = QLabel(self.f_pregunta_15)
        self.l_pregunta_15.setObjectName(u"l_pregunta_15")
        sizePolicy7.setHeightForWidth(self.l_pregunta_15.sizePolicy().hasHeightForWidth())
        self.l_pregunta_15.setSizePolicy(sizePolicy7)
        self.l_pregunta_15.setMinimumSize(QSize(0, 30))
        self.l_pregunta_15.setFont(font10)
        self.l_pregunta_15.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.l_pregunta_15)

        self.lineedit_preg_15 = QLineEdit(self.f_pregunta_15)
        self.lineedit_preg_15.setObjectName(u"lineedit_preg_15")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_15.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_15.setSizePolicy(sizePolicy3)
        self.lineedit_preg_15.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_15.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_15.setFont(font7)
        self.lineedit_preg_15.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.lineedit_preg_15)


        self.verticalLayout_28.addWidget(self.f_pregunta_15)

        self.f_pregunta_16 = QFrame(self.f_cat_4)
        self.f_pregunta_16.setObjectName(u"f_pregunta_16")
        self.f_pregunta_16.setMinimumSize(QSize(0, 90))
        self.f_pregunta_16.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_16.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.f_pregunta_16)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.l_pregunta_16 = QLabel(self.f_pregunta_16)
        self.l_pregunta_16.setObjectName(u"l_pregunta_16")
        sizePolicy7.setHeightForWidth(self.l_pregunta_16.sizePolicy().hasHeightForWidth())
        self.l_pregunta_16.setSizePolicy(sizePolicy7)
        self.l_pregunta_16.setMinimumSize(QSize(0, 30))
        self.l_pregunta_16.setFont(font10)
        self.l_pregunta_16.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.l_pregunta_16)

        self.lineedit_preg_16 = QLineEdit(self.f_pregunta_16)
        self.lineedit_preg_16.setObjectName(u"lineedit_preg_16")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_16.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_16.setSizePolicy(sizePolicy3)
        self.lineedit_preg_16.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_16.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_16.setFont(font7)
        self.lineedit_preg_16.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.lineedit_preg_16)


        self.verticalLayout_28.addWidget(self.f_pregunta_16)


        self.verticalLayout_33.addWidget(self.f_cat_4)

        self.stackedWidget_3.addWidget(self.pregunta_pag4)
        self.pregunta_pag3 = QWidget()
        self.pregunta_pag3.setObjectName(u"pregunta_pag3")
        self.verticalLayout_27 = QVBoxLayout(self.pregunta_pag3)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.f_cat_3 = QFrame(self.pregunta_pag3)
        self.f_cat_3.setObjectName(u"f_cat_3")
        self.f_cat_3.setStyleSheet(u"background: rgba(70, 70, 70, 0);")
        self.f_cat_3.setFrameShape(QFrame.Shape.NoFrame)
        self.f_cat_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.f_cat_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(10, 10, 10, 10)
        self.f_pregunta_9 = QFrame(self.f_cat_3)
        self.f_pregunta_9.setObjectName(u"f_pregunta_9")
        self.f_pregunta_9.setMinimumSize(QSize(0, 90))
        self.f_pregunta_9.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_9.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.f_pregunta_9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.l_pregunta_9 = QLabel(self.f_pregunta_9)
        self.l_pregunta_9.setObjectName(u"l_pregunta_9")
        sizePolicy7.setHeightForWidth(self.l_pregunta_9.sizePolicy().hasHeightForWidth())
        self.l_pregunta_9.setSizePolicy(sizePolicy7)
        self.l_pregunta_9.setMinimumSize(QSize(0, 30))
        self.l_pregunta_9.setFont(font10)
        self.l_pregunta_9.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.l_pregunta_9)

        self.lineedit_preg_9 = QLineEdit(self.f_pregunta_9)
        self.lineedit_preg_9.setObjectName(u"lineedit_preg_9")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_9.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_9.setSizePolicy(sizePolicy3)
        self.lineedit_preg_9.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_9.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_9.setFont(font7)
        self.lineedit_preg_9.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.lineedit_preg_9)


        self.verticalLayout_22.addWidget(self.f_pregunta_9)

        self.f_pregunta_10 = QFrame(self.f_cat_3)
        self.f_pregunta_10.setObjectName(u"f_pregunta_10")
        self.f_pregunta_10.setMinimumSize(QSize(0, 90))
        self.f_pregunta_10.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_10.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.f_pregunta_10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.l_pregunta_10 = QLabel(self.f_pregunta_10)
        self.l_pregunta_10.setObjectName(u"l_pregunta_10")
        sizePolicy7.setHeightForWidth(self.l_pregunta_10.sizePolicy().hasHeightForWidth())
        self.l_pregunta_10.setSizePolicy(sizePolicy7)
        self.l_pregunta_10.setMinimumSize(QSize(0, 30))
        self.l_pregunta_10.setFont(font10)
        self.l_pregunta_10.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.l_pregunta_10)

        self.lineedit_preg_10 = QLineEdit(self.f_pregunta_10)
        self.lineedit_preg_10.setObjectName(u"lineedit_preg_10")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_10.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_10.setSizePolicy(sizePolicy3)
        self.lineedit_preg_10.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_10.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_10.setFont(font7)
        self.lineedit_preg_10.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.lineedit_preg_10)


        self.verticalLayout_22.addWidget(self.f_pregunta_10)

        self.f_pregunta_11 = QFrame(self.f_cat_3)
        self.f_pregunta_11.setObjectName(u"f_pregunta_11")
        self.f_pregunta_11.setMinimumSize(QSize(0, 90))
        self.f_pregunta_11.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_11.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.f_pregunta_11)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.l_pregunta_11 = QLabel(self.f_pregunta_11)
        self.l_pregunta_11.setObjectName(u"l_pregunta_11")
        sizePolicy7.setHeightForWidth(self.l_pregunta_11.sizePolicy().hasHeightForWidth())
        self.l_pregunta_11.setSizePolicy(sizePolicy7)
        self.l_pregunta_11.setMinimumSize(QSize(0, 30))
        self.l_pregunta_11.setFont(font10)
        self.l_pregunta_11.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.l_pregunta_11)

        self.lineedit_preg_11 = QLineEdit(self.f_pregunta_11)
        self.lineedit_preg_11.setObjectName(u"lineedit_preg_11")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_11.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_11.setSizePolicy(sizePolicy3)
        self.lineedit_preg_11.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_11.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_11.setFont(font7)
        self.lineedit_preg_11.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.lineedit_preg_11)


        self.verticalLayout_22.addWidget(self.f_pregunta_11)

        self.f_pregunta_12 = QFrame(self.f_cat_3)
        self.f_pregunta_12.setObjectName(u"f_pregunta_12")
        self.f_pregunta_12.setMinimumSize(QSize(0, 90))
        self.f_pregunta_12.setStyleSheet(u"background: rgba(50, 50, 50, 0.4);")
        self.f_pregunta_12.setFrameShape(QFrame.Shape.NoFrame)
        self.f_pregunta_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.f_pregunta_12)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.l_pregunta_12 = QLabel(self.f_pregunta_12)
        self.l_pregunta_12.setObjectName(u"l_pregunta_12")
        sizePolicy7.setHeightForWidth(self.l_pregunta_12.sizePolicy().hasHeightForWidth())
        self.l_pregunta_12.setSizePolicy(sizePolicy7)
        self.l_pregunta_12.setMinimumSize(QSize(0, 30))
        self.l_pregunta_12.setFont(font10)
        self.l_pregunta_12.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.l_pregunta_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.l_pregunta_12)

        self.lineedit_preg_12 = QLineEdit(self.f_pregunta_12)
        self.lineedit_preg_12.setObjectName(u"lineedit_preg_12")
        sizePolicy3.setHeightForWidth(self.lineedit_preg_12.sizePolicy().hasHeightForWidth())
        self.lineedit_preg_12.setSizePolicy(sizePolicy3)
        self.lineedit_preg_12.setMinimumSize(QSize(600, 30))
        self.lineedit_preg_12.setMaximumSize(QSize(16777215, 40))
        self.lineedit_preg_12.setFont(font7)
        self.lineedit_preg_12.setStyleSheet(u"background: rgba(70, 70, 70, 0.4);")
        self.lineedit_preg_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.lineedit_preg_12)


        self.verticalLayout_22.addWidget(self.f_pregunta_12)


        self.verticalLayout_27.addWidget(self.f_cat_3)

        self.stackedWidget_3.addWidget(self.pregunta_pag3)

        self.horizontalLayout_14.addWidget(self.stackedWidget_3)


        self.verticalLayout_7.addWidget(self.f_edit_dawn)

        self.stackedWidget_2.addWidget(self.e_pag_1)

        self.horizontalLayout_12.addWidget(self.stackedWidget_2)


        self.horizontalLayout_8.addWidget(self.f_pag1_encuesta)

        self.stackedWidget.addWidget(self.pag_5)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.f_ventanas)


        self.verticalLayout.addWidget(self.f_cuerpo_dawn)

        MainWindow.setCentralWidget(self.w_central)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(-1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_logo.setText("")
        self.b_perfil.setText("")
        self.b_encuesta.setText("")
        self.b_stats.setText("")
        self.b_config.setText("")
        self.label.setText("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.label_correo.setText(QCoreApplication.translate("MainWindow", u"Correo :", None))
        self.label_padsword.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a :", None))
        self.label_escuela.setText(QCoreApplication.translate("MainWindow", u"Escuela :", None))
        self.label_direccion.setText(QCoreApplication.translate("MainWindow", u"Direccion :", None))
        self.lineedit_password.setText(QCoreApplication.translate("MainWindow", u"1234", None))
        self.label_telefono.setText(QCoreApplication.translate("MainWindow", u"Telefono :", None))
        self.label_img.setText("")
        self.label_nick.setText(QCoreApplication.translate("MainWindow", u"NICK", None))
        self.label_apellido.setText(QCoreApplication.translate("MainWindow", u"NOMBRE ", None))
        self.label_nombre.setText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.b_cerrar_secion.setText(QCoreApplication.translate("MainWindow", u"Cerrar secion", None))
        self.b_ver_password.setText("")
        self.b_cambiar_pasworld.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_4.setText("")
        self.b_edit_encuesta.setText(QCoreApplication.translate("MainWindow", u"Editar\n"
"Encuestas", None))
        self.b_enviar_encuesta.setText(QCoreApplication.translate("MainWindow", u"Enviar\n"
"Encuestas", None))
        self.b_editar_profes.setText(QCoreApplication.translate("MainWindow", u"Agregar\n"
"Profesores", None))
        self.b_editar_estudiantes.setText(QCoreApplication.translate("MainWindow", u"Agregar\n"
"Estudiantes", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Agragar Profesores", None))
        self.b_atras_agegar_profe.setText("")
        self.b_cancelar_agegar_profe.setText("")
        self.b_guardar_agegar_profe.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Agragar Estudiantes", None))
        self.b_atras_agegar_estud.setText("")
        self.b_cancelar_agegar_estud.setText("")
        self.b_guardar_agegar_estud.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Edicion de Encuestas ...", None))
        self.b_atras_encuesta.setText("")
        self.b_cancelar_encuesta.setText("")
        self.b_guardar_encuesta.setText("")
        self.b_categoria_1.setText(QCoreApplication.translate("MainWindow", u"cat 1", None))
        self.b_categoria_2.setText(QCoreApplication.translate("MainWindow", u"cat2", None))
        self.b_categoria_3.setText(QCoreApplication.translate("MainWindow", u"cat 3", None))
        self.b_categoria_4.setText(QCoreApplication.translate("MainWindow", u"cat 4", None))
        self.l_pregunta_1.setText(QCoreApplication.translate("MainWindow", u"Pregunta 1  ?", None))
        self.lineedit_preg_1.setText("")
        self.l_pregunta_2.setText(QCoreApplication.translate("MainWindow", u"Pregunta 2  ?", None))
        self.lineedit_preg_2.setText("")
        self.l_pregunta_3.setText(QCoreApplication.translate("MainWindow", u"Pregunta 3  ?", None))
        self.lineedit_preg_3.setText("")
        self.l_pregunta_4.setText(QCoreApplication.translate("MainWindow", u"Pregunta 4  ?", None))
        self.lineedit_preg_4.setText("")
        self.l_pregunta_5.setText(QCoreApplication.translate("MainWindow", u"Pregunta 1  ?", None))
        self.lineedit_preg_5.setText("")
        self.l_pregunta_6.setText(QCoreApplication.translate("MainWindow", u"Pregunta 2  ?", None))
        self.lineedit_preg_6.setText("")
        self.l_pregunta_7.setText(QCoreApplication.translate("MainWindow", u"Pregunta 3  ?", None))
        self.lineedit_preg_7.setText("")
        self.l_pregunta_8.setText(QCoreApplication.translate("MainWindow", u"Pregunta 4  ?", None))
        self.lineedit_preg_8.setText("")
        self.l_pregunta_13.setText(QCoreApplication.translate("MainWindow", u"Pregunta 1  ?", None))
        self.lineedit_preg_13.setText("")
        self.l_pregunta_14.setText(QCoreApplication.translate("MainWindow", u"Pregunta 2  ?", None))
        self.lineedit_preg_14.setText("")
        self.l_pregunta_15.setText(QCoreApplication.translate("MainWindow", u"Pregunta 3  ?", None))
        self.lineedit_preg_15.setText("")
        self.l_pregunta_16.setText(QCoreApplication.translate("MainWindow", u"Pregunta 4  ?", None))
        self.lineedit_preg_16.setText("")
        self.l_pregunta_9.setText(QCoreApplication.translate("MainWindow", u"Pregunta 1  ?", None))
        self.lineedit_preg_9.setText("")
        self.l_pregunta_10.setText(QCoreApplication.translate("MainWindow", u"Pregunta 2  ?", None))
        self.lineedit_preg_10.setText("")
        self.l_pregunta_11.setText(QCoreApplication.translate("MainWindow", u"Pregunta 3  ?", None))
        self.lineedit_preg_11.setText("")
        self.l_pregunta_12.setText(QCoreApplication.translate("MainWindow", u"Pregunta 4  ?", None))
        self.lineedit_preg_12.setText("")
    # retranslateUi

