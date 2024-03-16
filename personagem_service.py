from personagem_entity import personagem

def criar_personagem():    
    print("\n============| Criação de Personagem! |============")

    nome = input(str("Digite o NOME do seu personagem: "))
    descricao = input(str("Insira a DESCRIÇÃO do seu personagem: "))
    imagem = input(str("Insira a IMAGEM do seu personagem: "))
    programa = input(str("Digite o PROGRAMA do seu personagem: "))
    animador = input(str("Digite o ANIMADOR do seu personagem: "))
    
    novo_personagem = personagem(nome, descricao, imagem, programa, animador)
    print("\n==============| Personagem Criado! |==============")
    print(novo_personagem)
    print("==============| Personagem Criado! |==============")
    return novo_personagem