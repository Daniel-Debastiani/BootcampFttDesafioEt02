from personagem_entity import personagem
from personagem_service import criar_personagem


def exibir_menu():
    print("""\n============| Menu |============
1. Criar Personagem
2. Ver Personagens
3. Sair""")

personagens = []

menu_opcao = "0"
while menu_opcao != "3":
    exibir_menu()
    menu_opcao = input("Escolha uma opção: ")
    if menu_opcao == "1":
        novo_personagem = criar_personagem()
        personagens.append(novo_personagem)
    elif menu_opcao == "2":
        if personagens:
            for personagem in personagens:
                print(f"\n{personagem}")
        else:
            print("\nNENHUM PERSONAGEM REGISTRADO!")
    elif menu_opcao == "3":
        print("\nSaindo do programa...")
    else:
        print("\nOpção inválida! Por favor, escolha uma opção válida.")