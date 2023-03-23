# Jogo rpg 
#-Classe ser vivo, base pro projeto. TODOS os personagens serão seres vivos, Atributos de Pontos de vida e pontos de ataque
#-Classes derivadas do ser vivo, Personagem e monstro.
#-Personagem atributo adicional nome 
#-Monstro atributo adicional tipo 
#-Mais duas classes derivadas de monstro, Lobo e Goblim
#-Lobo possui atributo adicional força  e goblin possui atributo adicional inteligencia

import random

class SerVivo:
    def __init__(self, vida, ataque):
        self.vida = vida
        self.ataque= ataque

class Personagem(SerVivo):
    def __init__(self, vida, ataque, nome):
        super().__init__(vida, ataque)
        self.nome = nome

class Monstro(SerVivo):
    def __init__(self, vida, ataque, tipo):
        super().__init__(vida, ataque)
        self.tipo = tipo

class Lobo(Monstro):
    def __init__(self, vida, ataque, forca):
        super().__init__(vida, ataque, 'Lobo')
        self.forca = forca

class Goblin(Monstro):
    def __init__(self, vida, ataque, inteligencia):
        super().__init__(vida, ataque, 'Goblin')
        self.inteligencia = inteligencia


personagem = Personagem(100, 10, 'Herói')
lobo = Lobo(50, 8, 12)
goblin = Goblin(30, 5, 20)

monstros = [lobo, goblin]
monstro_aleatorio = random.choice(monstros)

while True:
    # Ataque do personagem
    print(f'{personagem.nome} ataca o {monstro_aleatorio.tipo} com {personagem.ataque} de ataque')
    monstro_aleatorio.vida -= personagem.ataque
    if monstro_aleatorio.vida <= 0:
        print(f'{personagem.nome} venceu!')
        break

    # Ataque do monstro
    print(f'{monstro_aleatorio.tipo} ataca o {personagem.nome} com {monstro_aleatorio.ataque} de ataque')
    personagem.vida -= monstro_aleatorio.ataque
    if personagem.vida <= 0:
        print(f'{monstro_aleatorio.tipo} venceu!')
        break
