from bio.sequencia import Sequencia

class OrganismoFasta:
    def __init__(self, id, nome, sequencia):
        self.id = id
        self.nome = nome
        self.sequencia = Sequencia(sequencia)
    
    def __str__(self):
        return f"{self.id} | {self.nome}"
        
    def calcular_percentual(self, bases):
        return self.sequencia.calcular_percentual(bases)
