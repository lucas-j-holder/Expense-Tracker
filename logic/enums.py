# Expense Tracker - Expense Tracking Program - Enumerations File
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

from enum import Enum

class CompoundFrequencies(Enum):
  Annually = 1
  Semiannually = 2
  Quarterly = 3
  Semimonthly = 4
  Monthly = 5
  Biweekly = 6
  Weekly = 7
  Daily = 8
  Continuously = 9
class Frequencies(Enum):
  Biweekly = 1
  Monthly = 2
  Yearly = 3
  Daily = 4