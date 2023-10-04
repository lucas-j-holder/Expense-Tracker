from logic.enums.Frequencies import Frequencies
class FinancialModel():
  def __init__(self, name: str = "", amount: float = 0.0, category: str = "", frequency: Frequencies = Frequencies.Biweekly):
    self.amount = amount,
    self.name = name,
    self.category = category
    self.frequency = frequency