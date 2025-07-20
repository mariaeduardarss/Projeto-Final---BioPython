from bio.constantes import DNA_PARA_AMINOACIDO
from bio.constantes import DNA_STOP_CODONS

class Sequencia:

    def __init__(self, sequencia):
        self.sequencia = sequencia.upper()

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __iter__(self):
        return iter(self.sequencia)

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia[index]

    def calcular_percentual(self, bases):
        total = len(self.sequencia)
        if total == 0:
            return 0.0
        if isinstance(bases, str):
            bases = [bases]
        count = sum(self.sequencia.count(base.upper()) for base in bases)
        return (count / total) * 100
