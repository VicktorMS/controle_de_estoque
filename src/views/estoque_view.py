def atualizar_quantidade(controller) -> None:
    """Permite ao usuário atualizar a quantidade de um produto no estoque."""
    try:
        codigo = int(input("Digite o código do produto: "))
        operacao = input("Digite 'entrada' para adicionar ou 'saida' para remover: ").strip().lower()
        quantidade = int(input("Digite a quantidade: "))

        controller.atualizar_estoque(codigo, quantidade, operacao)
        print(f"Quantidade {operacao} realizada com sucesso!")
    except ValueError as e:
        print(f"Erro ao atualizar quantidade: {e}")


def exibir_produtos(produtos: list) -> None:
    """Exibe uma lista de produtos formatados."""
    for produto_info in produtos:
        produto = produto_info['produto']
        quantidade = produto_info['quantidade']
        print(f"{produto.descricao} (Código: {produto.codigo}) - Quantidade: {quantidade} - Preço: R${produto.preco_venda}")


def filtrar_produtos_com_baixa_quantidade(controller) -> None:
    """Permite ao usuário filtrar produtos com quantidade abaixo de um limite especificado."""
    try:
        limite = input("Digite o limite mínimo de quantidade (pressione Enter para usar o valor padrão 10): ")
        limite_minimo = int(limite) if limite else 10
    except ValueError:
        print("Limite inválido, usando valor padrão de 10.")
        limite_minimo = 10

    produtos_filtrados = controller.filtrar_produtos_com_baixa_quantidade(limite_minimo)

    if not produtos_filtrados:
        print(f"Nenhum produto com quantidade abaixo de {limite_minimo}.")
    else:
        exibir_produtos(produtos_filtrados)


def listar_produtos_esgotados(controller) -> None:
    """Exibe todos os produtos esgotados (quantidade igual a zero)."""
    produtos_esgotados = controller.listar_produtos_esgotados()

    if not produtos_esgotados:
        print("Nenhum produto esgotado.")
    else:
        print("Produtos esgotados:")
        for produto_info in produtos_esgotados:
            produto = produto_info['produto']
            print(f"{produto.descricao} (Código: {produto.codigo}) - Quantidade: 0")
