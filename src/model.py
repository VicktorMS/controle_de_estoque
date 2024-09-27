class Produto:
    def __init__(self, descricao: str, codigo: int, quantidade: int, custo: float, preco_venda: float) -> None:
        self.codigo: int = codigo
        self.descricao: str = descricao
        self.quantidade: int = quantidade
        self.custo: float = custo
        self.preco_venda: float = preco_venda
    
    def __str__(self) -> str:
        return f"{self.descricao} (Código: {self.codigo}) - Preço: R${self.preco_venda}"
    
    def __repr__(self) -> str:
        return (f"Produto({self.descricao}, Código: {self.codigo}, Quantidade: {self.quantidade}, "
                f"Custo: {self.custo}, Preço de venda: {self.preco_venda})")
