import pandas as pd

print("Vamos a leer el archivo Salaries.csv")
sal = pd.read_csv('Salaries.csv')


print("Vamos a imprimir su head")
print(sal.head())


print("Vamos a imprimir su información")
print(sal.info())

print("La mitjana de BasePay es:", sal['BasePay'].mean())

print("La cantidad màzima de OvertimePay és: ", sal['OvertimePay'].max())

print("Beneficis('TotalPayBenefits') fa en JOSEPH DRISCOLL",sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
