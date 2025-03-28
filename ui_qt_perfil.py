# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_perfilOOXhEk.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_f_shear_profe(object):
    def setupUi(self, f_shear_profe):
        if not f_shear_profe.objectName():
            f_shear_profe.setObjectName(u"f_shear_profe")
        f_shear_profe.resize(534, 164)
        f_shear_profe.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(f_shear_profe)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.w_shear_profe = QWidget(f_shear_profe)
        self.w_shear_profe.setObjectName(u"w_shear_profe")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_shear_profe.sizePolicy().hasHeightForWidth())
        self.w_shear_profe.setSizePolicy(sizePolicy)
        self.w_shear_profe.setMinimumSize(QSize(400, 100))
        self.w_shear_profe.setMaximumSize(QSize(650, 100))
        self.w_shear_profe.setStyleSheet(u"QWidget{\n"
"	/*background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"	stop:0 rgb(55, 55, 55),\n"
"	stop: 0.3 rgb(105, 105, 105),\n"
"	stop: 0.7 rgb(105, 105, 105),\n"
"	stop:1 rgb(55, 55, 55));*/\n"
"	\n"
"	background: rgba(70, 70, 70, 0.4);\n"
"	border-radius: 10px;\n"
"	color: rgba(255, 255, 255, 1);\n"
"}")
        self.gridLayout = QGridLayout(self.w_shear_profe)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.s_nombre_profe = QLabel(self.w_shear_profe)
        self.s_nombre_profe.setObjectName(u"s_nombre_profe")
        self.s_nombre_profe.setMinimumSize(QSize(200, 35))
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiLight Condensed"])
        font.setPointSize(14)
        self.s_nombre_profe.setFont(font)
        self.s_nombre_profe.setTextFormat(Qt.TextFormat.AutoText)
        self.s_nombre_profe.setScaledContents(False)
        self.s_nombre_profe.setWordWrap(False)
        self.s_nombre_profe.setMargin(5)
        self.s_nombre_profe.setIndent(5)

        self.gridLayout.addWidget(self.s_nombre_profe, 0, 1, 1, 1)

        self.stats_profe = QPushButton(self.w_shear_profe)
        self.stats_profe.setObjectName(u"stats_profe")
        self.stats_profe.setMinimumSize(QSize(35, 70))
        self.stats_profe.setMaximumSize(QSize(40, 80))
        self.stats_profe.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u"App_Icon/page_info_40dp_FILL0_wght400_GRAD0_opsz40 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.stats_profe.setIcon(icon)
        self.stats_profe.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.stats_profe, 0, 2, 2, 1)

        self.s_escuela_profe = QLabel(self.w_shear_profe)
        self.s_escuela_profe.setObjectName(u"s_escuela_profe")
        self.s_escuela_profe.setMinimumSize(QSize(200, 35))
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT Condensed"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.s_escuela_profe.setFont(font1)
        self.s_escuela_profe.setMargin(5)
        self.s_escuela_profe.setIndent(5)

        self.gridLayout.addWidget(self.s_escuela_profe, 1, 1, 1, 1)

        self.img_profe = QLabel(self.w_shear_profe)
        self.img_profe.setObjectName(u"img_profe")
        self.img_profe.setMinimumSize(QSize(45, 70))
        self.img_profe.setMaximumSize(QSize(100, 100))
        self.img_profe.setPixmap(QPixmap(u"App_Icon/account_circle_40dp_FILL0_wght400_GRAD0_opsz40 (1) 70x70.png"))
        self.img_profe.setScaledContents(False)
        self.img_profe.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.img_profe.setMargin(-1)

        self.gridLayout.addWidget(self.img_profe, 0, 0, 2, 1)


        self.horizontalLayout.addWidget(self.w_shear_profe)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(f_shear_profe)

        QMetaObject.connectSlotsByName(f_shear_profe)
    # setupUi

    def retranslateUi(self, f_shear_profe):
        f_shear_profe.setWindowTitle(QCoreApplication.translate("f_shear_profe", u"Frame", None))
        self.s_nombre_profe.setText(QCoreApplication.translate("f_shear_profe", u"Nombre Apellido", None))
        self.stats_profe.setText("")
        self.s_escuela_profe.setText(QCoreApplication.translate("f_shear_profe", u"Escuela: Fases", None))
        self.img_profe.setText("")
    # retranslateUi

