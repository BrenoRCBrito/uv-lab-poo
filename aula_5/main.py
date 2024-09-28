from classes.Pais import Pais
from classes.Estado import Estado
from classes.Cidade import Cidade
from classes.Grupo import Grupo
from classes.Funcionario import Funcionario
from classes.Departamento import Departamento
from classes.Empresa import Empresa
from classes.Filial import Filial
from classes.Escolaridade import Escolaridade

pais = Pais("Brasil")
estado = Estado("RJ", pais)
cidade = Cidade("Vassouras", estado)

empresa = Empresa("Empresa1")
departamento = Departamento("Departamento1", empresa)
filial = Filial("Filial1", cidade, empresa)
escolaridade = Escolaridade("Ensino superior completo")
presidente = Funcionario("presidente1", departamento, escolaridade, filial)
grupo = Grupo("Grupo1", pais, presidente)
empresa.set_grupo(grupo)


print(presidente.get_nome_escolaridade())
print(presidente.get_nome_pais_alocacao())

coordenador = Funcionario("coordenador1", departamento, escolaridade, filial)
print(coordenador.get_estado_coordenacao())

chefia = Funcionario("chefia1", departamento, escolaridade, filial)
departamento.set_chefia(chefia)
print(chefia.get_nome_escolaridade())


diretor = Funcionario("diretor1", departamento, escolaridade, filial)
empresa.set_diretor(chefia)
print(chefia.get_nome())
