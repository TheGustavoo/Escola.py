from models.sala_de_aula import SalaDeAula


class Escola:

    def __init__(self, nome: str, cnpj: str):
        self.nome = nome
        self.cnpj = cnpj
        self._salas: list[SalaDeAula] = []  
        self._professores = []            

    def adicionar_sala(self, numero: int, capacidade: int) -> SalaDeAula:
        if any(s.numero == numero for s in self._salas):
            raise ValueError(f"Sala {numero} já existe nesta escola")
        sala = SalaDeAula(numero, capacidade)
        self._salas.append(sala)
        return sala

    def remover_sala(self, numero: int) -> None:
        self._salas = [s for s in self._salas if s.numero != numero]

    def listar_salas(self) -> list[SalaDeAula]:
        return list(self._salas)

    def adicionar_professor(self, professor) -> None:
        if professor not in self._professores:
            self._professores.append(professor)
            professor._vincular(self)

    def remover_professor(self, professor) -> None:
        if professor in self._professores:
            self._professores.remove(professor)
            professor._desvincular(self)

    def listar_professores(self) -> list:
        return list(self._professores)

    def fechar(self) -> None:
        """Fecha a escola"""
        self._salas.clear()
        for professor in list(self._professores):
            self.remover_professor(professor)
