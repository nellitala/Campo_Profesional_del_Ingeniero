import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QRadioButton, QButtonGroup

METROS_A_PIES = 3.28084
METROS_A_PULGADAS = 39.3701
METROS_A_YARDAS = 1.09361

class ConvertirMetrosWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Convertir Metros")
        self.label_metros = QLabel("Ingrese la medida en metros:")
        self.input_metros = QLineEdit()

        self.radio_pies = QRadioButton("Pies (ft)")
        self.radio_pulgadas = QRadioButton("Pulgadas (in)")
        self.radio_yardas = QRadioButton("Yardas (yd)")
        self.radio_pies.setChecked(True)

        self.grupo_opciones = QButtonGroup()
        self.grupo_opciones.addButton(self.radio_pies)
        self.grupo_opciones.addButton(self.radio_pulgadas)
        self.grupo_opciones.addButton(self.radio_yardas)

        self.button_convertir = QPushButton("Convertir")
        self.result_label = QLabel("Resultado: ")

        layout = QVBoxLayout()

        layout.addWidget(self.label_metros)
        layout.addWidget(self.input_metros)

        layout.addWidget(self.radio_pies)
        layout.addWidget(self.radio_pulgadas)
        layout.addWidget(self.radio_yardas)

        layout.addWidget(self.button_convertir)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.button_convertir.clicked.connect(self.convertir)

    def convertir(self):
        try:
            metros = float(self.input_metros.text())

            if self.radio_pies.isChecked():
                resultado = metros * METROS_A_PIES
                unidad = "ft"
            elif self.radio_pulgadas.isChecked():
                resultado = metros * METROS_A_PULGADAS
                unidad = "in"
            else:
                resultado = metros * METROS_A_YARDAS
                unidad = "yd"

            self.result_label.setText(f"Resultado: {resultado:.4f} {unidad}")

        except ValueError:
            QMessageBox.warning(self, "Error de entrada", "Por favor ingrese un número válido.")


app = QApplication(sys.argv)
window = ConvertirMetrosWindow()
window.show()
sys.exit(app.exec())
