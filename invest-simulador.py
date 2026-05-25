#--- simulador de investimentos ---
deposito_mensal = 50
total = 0
for mes in range(1,7):
    total = total + deposito_mensal
    print(f"mês {mes}: saldo total = R$ {total} ")
print(f"ao final de 6 meses, você terá: R${total}")
