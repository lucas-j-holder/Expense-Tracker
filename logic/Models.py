# Expense Tracker - Expense Tracking Program - Models
# Copyright (C) 2023 Lucas Holder - lucas.j.holder@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
  def __init__(self, name:str, principal:float, return_rate:float, compound_frequency:CompoundFrequencies, additional_contribution:float, additional_contribution_frequency:Frequencies):
    self.name = name
    self.principal = principal
    self.return_rate = return_rate
    self.compound_frequency = compound_frequency
    self.additional_contribution = additional_contribution
    self.additional_contribution_frequency = additional_contribution_frequency