import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow
from components.display import Display
from components.info_calculo import InfoCalc
from constants import WINDOW_ICON_PATH
from styles import setupTheme
from components.button import Button

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    setupTheme()

    # Define o icone da aplicação
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Label com as informações do histórico de cálculos
    info = InfoCalc('2.0 ^ 10.0 = 1024 ')
    window.addWidgetToVLayout(info)

    # Input para calcular
    display = Display()
    window.addWidgetToVLayout(display)

    button = Button('Texto do Botão')
    window.addWidgetToVLayout(button)

    window.adjustFixedSize()

    window.show()
    app.exec()  # Loop da aplicação
