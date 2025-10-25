#menus e textos
menu_inicial = """
=======================================================================
#  +Bem-vindo ao Banco Din$                                           #
#                                                                     #
#  -Digite 1: caso já seja cadastrado;                                #
#                                                                     #
#  -Digite 2: Caso queira criar um cadastro;                          #
#                                                                     #
#  -Digite 0: Para sair do programa;                                  #
#                                                                     #
=======================================================================
"""
erro_teclado = f"\nUsuário cancelou programa:{KeyboardInterrupt}"

erro_valor = f"\nDigite o valor correto! {ValueError}"

indicador = "> "

digite_correto = "\nDigite o valor correto!"

mensagem_saida = "\nMuito obrigado por usar nossos serviços!"

usuarios = []

def login_usuario():
    
    pass

def cadastrar_usuario():
    pass

def menu():
    print(menu_inicial)
    
    while True:
        try:
            validador_usuario = int(input(indicador))
            
            match validador_usuario:
                case 0:
                    print(mensagem_saida)
                    exit()
                case 1:
                    login_usuario()
                case 2:
                    cadastrar_usuario()
                case _:
                    print(digite_correto)
        except ValueError:
            print(erro_valor)
pass

def main() -> None:
   
   validador_usuario = menu()

   pass
    
if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print(erro_teclado)
            break
    pass