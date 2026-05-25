#---simulador de poupança---
aporte = float(input("quanto você vai depositar por mês? "))
juros = float(input("qual a taxa de juros da poupança? "))
meses = int(input("por quantos meses você vai ivestir "))
juros_decimal = juros/100
total = 0
for mês  in range(1, meses +1):
    total = total + aporte
    total = total + (total * juros_decimal)
    print(f"mês{mês}: saldo total R${total}")
print(f"ao final de {mês} meses, você terá o valor de R${total:.2f}")