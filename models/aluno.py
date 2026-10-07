from models.endereco import Endereco


class Aluno:

    def __init__(self, nome: str, matricula: str, data_nascimento: str, dados_endereco: dict):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self._endereco: Endereco | None = Endereco(**dados_endereco) 

    @property
    def endereco(self) -> Endereco | None:
        return self._endereco

    def mudar_endereco(self, **dados) -> None:
        if self._endereco is None:
            raise ValueError("Aluno removido: não possui mais endereço")
        self._endereco.atualizar(**dados)

    def remover(self) -> Endereco | None:
        endereco, self._endereco = self._endereco, None
        return endereco

    def ficha(self) -> dict:
        return {
            "nome": self.nome,
            "matricula": self.matricula,
            "data_nascimento": self.data_nascimento,
            "endereco": self._endereco.endereco_completo() if self._endereco else None,
        }
