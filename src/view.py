from .controller import EstoqueController
from .utils import pausar_e_limpar

# Dados iniciais
ESTOQUE_INICIAL = (
    "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#"
    "Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#"
    "Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#"
    "Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"
)

def carregar_estoque_inicial(controller: EstoqueController) -> None:
    """Carrega os dados iniciais de estoque a partir de uma string."""
    for produto in ESTOQUE_INICIAL.split("#"):
        controller.cadastrar_produto_de_string(produto)

def exibir_produtos(produtos: list) -> None:
    """Função auxiliar para exibir produtos formatados."""
    for produto_info in produtos:
        produto = produto_info['produto']
        quantidade = produto_info['quantidade']
        print(f"{produto.descricao} (Código: {produto.codigo}) - Quantidade: {quantidade} - Preço: R${produto.preco_venda}")

def exibir_produtos_ordenados(controller: EstoqueController, crescente: bool = True) -> None:
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
    exibir_produtos(produtos_ordenados)

def adicionar_produto(controller: EstoqueController) -> None:
    """Permite ao usuário adicionar um novo produto."""
    dados_produto = input("Digite os dados do produto no formato 'Descrição;Código;Quantidade;Custo;Preço de Venda': ")
    try:
        controller.cadastrar_produto_de_string(dados_produto)
        print("Produto adicionado com sucesso!")
    except ValueError as e:
        print(f"Erro ao adicionar produto: {e}")

def atualizar_quantidade(controller: EstoqueController) -> None:
    """Permite ao usuário atualizar a quantidade de um produto no estoque (entrada ou saída)."""
    try:
        codigo = int(input("Digite o código do produto: "))
        operacao = input("Digite 'entrada' para adicionar ou 'saida' para remover: ").strip().lower()
        quantidade = int(input("Digite a quantidade: "))

        controller.atualizar_estoque(codigo, quantidade, operacao)
        print(f"Quantidade {operacao} realizada com sucesso!")
    except ValueError as e:
        print(f"Erro ao atualizar quantidade: {e}")

def buscar_produto(controller: EstoqueController) -> None:
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
    
def remover_produto(controller: EstoqueController) -> None:
    """Permite ao usuário remover um produto pelo código."""
    try:
        codigo = int(input("Digite o código do produto que deseja remover: "))
        controller.remover_produto(codigo)
    except ValueError as e:
        print(f"Erro ao remover produto: {e}")

def listar_produtos_esgotados(controller: EstoqueController) -> None:
    """Exibe todos os produtos esgotados (quantidade igual a zero)."""
    produtos_esgotados = controller.listar_produtos_esgotados()

    if not produtos_esgotados:
        print("Nenhum produto esgotado.")
    else:
        print("Produtos esgotados:")
        exibir_produtos(produtos_esgotados)

def filtrar_produtos_com_baixa_quantidade(controller: EstoqueController) -> None:
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

def exibir_menu() -> None:
    """Exibe o menu interativo para o usuário."""
    print("\n==== MENU DE CONTROLE DE ESTOQUE ====")
    print("1. Listar produtos por quantidade (crescente)")
    print("2. Listar produtos por quantidade (decrescente)")
    print("3. Adicionar produto")
    print("4. Atualizar quantidade de produto (entrada/saída)")
    print("5. Buscar produto")
    print("6. Remover produto")
    print("7. Listar produtos esgotados")
    print("8. Filtrar produtos com baixa quantidade")
    print("9. Sair")
    print("======================================")
