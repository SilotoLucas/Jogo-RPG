#tarefa da urna eletronica passada em aula, utlizando classes e metodos.

class Candidato:
    def __init__(self, nome, partido):
        self.nome = nome
        self.partido = partido

class UrnaEletronica:
    def __init__(self):
        self.candidatos = []

    def adicionar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def remover_candidato(self, nome):
        for candidato in self.candidatos:
            if candidato.nome == nome:
                self.candidatos.remove(candidato)
                return True
        return False

    def listar_candidatos(self):
        for candidato in self.candidatos:
            print(f"{candidato.nome} - {candidato.partido}")

if __name__ == "__main__":
    urna = UrnaEletronica()
    urna.adicionar_candidato(Candidato())
    urna.adicionar_candidato(Candidato())
    urna.adicionar_candidato(Candidato())

    urna.listar_candidatos()
    urna.remover_candidato()
    urna.listar_candidatos()
