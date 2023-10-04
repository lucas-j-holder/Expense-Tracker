from PyQt6.QtWidgets import QDialog, QWidget
from ui.Ui_EditInvestment import Ui_EditInvestment
from logic.models.FinancialModel import FinancialModel
from logic.enums import Frequencies
from logic.enums import CompoundFrequencies
class EditFinancialDialog(QDialog):
  def __init__(self, parent : QWidget=None):
    super().__init__(parent)
    self.ui = Ui_EditInvestment()
    self.ui.setupUi(self)
    for pair in Frequencies:
      self.ui.additional_contribution_frequency.addItem(pair.name, pair.value)
    for pair in CompoundFrequencies:
      self.ui.compound_frequency.addItem(pair.name, pair.value)
  
  def __init__(self, model:FinancialModel, parent: QWidget=None):
    super().__init__(parent)
    self.ui = Ui_EditInvestment()
    self.ui.setupUi(self)
    for pair in Frequencies:
      self.ui.additional_contribution_frequency.addItem(pair.name, pair.value)
    for pair in CompoundFrequencies:
      self.ui.compound_frequency.addItem(pair.name, pair.value)