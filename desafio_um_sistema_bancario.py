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

cpf_errado = "\n CPF errado. Digite novamente!"

sem_cadastro = "\nVocê não tem cadastro"

cadastrar_pergunta = "\nDeseja realizar cadastro?[Sim/Não] "

#listas
usuarios_cpf = [7572341519]

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

def checar_cpf_base(cpf:int, indice:int) -> any:
    for checar in range(len(usuarios_cpf)):
        if cpf == usuarios_cpf[checar] and indice == 0:
            return True
        elif cpf == usuarios_cpf[checar] and indice == 0:
            return checar
        else:
            return False


def login_usuario() -> any:
    while True:
        print(mensagem_informe)
        cpf_usuario = int(input(indicador_cpf).strip())
        validador_bool_1 = validador_cpf(cpf_usuario)
        validador_bool_2 = checar_cpf_base(cpf_usuario, 0)

        if validador_bool_1 and validador_bool_2:
            print(informacao_valida)
            return checar_cpf_base(cpf_errado, 1)
        elif not validador_bool_1:
            print(informacao_invalida + cpf_errado)
        elif validador_bool_1 and not validador_bool_2:
            print(informacao_invalida + sem_cadastro)

            while True:
                cadastro = input(cadastrar_pergunta).strip().lower()
                if cadastro[0] == "s":
                    cadastrar_usuario()
                    break
                elif cadastro[0] == "n":
                    print(mensagem_saida)
                    exit()
                else:
                    print(informacao_invalida)

        nome_usuario = input(indicador_nome)

def menu() -> any:
    
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

def main() -> None:
    iniciador = menu()
    
if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print(erro_teclado)
            break
        except ValueError:
            print(erro_valor)
