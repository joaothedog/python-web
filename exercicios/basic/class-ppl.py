class Pessoa:
    def __init__(self, nome, idade):
        # construtores p inicilizar nome e idade
        self.nome = nome
        self.idade = idade
    
    def calc_ano_nasc(self):
        from datetime import datetime
        ano_atual = datetime.now().year
        return ano_atual - self.idade
    
pessoa1 = Pessoa("Joao", 23)

print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade}")
print(f"Ano nascimento: {pessoa1.calc_ano_nasc()}")