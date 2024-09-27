from src.controller import EstoqueController, CadastroController, ConsultaController
from src.utils import pausar_e_limpar
from src.view import (
    exibir_menu, exibir_produtos_ordenados, adicionar_produto,
    atualizar_quantidade, carregar_estoque_inicial, buscar_produto,
    remover_produto, listar_produtos_esgotados, filtrar_produtos_com_baixa_quantidade
)

def main() -> None:
    """Função principal para inicializar o sistema de estoque com menu interativo."""
    # Instanciando controladores
    cadastro_controller = CadastroController()  
    estoque_controller = EstoqueController(cadastro_controller)
    consulta_controller = ConsultaController(cadastro_controller)

    # Carregando o estoque inicial
    carregar_estoque_inicial(cadastro_controller)

    # Menu interativo
    while True:
        exibir_menu()
        opt = input("Escolha uma opção: ")

        opcoes = {
            "1": lambda: exibir_produtos_ordenados(consulta_controller, crescente=True),
            "2": lambda: exibir_produtos_ordenados(consulta_controller, crescente=False),
            "3": lambda: adicionar_produto(cadastro_controller),
            "4": lambda: atualizar_quantidade(estoque_controller),
            "5": lambda: buscar_produto(consulta_controller),
            "6": lambda: remover_produto(cadastro_controller),
            "7": lambda: listar_produtos_esgotados(estoque_controller),
            "8": lambda: filtrar_produtos_com_baixa_quantidade(estoque_controller),
        }

        if opt in opcoes:
            opcoes[opt]()
            pausar_e_limpar()
        elif opt == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            pausar_e_limpar()

if __name__ == "__main__":
    main()
