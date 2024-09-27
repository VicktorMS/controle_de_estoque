from src.controller import EstoqueController
from src.utils import pausar_e_limpar
from src.view import (
    exibir_menu, 
    exibir_produtos_ordenados, 
    adicionar_produto,
    atualizar_quantidade, 
    carregar_estoque_inicial, 
    buscar_produto,
    remover_produto, 
    listar_produtos_esgotados
)

def main() -> None:
    """Função principal para inicializar o sistema de estoque com menu interativo."""
    controller = EstoqueController()

    # Carregando o estoque inicial
    carregar_estoque_inicial(controller)

    # Menu interativo
    while True:
        exibir_menu()
        opt = input("Escolha uma opção: ")

        if opt == "1":
            exibir_produtos_ordenados(controller, crescente=True)
            pausar_e_limpar()
        elif opt == "2":
            exibir_produtos_ordenados(controller, crescente=False)
            pausar_e_limpar()
        elif opt == "3":
            adicionar_produto(controller)
            pausar_e_limpar("Produto adicionado com sucesso. Pressione Enter para continuar...")
        elif opt == "4":
            atualizar_quantidade(controller)
            pausar_e_limpar("Quantidade atualizada com sucesso. Pressione Enter para continuar...")
        elif opt == "5":
            buscar_produto(controller)
        elif opt == "6":
            remover_produto(controller)
        elif opt == "7":
            listar_produtos_esgotados(controller)
        elif opt == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            pausar_e_limpar()

if __name__ == "__main__":
    main()
