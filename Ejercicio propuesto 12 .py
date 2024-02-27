horas_trabajadas = 48 
pago_por_hora = 5000
salario_bruto = horas_trabajadas * pago_por_hora
retencion_de_fuente = salario_bruto * (12.5 / 100)
salario_neto = salario_bruto - retencion_de_fuente 

print(f"El salario bruto del empleado es: {salario_bruto}, la retención " 
      f"de fuente es: {int(retencion_de_fuente)} y el salario neto es: "
      f"{int(salario_neto)}")