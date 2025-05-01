# ATENÇÃO O CÓDIGO A SEGUIR POSSUI A FINALIDADE DIDATICA, NÃO É UM CÓDIGO OFICIAL E NÃO DEVE SER UTILIZADO PARA CÁLCULOS FISCAIS REAIS.
salario = float(input("Insira o seu salário: "))

# O código a seguir utiliza os valores da "Base de cálculo da Receita Federal"

if salario <= 2428.80:
  print(f"Colaborador Isento de Imposto")
  print(f"Salário a receber = {salario}")

elif salario <= 2826.65:
  print(f"Colaborador deve pagar imposto de 7,5%, valor R$182.16")
  print(f"Salário a receber = {salario - 182.16}")

elif salario <= 3751.05:
  print(f"Colaborador deve pagar imposto de 15%, valor R$394.16")
  print(f"Salário a receber = {salario - 394.16}")

elif salario <= 4664.68:
  print(f"Colaborador deve pagar imposto de 22,5%, R$675.49")
  print(f"Salário a receber = {salario - 675.49}")
else:
  print(f"Acima de 4.664,68 o Colaborador deve pagar 27,5%, valor R$908.73")
  print(f"Salário a receber = {salario - 908.73}")


#A nova tabela progressiva mensal do IRPF passará a vigorar a partir de maio de 2025:
# Fonte das Informações: Agência Senado 14/04/2025, 12h42
# Site: https://www12.senado.leg.br/noticias/materias/2025/04/14/governo-publica-mp-que-reajusta-faixa-de-isencao-do-imposto-de-renda