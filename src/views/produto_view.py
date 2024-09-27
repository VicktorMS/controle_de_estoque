
ESTOQUE_INICIAL = (
    "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#"
    "Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#"
    "Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#"
    "Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"
)

def carregar_estoque_inicial(controller) -> None:
    """Carrega os dados iniciais de estoque a partir de uma string."""
    for produto in ESTOQUE_INICIAL.split("#"):
        controller.cadastrar_produto_de_string(produto)

def adicionar_produto(controller) -> None:
    """Permite ao usuário adicionar um novo produto."""
    dados_produto = input("Digite os dados do produto no formato 'Descrição;Código;Quantidade;Custo;Preço de Venda': ")
    try:
        controller.cadastrar_produto_de_string(dados_produto)
        print("Produto adicionado com sucesso!")
    except ValueError as e:
        print(f"Erro ao adicionar produto: {e}")

def buscar_produto(controller) -> None:
    """Busca um produto por código ou descrição."""
    criterio = input("Buscar por (1) Código ou (2) Descrição? ")

    try:
        if criterio == "1":
            codigo = int(input("Digite o código do produto: "))
            resultados = controller.buscar_produtos(codigo=codigo)
        elif criterio == "2":
            termo = input("Digite parte da descrição do produto: ")
            resultados = controller.buscar_produtos(termo=termo)
        else:
            print("Opção inválida.")
            return

        if not resultados:
            print("Nenhum produto encontrado.")
        else:
            exibir_produtos(resultados)
    except ValueError:
        print("Entrada inválida.")

def exibir_produtos_ordenados(controller, crescente: bool = True) -> None:
    """Exibe os produtos em ordem crescente ou decrescente de quantidade."""
    produtos = controller.listar_produtos()

    if not produtos:
        print("Estoque vazio.")
        return

    produtos_ordenados = sorted(
        produtos.values(),
        key=lambda x: x['quantidade'],
        reverse=not crescente
    )

    for produto_info in produtos_ordenados:
        produto = produto_info['produto']
        quantidade = produto_info['quantidade']
        print(f"{produto.descricao} (Código: {produto.codigo}) - Quantidade: {quantidade} - Preço de venda: R${produto.preco_venda}")


def remover_produto(controller) -> None:
    """Permite ao usuário remover um produto pelo código."""
    try:
        codigo = int(input("Digite o código do produto que deseja remover: "))
        controller.remover_produto(codigo)
        print(f"Produto com código {codigo} removido com sucesso!")
    except ValueError as e:
        print(f"Erro ao remover produto: {e}")
