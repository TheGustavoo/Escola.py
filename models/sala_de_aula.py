class SalaDeAula:

    def __init__(self, numero: int, capacidade: int):
        self.numero = numero
        self.capacidade = capacidade
        self.ocupada = False

    def reservar(self) -> None:
        if self.ocupada:
            raise ValueError(f"Sala {self.numero} já está ocupada")
        self.ocupada = True

    def liberar(self) -> None:
        self.ocupada = False

    def comporta(self, quantidade_alunos: int) -> bool:
        return quantidade_alunos <= self.capacidade
