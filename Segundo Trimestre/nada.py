from peewee import *
import os

arq = "NpraN.db"
db = SqliteDatabase(arq)

class BaseModel(Model):

    class Meta:
        database = db

class Disciplina(BaseModel):
    nome = CharField()

class Aluno(BaseModel):

    nome = CharField()
    disciplinas = ManyToManyField(Disciplina)

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
