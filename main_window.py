from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QPushButton, QLabel)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurar o Layout
        self.c_widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.c_widget.setLayout(self.v_layout)
        self.setCentralWidget(self.c_widget)

        # Titulo da janela
        self.setWindowTitle('Calculadora')

    # Fixa o tamanho da janela com base nos componentes(adjust)
    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # Adiciona um widget para o layout vertical
    def add_widget_to_vlayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
