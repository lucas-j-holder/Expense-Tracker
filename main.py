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

from ui import UI_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    qmainwindow = QMainWindow()
    main_window = UI_MainWindow.Ui_MainWindow()
    main_window.setupUi(qmainwindow)

    qmainwindow.show()

    sys.exit(app.exec())