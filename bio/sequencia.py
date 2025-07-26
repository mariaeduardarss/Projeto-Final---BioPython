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
        # Garante que a comparação seja feita com a string da sequência
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        # Permite acessar bases individuais ou fatias da sequência
        return self.sequencia[index]

    def complementar(self):
        """
        Retorna outro objeto Sequencia com a sequência complementar.
        A -> T, T -> A, C -> G, G -> C. 'N' permanece 'N'.
        """
        complemento = ""
        comp_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
        for base in self.sequencia:
            complemento += comp_map.get(base, base) # Se a base não estiver no mapa (ex: X), ela é mantida
        return Sequencia(complemento)

    def complementar_reversa(self):
        """
        Retorna outro objeto Sequencia, com a sequência complementar reversa.
        Primeiro complementa, depois inverte.
        """
        # Primeiro, obtém a sequência complementar usando o próprio método
        complementar_obj = self.complementar()
        # Depois inverte a string da sequência complementar
        reversa_str = complementar_obj.sequencia[::-1]
        return Sequencia(reversa_str)

    def transcrever(self):
        """
        Retorna outro objeto Sequencia, com a sequência resultado da transcrição (DNA para RNA).
        Substitui 'T' por 'U'.
        """
        rna_seq = self.sequencia.replace('T', 'U')
        return Sequencia(rna_seq)

    def traduzir(self, parar=False):
        """
        Retorna uma string com a tradução da sequência para uma proteína.
        - Usa DNA_PARA_AMINOACIDO para mapear códons.
        - Se 'parar' for True, a tradução interrompe no primeiro códon de parada (*).
        - Se 'parar' for False, a tradução continua, marcando os códons de parada como '*'.
        - Códons não encontrados no dicionário (bases indefinidas) são marcados como 'X'.
        """
        proteina = ""
        # Percorre a sequência em trincas (códons)
        # O len(self.sequencia) - len(self.sequencia) % 3 garante que a iteração pare em um múltiplo de 3
        for i in range(0, len(self.sequencia) - len(self.sequencia) % 3, 3):
            codon = self.sequencia[i:i+3]

            # Mapeia o códon para um aminoácido ou 'X' se for desconhecido
            # Já trata o stop codon como '*' pelo DNA_PARA_AMINOACIDO
            aminoacido = DNA_PARA_AMINOACIDO.get(codon, 'X')

            # Verifica a condição de parada
            if parar and aminoacido == '*':
                break # Para a tradução se 'parar' for True e for um códon de parada

            # Adiciona o aminoácido (ou 'X', ou '*') à proteína
            proteina += aminoacido
        return proteina

    def calcular_percentual(self, bases):
        """
        Calcula o percentual (proporção de 0 a 1) das bases especificadas na composição da Sequencia.
        Ex: Sequencia("ATCGAAA").calcular_percentual(bases=["A"]) = 0.5
        """
        total = len(self.sequencia)
        if total == 0:
            return 0.0 # Evita divisão por zero para sequências vazias

        # Garante que 'bases' seja uma lista, e que as bases estejam em maiúsculas para comparação
        if isinstance(bases, str):
            bases = [bases]
        bases_upper = [b.upper() for b in bases]

        # Conta a ocorrência das bases especificadas na sequência
        count = sum(self.sequencia.count(base_to_count) for base_to_count in bases_upper)

        # Retorna a proporção (não o percentual multiplicado por 100)
        return count / total
