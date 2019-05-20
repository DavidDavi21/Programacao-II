class Cliente:

    def __init__(self, nome, cpf, senha, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.email = email
        self.telefone = telefone

class Animal:

    def __init__(self, nome, especie, dono):
        self.nome = nome
        self.especie = especie
        self.dono = dono

class Produto:

    def __init__(self, codigo, preco, quantidade_estoque, nome_produto):
        self.codigo = codigo
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.nome_produto = nome_produto

class Consulta:

    def __init__(self, cliente, animal, tipo_atendimento, finalidade, hoario_marcado, horario_executado):
        self.cliente = Cliente()
        self. animal = Animal()
        self.tipo_atendimento = tipo_atendimento
        self.finalidade = finalidade
        self.horario_marcado = horario_marcado
        self.horario_executado = horario_executado

dono = Cliente("João", "123", "joaosilva@gmail.com", "4002-8922")
animal = Animal("Bilú", "Vira-lata", dono)
produto = Produto()

