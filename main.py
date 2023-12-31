# Expense Tracker - Expense Tracking Program - Main File
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

from ui.Ui_MainWindow import Ui_MainWindow
from logic.Widgets import IncomeTableDisplayWidget
from logic.Widgets import ExpenseTableDisplayWidget
from logic.Widgets import InvestmentTableDisplayWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import sys
window = None


class Expense_Tracker(QMainWindow):
    def add_expense_table_to_tabbed_widget(self, tab, widget):
        table = widget(None)
        tab.layout().addWidget(table)
        return table
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.income_table = self.add_expense_table_to_tabbed_widget(self.main_ui.income, IncomeTableDisplayWidget)
        self.expense_table = self.add_expense_table_to_tabbed_widget(self.main_ui.expense, ExpenseTableDisplayWidget)
        self.investment_table = self.add_expense_table_to_tabbed_widget(self.main_ui.investments, InvestmentTableDisplayWidget)
        # self.main_ui.expense_new.clicked.connect(lambda:self.create_financial_window())
        self.show()

    # def create_financial_window(self):
    #   window = EditFinancialDialog(self)
    #   window.exec()




    
    # return EditFinancial()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Expense_Tracker()
    # qmainwindow = QMainWindow()
    # main_window.setupUi(qmainwindow)
    # window = None
    
    # qmainwindow.show()

    sys.exit(app.exec())