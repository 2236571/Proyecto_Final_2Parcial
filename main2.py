#Nombres de integrantes
#Vivíana Caice Zuñiga
#Joseph Paez Cobos
#Jamilet Pillasagua Plaza
#Alejandra Barrera Guaranda

import sys

from PySide6.QtWidgets import QApplication
from servicio.persona_principal import PersonaPrincipal

app = QApplication()
vtn_principal = PersonaPrincipal()
vtn_principal.show()
sys.exit(app.exec())
