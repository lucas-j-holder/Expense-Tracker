# Expense Tracker - Expense Tracking Program - InvestmentTableDisplayWidget.py
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

from PyQt6.QtWidgets import QWidget
from ui.Ui_ExpenseTableWithButtons import Ui_ExpenseTableWithButtons
from logic.EditFinancialDialog import EditFinancialDialog
from logic.models.FinancialModel import FinancialModel
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