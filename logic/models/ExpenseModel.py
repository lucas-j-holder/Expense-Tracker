from logic.models.FinancialModel import FinancialModel
from logic.enums.Frequencies import Frequencies
class ExpenseModel(FinancialModel):
  def __init__(self, name: str, amount: float, category: str, frequency: Frequencies):
    super().__init__(name=name, amount=amount, category=category, frequency=frequency)
    