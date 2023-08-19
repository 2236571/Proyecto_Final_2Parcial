#Nombres de integrantes
#Vivíana Caice Zuñiga
#Joseph Paez Cobos
#Jamilet Pillasagua Plaza
#Alejandra Barrera Guaranda
from datetime import datetime, date

from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from UI.vtn_principal import Ui_vtn_principal
from datos.estudiante_dao import EstudianteDao
from dominio.docente import Docente
from dominio.estudiante import Estudiante


class PersonaPrincipal(QMainWindow):
    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.stb_estado.showMessage('BIENVENIDOS',2000)
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.btn_buscar_cedula.clicked.connect(self.buscar_x_cedula)
        self.ui.btn_estatura.clicked.connect(self.calculos_estatura)
        self.ui.btn_peso.clicked.connect(self.calculos_peso)
        self.ui.btn_fecha_nacimiento.clicked.connect(self.calculos_fecha_nacimiento)
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())


        correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9. -]+\[A-Z|a-z]{2,7}b'
        validator = QRegularExpressionValidator(correo_exp, self)
        self.ui.txt_email.setValidator(validator)

    def grabar(self):
            tipo_persona = self.ui.cb_tipo_persona.currentText()
            if self.ui.txt_nombre.text() == " " or self.ui.txt_apellido.text() == ' ' \
                    or len(self.ui.txt_cedula.text())<10 or self.ui.txt_email.text() == ' ':
                print('Completar datos')
                QMessageBox.warning(self, 'Advertencia', 'Falta de llenar los datos obligatorios')
            else:
                persona = None
            if tipo_persona == 'Docente':
               persona = Docente()
               persona.nombre = self.ui.txt_nombre.text()
               persona.apellido = self.ui.txt_apellido.text()
               persona.cedula = self.ui.txt_cedula.text()
               persona.email = self.ui.txt_email.text()
               persona.carrera = self.ui.txt_carrera.text()
               persona.estatura = self.ui.sp_estatura.text()
               persona.peso = self.ui.sp_peso.text()
               persona.fecha_nacimiento = self.ui.txt_fecha_nacimiento.date().getDate()
            else:
               persona = Estudiante()
               persona.nombre = self.ui.txt_nombre.text()
               persona.apellido = self.ui.txt_apellido.text()
               persona.cedula = self.ui.txt_cedula.text()
               persona.email = self.ui.txt_email.text()
               persona.carrera = self.ui.txt_carrera.text()
               persona.estatura = self.ui.sp_estatura.text()
               persona.peso = self.ui.sp_peso.text()
               persona.fecha_nacimiento = self.ui.txt_fecha_nacimiento.text()
               #insertar a la base de datos al estudiante
               respuesta = None
               respuesta = EstudianteDao.insertar_estudiante(persona)

            #archivo = None
            #try:
                #archivo = open("archivo.txt", mode="a")
                #archivo.write(persona.__str__())
                #archivo.write("\n")
            #except Exception as e:
                 #print("No se pudo grabar")
            #finally:
                #if archivo:
                   #archivo.close()
            if respuesta['exito']:
                self.ui.txt_nombre.setText("")
                self.ui.txt_apellido.setText("")
                self.ui.txt_cedula.setText("")
                self.ui.txt_email.setText("")
                self.ui.txt_carrera.setText("")
                self.ui.sp_estatura.setValue(0)
                self.ui.sp_peso.setValue(0)
                self.ui.stb_estado.showMessage('GRABADO CON ÉXITO', 2000)
            else:
                QMessageBox.critical(self, 'Error', respuesta['mensaje'])
    def buscar_x_cedula(self):
       cedula = self.ui.txt_cedula.text()
       e = Estudiante(cedula=cedula)
       e = EstudianteDao.seleccionar_por_cedula(e)
       print(e)
       self.ui.txt_nombre.setText(e.nombre)
       self.ui.txt_apellido.setText(e.apellido)
       self.ui.txt_email.setText(e.email)
       self.ui.cb_tipo_persona.setCurrentText('Estudiante')
       self.ui.txt_carrera.setText(e.carrera)
       self.ui.sp_peso.setValue(e.peso)
       self.ui.sp_estatura.setValue(e.estatura)
       self.ui.txt_fecha_nacimiento.setDate(e.fecha_nacimiento)

    def calculos_estatura(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_estaturas = 0
        estaturas = []
        for estudiante in estudiantes:
            suma_estaturas += estudiante.estatura
            estaturas.append(estudiante.estatura)
        promedio_estatura = suma_estaturas/cantidad_estudiantes
        estatura_minima = min(estaturas)
        estatura_maxima = max(estaturas)
        estaturas.sort()
        mediana_estaturas = estaturas[cantidad_estudiantes // 2]
        print('****Calculos estadisticos de las estaturas****')
        print(f'El promedio de estatura es: {promedio_estatura}')
        print(f'La mediana de pesos es: {mediana_estaturas}')
        print(f'La estatura mínima es: {estatura_minima}')
        print(f'La estatura máxima es: {estatura_maxima}')

        # Cálculo de la moda
        estaturas_frecuencias = {}  # Diccionario para almacenar frecuencias de estaturas
        max_frecuencia = 0
        modas = []

        for estatura in estaturas:
            if estatura in estaturas_frecuencias:
                estaturas_frecuencias[estatura] += 1
            else:
                estaturas_frecuencias[estatura] = 1

            if estaturas_frecuencias[estatura] > max_frecuencia:
                max_frecuencia = estaturas_frecuencias[estatura]
                modas = [estatura]
            elif estaturas_frecuencias[estatura] == max_frecuencia and estatura not in modas:
                modas.append(estatura)

        print(f'La moda de las estaturas es: {modas}')



    def calculos_peso(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_pesos = 0
        pesos = []
        for estudiante in estudiantes:
            suma_pesos += estudiante.peso
            pesos.append(estudiante.peso)
        promedio_peso = suma_pesos/cantidad_estudiantes
        peso_minimo= min(pesos)
        peso_maximo = max(pesos)
        pesos.sort()
        mediana_pesos = pesos[cantidad_estudiantes // 2]
        print('****Calculos estadisticos de los pesos****')
        print(f'El promedio de pesos es: {promedio_peso}')
        print(f'La mediana de pesos es: {mediana_pesos}')
        print(f'El peso mínimo es: {peso_minimo}')
        print(f'El peso máximo es: {peso_maximo}')

        # Cálculo de la moda
        pesos_frecuencias = {}  # Diccionario para almacenar frecuencias de estaturas
        max_frecuencia = 0
        modas = []

        for peso in pesos:
            if peso in pesos_frecuencias:
                pesos_frecuencias[peso] += 1
            else:
                pesos_frecuencias[peso] = 1

            if pesos_frecuencias[peso] > max_frecuencia:
                max_frecuencia = pesos_frecuencias[peso]
                modas = [peso]
            elif pesos_frecuencias[peso] == max_frecuencia and peso not in modas:
                modas.append(peso)
        print(f'La moda de los pesos son: {modas}')

    def calculos_fecha_nacimiento(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()

        # Calcular edades y almacenarlas en una lista
        edades = []
        for estudiante in estudiantes:
            fecha_nacimiento = estudiante.fecha_nacimiento
            edad = (datetime.now().date() - fecha_nacimiento).days // 365
            edades.append(edad)

        # Cálculo de estadísticas
        cantidad_estudiantes = len(edades)
        promedio_edad = sum(edades) / cantidad_estudiantes
        edades.sort()
        mediana_edad = edades[cantidad_estudiantes // 2]

        edades_frecuencias = {}
        max_frecuencia = 0
        modas = []

        for edad in edades:
            if edad in edades_frecuencias:
                edades_frecuencias[edad] += 1
            else:
                edades_frecuencias[edad] = 1

            if edades_frecuencias[edad] > max_frecuencia:
                max_frecuencia = edades_frecuencias[edad]
                modas = [edad]
            elif edades_frecuencias[edad] == max_frecuencia and edad not in modas:
                modas.append(edad)

        edad_minima = min(edades)
        edad_maxima = max(edades)

        print('****Calculos estadisticos de las edades****')
        print(f'El promedio de edades es: {promedio_edad:.2f}')
        print(f'La mediana de edades es: {mediana_edad}')
        print(f'La moda de las edades es: {modas}')
        print(f'La edad mínima es: {edad_minima}')
        print(f'La edad máxima es: {edad_maxima}')