import math 

radio_circulo = float(input())
area_circulo = math.pi * (radio_circulo ** 2)
longitud_circunferencia = math.pi * radio_circulo * 2 
print(f"El área del círculo es: {area_circulo} y la longitud de la " 
      f"circunferencia es: {longitud_circunferencia}")