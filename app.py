#lista de frutas 
frutas = ["maçã", "banana", "laranja", "manga", "uva", "abacaxi"]

#exebir a lista 
for i in range(len(frutas)):
    print(f"Índice {i}: {frutas[i]}.")
try:
    #usuário informa o índice
    indice = int(input("Informe o índice da fruta que deseja excluir: "))
    confirmacao = input(f"Deseja excluir a fruta {frutas[indice]}? Digite 'SIM' para confirmar. ")
    if confirmacao == "sim":
        del(frutas[indice])
        print("Fruta deletada com sucesso.")
    else:
        ...
except Exception as e:
    print(f"Não foi possível deletar a fruta. {e}.")
finally:
    #exebir a lista
    for i in range(len(frutas)):
        print(f"Índice {i}: {frutas[i]}.")
