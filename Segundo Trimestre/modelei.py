class Pessoa:

	def __init__(self, nome, cpf):
		self.nome = nome
		self.cpf = cpf

class Aluno(Pessoa):

	def __init__(self, nome, cpf, curso, turma, matricula):
		super.__init__(nome, cpf):
		self.curso = curso
		self.turma = turma
		self.matricula = matricula

class Professor(Pessoa):

	def __init__(self, nome, cpf, areas, codProfessor):
		super.__init__(nome, cpf):
		self.areas = areas
		self.codProfessor = codProfessor

class PI:

	def __init__(self, titulo, ano, nomesAlunos, nomesProfessores):
		self.titulo = titulo
		self.ano = ano
		self.nomesAlunos = nomesAlunos
		self.nomesProfessores = nomesProfessores

class Periodico:

	def __init__(self, ISSN, editora):
		self.ISSN = ISSN
		self.editora = editora

class Evento:

	def __init__(self, data, local):
		self.data = data
		self.local = local