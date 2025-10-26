#menus e textos
menu_inicial = """
=======================================================================
#  +Bem-vindo ao Banco Din$                                           #
#                                                                     #
#  -Digite 1: Caso já seja cadastrado;                                #
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

mensagem_saida = "\nSaindo do Banco\nMuito obrigado por usar nossos serviços!"

mensagem_informe = "\nInforme suas seguintes informações:"

indicador_cpf = f"\n-Digite sem pontos(.), Traços(-) ou qualquer outro sinal. Apenas números!\nCPF: "

indicador_nome = "\nNome completo: "

tamanho_minimo = 11

informacao_valida = "\nInformação Valida!"

informacao_invalida = "\nInformação Invalida!"

usuarios_cpf = []

def cadastrar_usuario():
    pass

def validador_cpf(cpf: int) -> bool:
    cpf_str = str(cpf).zfill(11)
    
    if len(cpf_str) == 11 and cpf_str != cpf_str[0] * 11:
        for posicao in range(9, 11):
            soma = sum(int(cpf_str[i]) * ((posicao + 1) - i) for i in range(posicao))
            digito = 11 - (soma % 11)
            digito = 0 if digito >= 10 else digito
            
            if int(cpf_str[posicao]) != digito:
                return False
        return True
    else:
        return False

def checar_cpf_base(cpf:int, indice:int):
    pass

def login_usuario():
    while True:
        print(mensagem_informe)
        cpf_usuario = int(input(indicador_cpf).strip())
        validador_bool_1 = validador_cpf(cpf_usuario)
        validador_bool_2 = checar_cpf_base(cpf_usuario, 1)

        if validador_bool_1 and validador_bool_2:
            print(informacao_valida)
        elif validador_bool_1 == False:
            print(informacao_invalida + "\n CPF errado. Digite novamente!")
        elif validador_bool_1 == True and validador_bool_2 == False:
            

        nome_usuario = input(indicador_nome)

def menu():
    
    while True:
        print(menu_inicial)
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
        except ValueError:
            print(erro_valor)
    pass