class Pessoa:
    def __init__(self,nome=None, Idade=35):
        self.idade = Idade
        self.nome = nome



    def cumprimentar(self):
        return f'ola{id(self)}'


if __name__ == '__main__':
    p = Pessoa('Aroldo')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Haroldo'
    print(p.nome)
    print(p.idade)


