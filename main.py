import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from components.display import Display
from components.info_calculo import InfoCalc
from constants import WINDOW_ICON_PATH
from styles import setup_theme
from components.buttons.button_grid import ButtonGrid
from components.buttons.button import Button

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    setup_theme()

    # Define o icone da aplicação
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Label com as informações do histórico de cálculos
    info = InfoCalc('2.0 ^ 10.0 = 1024 ')
    window.add_widget_to_vlayout(info)

    # Input para calcular
    display = Display()
    window.add_widget_to_vlayout(display)

    button_grid = ButtonGrid()
    window.v_layout.addLayout(button_grid)

    window.adjust_fixed_size()

    window.show()
    app.exec()  # Loop da aplicação
