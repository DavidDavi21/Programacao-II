from peewee import *
arq = '/home/david.martines/modelo.db'db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta():
        database = db

class Jogador(BaseModel):    
    nome = CharField()    
    idade = IntegerField()    
    tamanho = FloatField()

class Tecnico(BaseModel):    
    nome = CharField()    
    idade = IntegerField()

class Time(BaseModel):    
    nome = CharField()    
    jogadores = ForeignKeyField(Jogador)    
    tecnico_do_time = ForeignKeyField(Tecnico)

class Organizacao(BaseModel):    
    nome = CharField()    
    data_evento = DateTimeField()
    
class Campeonato(BaseModel):    
    times = ManyToManyField(Time)    
    organizacao = ForeignKeyField(Organizacao)
    
class Esporte(BaseModel):    
    nome = CharField()    
    caracteristicas = CharField()    
    equipes = ManyToManyField(Time)
    
class Arbitro(BaseModel):    
    nome = CharField()    
    idade = IntegerField()    
    nacionalidade = CharField()

class Torcedor(BaseModel):    
    nome = CharField()    
    idade = IntegerField()    
    tamanho = FloatField()    
    nacionalidade = CharField()    
    time_torcedor = ManyToManyField(Time)
    
class Partida(BaseModel):    
    esporte = ForeignKeyField(Esporte)    
    total_pontos = IntegerField()    
    jogo = ManyToManyField(Time)    
    arbritros = ForeignKeyField(Arbitro)
    
class Premiacao(BaseModel):    
    equipe_premiada = ForeignKeyField(Time)    
    jogador_premiado = ManyToManyField(Jogador)
    
if __name__ == "__main__":
    db.connect()    
    db.create_tables([Premiacao, Partida, Torcedor, Organizacao, Arbitro, Esporte, Tecnico, Campeonato, Jogador, Time, Campeonato.times.get_through_model(), Esporte.equipes.get_through_model(), Torcedor.time_torcedor.get_through_model(), Partida.jogo.get_through_model(), Premiacao.jogador_premiado.get_through_model()])        jogador1 = Jogador.create(nome="João Kleber", idade=16, tamanho=1.75)
    
    tecnico1 = Tecnico.create(nome="Fausto Silva", idade=45)
    arbitro1 = Arbitro.create(nome="Gabriel Jesus", idade=17, nacionalidade="Brasileiro")
    time1 = Time.create(nome="Sao José de Rio Rosa", jogadores=jogador1, tecnico_do_time=tecnico1)
    organizacao_do_evento = Organizacao.create(nome="CBF", data_evento=12/5/2015)
    esporte1 = Esporte.create(nome="Futebol", caracteristicas="bola")
    torcedor1 = Torcedor.create(nome="Lucas", idade=28, tamanho=1.63, nacionalidade="Argentino")
    premiacao_partida = Premiacao.create(equipe_premiada=time1)
    campeonato1 = Campeonato.create(organizacao=organizacao_do_evento)        
    partida = Partida.create(esporte="Futebol", total_pontos="0/0", arbitros=arbitro1)
    
    campeonato1.times.add(time1)    
    esporte1.equipes.add(time1)    
    torcedor1.time_torcedor(time1)    
    partida.jogo.add(time1)    
    premiacao_partida.jogador_premiado.add(jogador1)
    
    for i in campeonato1.times:        
        print(i.nome)
