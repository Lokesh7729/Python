# Let's create a Python notes file for "Modules in Python"

notes_content = """
# 📌 Modules in Python

# ✅ Definition:
# A module in Python is simply a file containing Python code (functions, classes, or variables)
# that can be imported and reused in other programs.

# ---------------------------------------------------------
# 🔹 Types of Modules in Python
# ---------------------------------------------------------

# 1. Built-in Modules
import math
print("Square Root of 16:", math.sqrt(16))
print("Value of PI:", math.pi)

# 2. User-defined Modules
# Example: Create a file 'mymodule.py' with this code:
# def greet(name):
#     return f"Hello, {name}!"
#
# Then in main.py:
# import mymodule
# print(mymodule.greet("Lokesh"))

# 3. Third-party Modules (installed using pip)
# Example: pip install numpy
# import numpy as np
# arr = np.array([1, 2, 3])
# print(arr)

# ---------------------------------------------------------
# 🔹 Importing Modules
# ---------------------------------------------------------

# Basic Import
import math
print(math.factorial(5))

# Import with Alias
import math as m
print(m.sqrt(25))

# Import Specific Functions
from math import sqrt, pi
print(sqrt(36))
print(pi)

# Import All Functions
from math import *
print(sin(1))  # sin(1 radian)

# ---------------------------------------------------------
# 🔹 Commonly Used Built-in Modules
# ---------------------------------------------------------

import random
import datetime
import os
import sys
import json
import re
import statistics

print("Random Number:", random.randint(1, 100))
print("Current Date & Time:", datetime.datetime.now())
print("Current Working Directory:", os.getcwd())
print("Python Version:", sys.version)
print("JSON Example:", json.dumps({"name": "Lokesh", "age": 21}))
print("Regex Search:", re.search("ai", "The rain in Spain"))
print("Statistics Mean:", statistics.mean([1, 2, 3, 4, 5]))

# ---------------------------------------------------------
# 🔹 Quick Revision
# ---------------------------------------------------------
# - Module = File containing Python code.
# - Types = Built-in, User-defined, Third-party.
# - Import Methods = import, import as, from ... import.
# - Examples = math, os, random, datetime, numpy.
"""

