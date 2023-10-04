from PyQt6.QtWidgets import QWidget
from ui.Ui_ExpenseTableWithButtons import Ui_ExpenseTableWithButtons
from logic.EditFinancialDialog import EditFinancialDialog
from logic.models.FinancialModel import FinancialModel
class ExpenseTableDisplayWidget(QWidget):
  def show_new_menu(self):
    return EditFinancialDialog(self)
  def show_edit_menu(self):
    return EditFinancialDialog(FinancialModel(), self)
  def __init__(self, parent=None):
    super().__init__(parent)
    self.ui = Ui_ExpenseTableWithButtons()
    self.ui.setupUi(self)
    self.ui.expense_new.clicked.connect(lambda: self.show_new_menu())
    self.ui.expense_edit.clicked.connect(lambda: self.show_edit_menu())