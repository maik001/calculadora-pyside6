from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Slot
from components.buttons.button import Button
from utils.utils import is_empty, is_num_or_dot, is_valid_number
from typing import TYPE_CHECKING

# Evitar o Erro de Importação Circular (Circular Import)
if TYPE_CHECKING:
    from components.display import Display
    from components.info_calculo import InfoCalc


class ButtonGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'InfoCalc', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self._equation = ''

        self.equation = 'Qualquer Coisa'
        self._make_grid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _make_grid(self):
        for row, list_data in enumerate(self._grid_mask):
            for col, text in enumerate(list_data):
                button = Button(text)
                if not is_num_or_dot(text) and not is_empty(text):
                    button.setProperty('cssClass', 'specialButton')
                self.addWidget(button, row, col)

                button_slot = self._make_button_slot(
                        self._insert_button_text_to_display,
                        button
                )

                button.clicked.connect(button_slot)

    def _make_button_slot(self, method, *args, **kwargs):
        # Decorar o slot
        @Slot(bool)
        def real_slot():
            method(*args, **kwargs)
        return real_slot

    def _insert_button_text_to_display(self, button: Button):
        button_text = button.text()

        new_display_value = self.display.text() + button_text

        if not is_valid_number(new_display_value):
            return

        if button_text == '=':
            self.display.setText(str(eval(self.display.text())))
        else:
            self.display.insert(button_text)
