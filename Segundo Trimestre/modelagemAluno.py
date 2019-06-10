from peewee import *
import os

arq = "NpraN.db"
db = SqliteDatabase(arq)

class Aluno(BaseModel):

	def __init__(self, nome, discplinas):
		self.nome = CharField()
		self.displinas = ManyToMany(Disciplina)

class Disciplina(BaseModel):

	def __init__(self, nome):
		self.nome = CharField()

class BaseModel(Model):

	class Meta:
		database = db

if __name__ == "__main__":
	if os.path.exists(arq):
		os.remove(arq)
	db.connect()
	db.create_tables([Aluno, Disciplina, Aluno.disciplinas.get_through_model()])
	joao = Aluno.create(nome="João")
	teresa = Aluno.create(nome="Teresa Almeida")
	ingles = Disciplina.create(nome="Inglês")
	joao.disciplinas.add(ingles)
	ingles.alunos.add(teresa)