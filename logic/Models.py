from logic.enums import Frequencies, CompoundFrequencies
class FinancialModel():
  def __init__(self, name: str = "", amount: float = 0.0, category: str = "", frequency: Frequencies = Frequencies.Biweekly):
    self.amount = amount,
    self.name = name,
    self.category = category
    self.frequency = frequency

class IncomeModel(FinancialModel):
  def __init__(self, name: str, amount: float, category: str, frequency: Frequencies):
    super().__init__(name=name, amount=amount, category=category, frequency=frequency)

class ExpenseModel(FinancialModel):
  def __init__(self, name: str, amount: float, category: str, frequency: Frequencies):
    super().__init__(name=name, amount=amount, category=category, frequency=frequency)
    
class InvestmentModel():
  def __init__():
    pass