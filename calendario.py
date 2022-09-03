#calendario anual en Python
from calendar import *
import datetime

year = int(input("Ingresa año:"))
today = datetime.datetime.now()
print(calendar(year, 2, 1, 8, 4))
print("Hoy es: ", "")
print ("Día : ", end = "")
print(today.day)
print ("Mes : ", end = "")
print(today.month)
print ("Año : ", end = "")
print(today.year)