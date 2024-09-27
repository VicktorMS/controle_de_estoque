from src.controller import EstoqueController, CadastroController, ConsultaController
from src.utils import pausar_e_limpar
from src.view import (
    exibir_menu, exibir_produtos_ordenados, adicionar_produto,
    atualizar_quantidade, carregar_estoque_inicial, buscar_produto,
    remover_produto, listar_produtos_esgotados, filtrar_produtos_com_baixa_quantidade
)

def main() -> None:
    """Função principal para inicializar o sistema de estoque com menu interativo."""
    cadastro_controller = CadastroController()  
    estoque_controller = EstoqueController(cadastro_controller)
    consulta_controller = ConsultaController(cadastro_controller)

    # Carregando o estoque inicial
    carregar_estoque_inicial(cadastro_controller)

    # Menu interativo
    while True:
        exibir_menu()
        opt = input("Escolha uma opção: ")

        if opt == "1":
            exibir_produtos_ordenados(consulta_controller, crescente=True)
            pausar_e_limpar()
        elif opt == "2":
            exibir_produtos_ordenados(consulta_controller, crescente=False)
            pausar_e_limpar()
        elif opt == "3":
            adicionar_produto(cadastro_controller)
            pausar_e_limpar("Produto adicionado com sucesso. Pressione Enter para continuar...")
        elif opt == "4":
            atualizar_quantidade(estoque_controller)
            pausar_e_limpar("Quantidade atualizada com sucesso. Pressione Enter para continuar...")
        elif opt == "5":
            buscar_produto(consulta_controller)
        elif opt == "6":
            remover_produto(cadastro_controller)
        elif opt == "7":
            listar_produtos_esgotados(estoque_controller)
        elif opt == "8":
            filtrar_produtos_com_baixa_quantidade(estoque_controller)
        elif opt == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            pausar_e_limpar()

if __name__ == "__main__":
    main()
