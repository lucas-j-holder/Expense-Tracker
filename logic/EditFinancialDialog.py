from PyQt6.QtWidgets import QDialog
from ui.EditFinancial import EditFinancial
class EditFinancialDialog(QDialog):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.ui = EditFinancial()
    self.ui.setupUi(self)