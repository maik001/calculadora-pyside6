from PySide6.QtWidgets import QGridLayout
from components.buttons.button import Button
from utils.utils import is_empty, is_num_or_dot


class ButtonGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]

        self._make_grid()

    def _make_grid(self):
        for row, list_data in enumerate(self._grid_mask):
            for col, text in enumerate(list_data):
                button = Button(text)
                if not is_num_or_dot(text) and not is_empty(text):
                    button.setProperty('cssClass', 'specialButton')
                self.addWidget(button, row, col)
