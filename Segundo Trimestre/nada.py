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
    idade = CharField()
    disciplinas = ManyToManyField(Disciplina)

if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Aluno, Disciplina, Aluno.disciplinas.get_through_model()])
    joao = Aluno.create(nome="João", idade="21")
    teresa = Aluno.create(nome="Teresa Almeida", idade="22")
    ingles = Disciplina.create(nome="Inglês")
    joao.disciplinas.add(ingles)
    ingles.alunos.add(teresa)
    maria = Aluno.create(nome="Maria Mognon", idade="10")
    jose = Aluno.create(nome="José de Alencar", idade="5")
    programacao = Disciplina.create(nome="Programação II")
    espanhol = Disciplina.create(nome="Espanhol")
    maria.disciplinas.add(programacao)
    jose.disciplinas.add([espanhol, programacao])
    todos = Disciplina.select()
    tudo = Aluno.select()
    for disc in todos:
        print("Quem cursa a disciplina de " + disc.nome + ":")
        for aluno in disc.alunos:
            print("Nome do aluno: " + aluno.nome + ", idade:" + aluno.idade)
        print()
    for alunineos in tudo:
        print("Disciplinas de " + str(alunineos.nome) + ":")
        for disciplina in alunineos.disciplinas:
            print(disciplina.nome)
        print()
    print()
    for disci in todos:
        contador = 0
        for aluno in disci.alunos:
            contador += 1
        print("O número de alunos da disciplina de " + str(disci.nome) + " é de " + str(contador))
