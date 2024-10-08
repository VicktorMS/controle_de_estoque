from typing import Dict, List
from .model import Produto

class ProdutoParser:
    @staticmethod
    def parse(dados_produto: str) -> Produto:
        """Faz o parsing de uma string de dados para criar um objeto Produto."""
        try:
            descricao, codigo, quantidade, custo, preco_venda = dados_produto.split(';')
            return Produto(
                descricao=descricao,
                codigo=int(codigo),
                quantidade=int(quantidade),
                custo=float(custo),
                preco_venda=float(preco_venda)
            )
        except ValueError as e:
            raise ValueError(f"Erro ao processar os dados do produto: {e}")

class CadastroController:
    def __init__(self) -> None:
        self.produtos: Dict[int, Dict[str, Produto]] = {}

    def cadastrar_produto(self, produto: Produto) -> None:
        """Cadastra um novo produto no estoque."""
        if produto.codigo in self.produtos:
            raise ValueError(f"O código {produto.codigo} já existe")
        self.produtos[produto.codigo] = {
            'produto': produto,
            'quantidade': produto.quantidade
        }

    def cadastrar_produto_de_string(self, dados_produto: str) -> None:
        """Cadastra um produto a partir de uma string com seus dados."""
        produto = ProdutoParser.parse(dados_produto)
        self.cadastrar_produto(produto)

    def remover_produto(self, codigo_produto: int) -> None:
        """Remove um produto do estoque com base no código."""
        if codigo_produto in self.produtos:
            del self.produtos[codigo_produto]
            print(f"Produto com código {codigo_produto} removido com sucesso.")
        else:
            raise ValueError(f"Produto com código {codigo_produto} não encontrado.")


class ConsultaController:
    def __init__(self, cadastro_controller: CadastroController) -> None:
        self.produtos = cadastro_controller.produtos

    def listar_produtos(self) -> Dict[int, Dict[str, Produto]]:
        """Retorna todos os produtos cadastrados."""
        return self.produtos if self.produtos else {}

    def buscar_produtos(self, termo: str = "", codigo: int = None) -> List[Dict[str, Produto]]:
        """Busca produtos no estoque por descrição ou código."""
        resultados = []

        if codigo is not None:
            if codigo in self.produtos:
                resultados.append(self.produtos[codigo])
            return resultados

        if termo:
            for produto_info in self.produtos.values():
                if termo.lower() in produto_info['produto'].descricao.lower():
                    resultados.append(produto_info)

        return resultados

    def consultar_estoque(self, codigo_produto: int) -> str:
        """Retorna a quantidade de um produto específico no estoque."""
        if codigo_produto not in self.produtos:
            raise ValueError(f"Produto com código {codigo_produto} não encontrado.")
        produto = self.produtos[codigo_produto]['produto']
        quantidade = self.produtos[codigo_produto]['quantidade']
        return f"{produto.descricao}: {quantidade} unidades"


class EstoqueController:
    def __init__(self, cadastro_controller: CadastroController) -> None:
        self.produtos = cadastro_controller.produtos

    def verificar_produto_existe(self, codigo_produto: int) -> None:
        """Verifica se um produto com o código informado existe no estoque."""
        if codigo_produto not in self.produtos:
            raise ValueError(f"Produto com código {codigo_produto} não encontrado.")

    def atualizar_estoque(self, codigo_produto: int, quantidade: int, operacao: str) -> None:
        """Atualiza a quantidade de um produto no estoque com base na operação (entrada/saída)."""
        self.verificar_produto_existe(codigo_produto)
        
        if operacao == "entrada":
            self.produtos[codigo_produto]['quantidade'] += quantidade
        elif operacao == "saida":
            if self.produtos[codigo_produto]['quantidade'] < quantidade:
                raise ValueError(f"Estoque insuficiente para a quantidade solicitada. Estoque atual: {self.produtos[codigo_produto]['quantidade']}")
            self.produtos[codigo_produto]['quantidade'] -= quantidade
        else:
            raise ValueError("Operação inválida. Use 'entrada' para adicionar ou 'saida' para remover.")

    def listar_produtos_esgotados(self) -> list:
        """Retorna uma lista de produtos que estão esgotados (quantidade igual a zero)."""
        produtos_esgotados = [
            produto_info for produto_info in self.produtos.values()
            if produto_info['quantidade'] == 0
        ]
        return produtos_esgotados

    def filtrar_produtos_com_baixa_quantidade(self, limite_minimo: int = 10) -> list:
        """Filtra os produtos cuja quantidade esteja abaixo de um limite mínimo."""
        produtos_filtrados = [
            produto_info for produto_info in self.produtos.values() 
            if produto_info['quantidade'] < limite_minimo
        ]
        return produtos_filtrados