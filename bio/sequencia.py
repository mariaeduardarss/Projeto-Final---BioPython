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

    def complementar(self):
        complemento = ""
        comp_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
        for base in self.sequencia:
            complemento += comp_map.get(base, base)
        return Sequencia(complemento)

    def complementar_reversa(self):    
        complementar_obj = self.complementar()
        reversa_str = complementar_obj.sequencia[::-1]
        return Sequencia(reversa_str)

    def transcrever(self):
        rna_seq = self.sequencia.replace('T', 'U')
        return Sequencia(rna_seq)

    def traduzir(self, parar=False):
        proteina = ""
        for i in range(0, len(self.sequencia) - len(self.sequencia) % 3, 3):
            codon = self.sequencia[i:i+3]
            aminoacido = DNA_PARA_AMINOACIDO.get(codon, 'X')

            if parar and aminoacido == '*':
                break 
            proteina += aminoacido
        return proteina

    def calcular_percentual(self, bases):
        total = len(self.sequencia)
        if total == 0:
            return 0.0

        if isinstance(bases, str):
            bases = [bases]
        bases_upper = [b.upper() for b in bases]

        count = sum(self.sequencia.count(base_to_count) for base_to_count in bases_upper)

        return count / total
