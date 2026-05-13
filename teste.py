# Criando um Teste com Pontuação--
print("Teste seus Conhecimentos sobre Ciências")
pontos =0
#--Questão 1--
print("qual é a formula da água?")
print("a-H2O \n b-CO2 \n c-AL")
resposta1 = input("digite a resposta: ").lower()
if resposta1 == "a":
    print("resposta correta")
    pontos = pontos +1
else:
    print("você errou")
#Questão 2--
print("2- 0 sol é : ")
print("a-Satélite \n b-Estrela \n c-Asteróide")
resposta2 = input("digite a Resposta: ").lower()
if resposta2 == "b":
    print("Você acertou")
    pontos = pontos +1
else:
    print("Você errou")