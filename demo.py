
from models.aluno import Aluno
from models.escola import Escola
from models.professor import Professor

escola = Escola("Escola Cev", "12.345.678/0001-90")
escola.adicionar_sala(101, 30)
escola.adicionar_sala(102, 25)
print("Salas antes de fechar:", [s.numero for s in escola.listar_salas()])

ana = Professor("Ana", "111.111.111-11", "Matemática")
outra = Escola("Colégio Nassau", "98.765.432/0001-10")
ana.lecionar_em(escola)
ana.lecionar_em(outra)
print("Escolas da Ana:", [e.nome for e in ana.listar_escolas()])
print(ana.ministrar_aula(escola, 101))

escola.fechar()
print("Salas depois da escola fechar:", escola.listar_salas())
print("Ana continua existindo e leciona em:", [e.nome for e in ana.listar_escolas()])


aluno = Aluno("João", "2026001", "2010-05-12",
              {"rua": "Rua das Flores", "numero": "10", "bairro": "Centro",
               "cidade": "Parnaíba", "estado": "PI", "cep": "64200-000"})
print(aluno.ficha())
endereco = aluno.remover()
print("Aluno removido. Endereço repassado ao relatório:", endereco.endereco_completo())
