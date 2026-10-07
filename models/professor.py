class Professor:

    def __init__(self, nome: str, cpf: str, disciplina: str):
        self.nome = nome
        self.cpf = cpf
        self.disciplina = disciplina
        self._escolas = []

    def lecionar_em(self, escola) -> None:
        escola.adicionar_professor(self)

    def deixar_escola(self, escola) -> None:
        escola.remover_professor(self)

    def listar_escolas(self) -> list:
        return list(self._escolas)

    def ministrar_aula(self, escola, numero_sala: int) -> str:
        if escola not in self._escolas:
            raise ValueError(f"{self.nome} não leciona em {escola.nome}")
        sala = next((s for s in escola.listar_salas() if s.numero == numero_sala), None)
        if sala is None:
            raise ValueError(f"Sala {numero_sala} não existe em {escola.nome}")
        sala.reservar()
        return f"{self.nome} está ministrando {self.disciplina} na sala {numero_sala}"

    def _vincular(self, escola) -> None:
        if escola not in self._escolas:
            self._escolas.append(escola)

    def _desvincular(self, escola) -> None:
        if escola in self._escolas:
            self._escolas.remove(escola)
