from PyQt6.QtWidgets import QDialog, QWidget
from ui.Ui_EditFinancial import Ui_EditFinancial
from logic.models.FinancialModel import FinancialModel
from logic.enums.Frequencies import Frequencies
from multipledispatch import dispatch
from multimethod import multimethod, overload


class EditFinancialDialog(QDialog):
  @overload
  def __init__(self, parent : QWidget=None):
    super().__init__(parent)
    self.ui = Ui_EditFinancial()
    self.ui.setupUi(self)
    for pair in Frequencies:
      self.ui.frequency.addItem(pair.name, pair.value)
    self.exec()
  
  @overload
  def __init__(self, model:FinancialModel, parent: QWidget=None):
    print("Edit")
    super().__init__(parent)
    self.ui = Ui_EditFinancial()
    self.ui.setupUi(self)
    for pair in Frequencies:
      self.ui.frequency.addItem(pair.name, pair.value)
    self.exec()
