class Endereco:

    def __init__(self, rua: str, numero: str, bairro: str, cidade: str, estado: str, cep: str):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def endereco_completo(self) -> str:
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - CEP {self.cep}"

    def atualizar(self, **dados) -> None:
        for campo, valor in dados.items():
            if hasattr(self, campo) and valor is not None:
                setattr(self, campo, valor)

    def para_relatorio(self) -> dict:
        return {"endereco": self.endereco_completo()}
