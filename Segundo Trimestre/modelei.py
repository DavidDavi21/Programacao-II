class Pessoa:

	def __init__(self, nome, cpf):
		self.nome = nome
		self.cpf = cpf

	def __str__(self):
		return "nome: " + self.nome + ", cpf: " + self.cpf

class Aluno(Pessoa):

	def __init__(self, nome, cpf, curso, turma, matricula):
		super.__init__(nome, cpf)
		self.curso = curso
		self.turma = turma
		self.matricula = matricula

		def __str__(self):
		return "nome: " + self.nome + ", cpf: " + self.cpf + ", curso: " + self.curso + ", turma: " + self.turma + ", matrícula: " + self.matricula

class Professor(Pessoa):

	def __init__(self, nome, cpf, areas, codProfessor):
		super.__init__(nome, cpf)
		self.areas = areas
		self.codProfessor = codProfessor

		def __str__(self):
		return "nome: " + self.nome + ", cpf: " + self.cpf + ", areas: " + self.areas + ", código do professor: " + self.codProfessor

class PI:

	def __init__(self, titulo, ano, nomesAlunos, nomesProfessores):
		self.titulo = titulo
		self.ano = ano
		self.nomesAlunos = nomesAlunos
		self.nomesProfessores = nomesProfessores

		def __str__(self):
		return "titulo: " + self.titulo + ", ano: " + self.ano + ", nome de alunos: " + self.nomesAlunos + ", nome dos professores: " + self.nomesProfessores

class Periodico:

	def __init__(self, ISSN, editora):
		self.ISSN = ISSN
		self.editora = editora

		def __str__(self):
		return "ISSN: " + self.ISSN + ", editora: " + self.editora

class Evento:

	def __init__(self, data, local):
		self.data = data
		self.local = local

	def __str__(self):
		return "data: " + self.data + ", local: " + self.local

if __name__ == "__main__":

	pessoa = Pessoa('Bocó', "12345678-78")
	aluno = Aluno('Informática', '302', '201730325')
	professor = Professor('Todas as áreas', '78958754')
	pi = PI('Uma aventura e meia', '2085', 'GUstavão e Marcelinho da QUebrada', 'Deivis, the best')
	periodico = Periodico('85465465465', 'Saraiva')
	evento = Evento('12/12/12', 'São Paulo')

	print(pessoa)
	print(aluno)
	print(professor)
	print(pi)
	print(periodico)
	print(evento)