from menu import menu_principal, ler_dados, salvar_dados, validação_de_entrada, continuar

while True:
    menu_principal()
    option = validação_de_entrada('Sua Opção: ')
    if option == 1:
        ler_dados()
        continuar()
    elif option == 2:
        salvar_dados()
        continuar()
    elif option == 3:
        continuar()
        break
