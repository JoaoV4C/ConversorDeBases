from functions import *
from screens import *

def main():
    repetir = "s"
    while repetir == "s":
        print(incial())
        print(bases())
        base_inicial = validar_escolha_menu(input("Digite a base atual do número:\n"))
        numero = validar_entradas(input("Digite o número que deseja converter:\n").upper(),base_inicial)
        print(final())
        print(bases())
        base_final = validar_escolha_menu(input("Digite a base que deseja converter o número:\n"))
        opcoes(numero, base_inicial, base_final)
        repetir = validar_sim_nao(input("Deseja converter outro valor? [S] ou [N]\n").lower())

if __name__ == "__main__":
    main()