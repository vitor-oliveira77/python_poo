class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Vitor', 'Augusto')
# p1.nome = 'Vitor'
# p1.sobrenome = 'Augusto'

p2 = Pessoa('Maria', 'Joaquina')
# p1.nome = 'Maria'
# p1.sobrenome = 'Joaquina'

print(p1.nome)
print(p1.sobrenome)
