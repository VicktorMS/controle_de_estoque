from src.controller import EstoqueController, CadastroController, ConsultaController
from src.utils import pausar_e_limpar
from src.views.produto_view import (
    adicionar_produto,
    buscar_produto,
    carregar_estoque_inicial,
    exibir_produtos_ordenados,
    remover_produto
    )
from src.views.estoque_view import (
    atualizar_quantidade,
    filtrar_produtos_com_baixa_quantidade,
    listar_produtos_esgotados
    )
from src.views.menu_view import exibir_menu

def main() -> None:
    """Função principal para inicializar o sistema de estoque com menu interativo."""
    cadastro_controller = CadastroController()  
    estoque_controller = EstoqueController(cadastro_controller)
    consulta_controller = ConsultaController(cadastro_controller)

    carregar_estoque_inicial(cadastro_controller)

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
