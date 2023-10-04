# Expense Tracker - Expense Tracking Program - Widgets
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

from PyQt6.QtWidgets import QDialog, QWidget
from ui.Ui_EditFinancial import Ui_EditFinancial
from logic.Models import FinancialModel
from logic.enums import Frequencies, CompoundFrequencies
from multimethod import multimethod, overload
from ui.Ui_EditInvestment import Ui_EditInvestment
from ui.Ui_ExpenseTableWithButtons import Ui_ExpenseTableWithButtons

class ExpenseTableWithButtonsWidget(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.ui = Ui_ExpenseTableWithButtons()
    self.ui.setupUi(self)
    columns = ["Name", "Amount", "Category", "Frequency"]
    self.ui.expense_table.setColumnCount(len(columns))
    self.ui.expense_table.setHorizontalHeaderLabels(columns)

class ExpenseTableDisplayWidget(ExpenseTableWithButtonsWidget):
  def show_new_menu(self):
    return EditFinancialDialog(self)
  def show_edit_menu(self):
    return EditFinancialDialog(FinancialModel(), self)
  def __init__(self, parent=None):
    super().__init__(parent)
    # self.ui = Ui_ExpenseTableWithButtons()
    # self.ui.setupUi(self)
    self.ui.expense_new.clicked.connect(lambda: self.show_new_menu())
    self.ui.expense_edit.clicked.connect(lambda: self.show_edit_menu())

class IncomeTableDisplayWidget(ExpenseTableWithButtonsWidget):
  def show_new_menu(self):
    return EditFinancialDialog(self)
  def show_edit_menu(self):
    return EditFinancialDialog(FinancialModel(), self)
  def __init__(self, parent=None):
    super().__init__(parent)
    # self.ui = Ui_ExpenseTableWithButtons()
    # self.ui.setupUi(self)
    self.ui.expense_new.clicked.connect(lambda: self.show_new_menu())
    self.ui.expense_edit.clicked.connect(lambda: self.show_edit_menu())
  
class InvestmentTableDisplayWidget(QWidget):
  def show_new_menu(self):
    return EditFinancialDialog(self)
  def show_edit_menu(self):
    return EditFinancialDialog(FinancialModel(), self)
  def __init__(self, parent=None):
    super().__init__(parent)
    self.ui = Ui_ExpenseTableWithButtons()
    self.ui.setupUi(self)
    columns = ["Name", "Principal", "Return Rate", "Compound Freq.", "Add. Contrib.", "Add. Contrib. Freq."]
    self.ui.expense_table.setColumnCount(len(columns))
    self.ui.expense_table.setHorizontalHeaderLabels(columns)
    self.ui.expense_new.clicked.connect(lambda: self.show_new_menu())
    self.ui.expense_edit.clicked.connect(lambda: self.show_edit_menu())


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

