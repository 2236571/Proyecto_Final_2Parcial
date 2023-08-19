# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(520, 468)
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_grabar = QPushButton(self.centralwidget)
        self.btn_grabar.setObjectName(u"btn_grabar")
        self.btn_grabar.setGeometry(QRect(190, 330, 101, 31))
        self.lbl_nombre = QLabel(self.centralwidget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(50, 70, 51, 16))
        self.lbl_apellido = QLabel(self.centralwidget)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(270, 70, 51, 16))
        self.txt_nombre = QLineEdit(self.centralwidget)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(120, 60, 111, 31))
        self.txt_nombre.setMaxLength(50)
        self.txt_apellido = QLineEdit(self.centralwidget)
        self.txt_apellido.setObjectName(u"txt_apellido")
        self.txt_apellido.setGeometry(QRect(330, 60, 111, 31))
        self.txt_apellido.setMaxLength(50)
        self.cb_tipo_persona = QComboBox(self.centralwidget)
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.setObjectName(u"cb_tipo_persona")
        self.cb_tipo_persona.setGeometry(QRect(120, 20, 111, 31))
        self.lbl_tipo_persona = QLabel(self.centralwidget)
        self.lbl_tipo_persona.setObjectName(u"lbl_tipo_persona")
        self.lbl_tipo_persona.setGeometry(QRect(50, 30, 51, 16))
        self.lbl_cedula = QLabel(self.centralwidget)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(50, 110, 51, 16))
        self.lbl_email = QLabel(self.centralwidget)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(60, 150, 51, 16))
        self.txt_cedula = QLineEdit(self.centralwidget)
        self.txt_cedula.setObjectName(u"txt_cedula")
        self.txt_cedula.setGeometry(QRect(120, 100, 111, 31))
        self.txt_cedula.setMaxLength(10)
        self.txt_email = QLineEdit(self.centralwidget)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(120, 140, 111, 31))
        self.txt_email.setMaxLength(100)
        self.btn_buscar_cedula = QPushButton(self.centralwidget)
        self.btn_buscar_cedula.setObjectName(u"btn_buscar_cedula")
        self.btn_buscar_cedula.setGeometry(QRect(240, 110, 121, 23))
        self.lbl_estatura = QLabel(self.centralwidget)
        self.lbl_estatura.setObjectName(u"lbl_estatura")
        self.lbl_estatura.setGeometry(QRect(100, 200, 71, 20))
        self.lbl_peso = QLabel(self.centralwidget)
        self.lbl_peso.setObjectName(u"lbl_peso")
        self.lbl_peso.setGeometry(QRect(110, 240, 51, 16))
        self.lbl_fecha_nacimiento = QLabel(self.centralwidget)
        self.lbl_fecha_nacimiento.setObjectName(u"lbl_fecha_nacimiento")
        self.lbl_fecha_nacimiento.setGeometry(QRect(20, 280, 91, 16))
        self.lbl_carrera = QLabel(self.centralwidget)
        self.lbl_carrera.setObjectName(u"lbl_carrera")
        self.lbl_carrera.setGeometry(QRect(270, 150, 51, 16))
        self.txt_carrera = QLineEdit(self.centralwidget)
        self.txt_carrera.setObjectName(u"txt_carrera")
        self.txt_carrera.setGeometry(QRect(330, 140, 111, 31))
        self.txt_carrera.setMaxLength(50)
        self.sp_estatura = QSpinBox(self.centralwidget)
        self.sp_estatura.setObjectName(u"sp_estatura")
        self.sp_estatura.setGeometry(QRect(190, 200, 42, 22))
        self.sp_estatura.setMaximum(300)
        self.sp_peso = QSpinBox(self.centralwidget)
        self.sp_peso.setObjectName(u"sp_peso")
        self.sp_peso.setGeometry(QRect(190, 240, 42, 22))
        self.sp_peso.setMaximum(255)
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(-250, 210, 110, 22))
        self.txt_fecha_nacimiento = QDateEdit(self.centralwidget)
        self.txt_fecha_nacimiento.setObjectName(u"txt_fecha_nacimiento")
        self.txt_fecha_nacimiento.setGeometry(QRect(120, 280, 110, 22))
        self.txt_fecha_nacimiento.setDateTime(QDateTime(QDate(2023, 8, 14), QTime(0, 0, 0)))
        self.txt_fecha_nacimiento.setMaximumDateTime(QDateTime(QDate(2023, 8, 20), QTime(23, 59, 59)))
        self.txt_fecha_nacimiento.setMinimumDateTime(QDateTime(QDate(1950, 9, 14), QTime(0, 0, 0)))
        self.btn_estatura = QPushButton(self.centralwidget)
        self.btn_estatura.setObjectName(u"btn_estatura")
        self.btn_estatura.setGeometry(QRect(260, 200, 121, 23))
        self.btn_peso = QPushButton(self.centralwidget)
        self.btn_peso.setObjectName(u"btn_peso")
        self.btn_peso.setGeometry(QRect(260, 240, 121, 23))
        self.btn_fecha_nacimiento = QPushButton(self.centralwidget)
        self.btn_fecha_nacimiento.setObjectName(u"btn_fecha_nacimiento")
        self.btn_fecha_nacimiento.setGeometry(QRect(260, 280, 121, 23))
        vtn_principal.setCentralWidget(self.centralwidget)
        self.mnb_menu_principal = QMenuBar(vtn_principal)
        self.mnb_menu_principal.setObjectName(u"mnb_menu_principal")
        self.mnb_menu_principal.setGeometry(QRect(0, 0, 520, 21))
        vtn_principal.setMenuBar(self.mnb_menu_principal)
        self.stb_estado = QStatusBar(vtn_principal)
        self.stb_estado.setObjectName(u"stb_estado")
        vtn_principal.setStatusBar(self.stb_estado)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"Ventana Principal ", None))
        self.btn_grabar.setText(QCoreApplication.translate("vtn_principal", u"Grabar", None))
        self.lbl_nombre.setText(QCoreApplication.translate("vtn_principal", u"Nombre:", None))
        self.lbl_apellido.setText(QCoreApplication.translate("vtn_principal", u"Apellido:", None))
        self.cb_tipo_persona.setItemText(0, QCoreApplication.translate("vtn_principal", u"Docente", None))
        self.cb_tipo_persona.setItemText(1, QCoreApplication.translate("vtn_principal", u"Estudiante", None))

        self.lbl_tipo_persona.setText(QCoreApplication.translate("vtn_principal", u"Tipo", None))
        self.lbl_cedula.setText(QCoreApplication.translate("vtn_principal", u"Cedula:", None))
        self.lbl_email.setText(QCoreApplication.translate("vtn_principal", u"Email:", None))
        self.btn_buscar_cedula.setText(QCoreApplication.translate("vtn_principal", u"Buscar por Cedula", None))
        self.lbl_estatura.setText(QCoreApplication.translate("vtn_principal", u"Estatura(cm):", None))
        self.lbl_peso.setText(QCoreApplication.translate("vtn_principal", u"Peso (Kg):", None))
        self.lbl_fecha_nacimiento.setText(QCoreApplication.translate("vtn_principal", u"Fecha_nacimiento:", None))
        self.lbl_carrera.setText(QCoreApplication.translate("vtn_principal", u"Carrera:", None))
        self.btn_estatura.setText(QCoreApplication.translate("vtn_principal", u"C.E estatura", None))
        self.btn_peso.setText(QCoreApplication.translate("vtn_principal", u"C.E peso", None))
        self.btn_fecha_nacimiento.setText(QCoreApplication.translate("vtn_principal", u"C.E fecha_nacimiento", None))
    # retranslateUi

