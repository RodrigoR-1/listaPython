empresa = {
"nome": "mercado nova",
"cnpj": "12,345.678/0001-90",
"endereço": "Rua da casa branca, 123 - Bairro centro - cidade",
"telefone": "*(11) 99999-9999",
"email": "supermercado@mercado.com",
"area": "repositor",
"responsavel": "João Silva"}

produtos = {
	1: {"ID": 1, "nome": "Arroz", "quantidade": 20, "preço": 24.90},
	2: {"ID": 2, "nome": "Feijão", "quantidade": 15, "preço": 8.50},
	3: {"ID": 3, "nome": "Macarrão", "quantidade": 30, "preço": 4.75},
	4: {"ID": 4, "nome": "Leite", "quantidade": 12, "preço": 5.20},
	5: {"ID": 5, "nome": "Café", "quantidade": 10, "preço": 18.90},
}

matriz_produtos = [
	[produtos[1]["ID"], produtos[2]["ID"], produtos[3]["ID"]],
	[produtos[4]["ID"], produtos[5]["ID"], 0],
]


def buscar_produto():
	try:
		id_produto = int(input("Digite o ID do produto: "))
	except ValueError:
		print("ID inválido. Digite um número inteiro.")
		return

	produto = produtos.get(id_produto)
	if produto is None:
		print("Produto não encontrado.")
		return

	print(f"Nome: {produto['nome']}")
	print(f"Quantidade: {produto['quantidade']}")
	print(f"Preço: R$ {produto['preço']:.2f}")


def mostrar_produtos():
	for produto in produtos.values():
		print(
			f"ID: {produto['ID']} | Nome: {produto['nome']} | "
			f"Quantidade: {produto['quantidade']} | "
			f"Preço: R$ {produto['preço']:.2f}"
		)


def mostrar_empresa():
	for campo, valor in empresa.items():
		print(f"{campo.capitalize()}: {valor}")


while True:
	print("\n--- Menu principal ---")
	print("1 - Consultar produto pelo ID")
	print("2 - Mostrar todos os produtos")
	print("3 - Mostrar dados da empresa")
	print("0 - Sair")
	opcao = input("Escolha uma opção: ")

	if opcao == "1":
		buscar_produto()
	elif opcao == "2":
		mostrar_produtos()
	elif opcao == "3":
		mostrar_empresa()
	elif opcao == "0":
		print("Programa encerrado.")
		break
	else:
		print("Opção inválida. Escolha 1, 2, 3 ou 0.")

