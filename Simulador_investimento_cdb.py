aporte = float(input("quanto você vai depositar por mês? "))
CDB = float(input("qual a taxa de juros do CDB? "))
meses = int(input("por quantos meses você vai ivestir? "))
CDB_decimal = CDB/100
total = 0
for mês  in range(1, meses +1):
    total = total + aporte
    total = total + (total * CDB_decimal)
    print(f"mês {mês}: saldo total = R${total}")
print(f"ao final de {mês} meses, você terá o valor de R${total:.2f}")