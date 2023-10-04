from PyQt6.QtWidgets import QWidget
from ui.Ui_ExpenseTableWithButtons import Ui_ExpenseTableWithButtons
class ExpenseTableWithButtonsWidget(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.ui = Ui_ExpenseTableWithButtons()
    self.ui.setupUi(self)
