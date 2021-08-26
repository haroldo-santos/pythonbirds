class Pessoa:
    def __init__(self,*filhos,nome=None, Idade=35):
        self.idade = Idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'ola{id(self)}'

if __name__ == '__main__':
    haroldo= Pessoa(nome='Haroldo')
    aroldo = Pessoa(haroldo, nome='Aroldo')
    print(Pessoa.cumprimentar(aroldo))
    print(id(aroldo))
    print(aroldo.cumprimentar())
    print(aroldo.nome)
    print(aroldo.idade)
    for filho in aroldo.filhos:
        print(filho.nome)

    print(aroldo.filhos)



