"""
# Problema 2: Tradução de Sequências de Nucleotídeos para Sequências de Proteínas
Objetivo: Traduzir sequências de nucleotídeos para sequências de proteínas.

Tarefa: Escreva um script em Python para:

Fazer o parse do arquivo multiFASTA.
Traduzir cada sequência de nucleotídeos para sua sequência de proteína correspondente.
Imprimir as sequências de proteínas.
Dica: Use sua classe Sequencia e sua função de traduzir
"""

from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia

def traduzir_sequencias_em_proteinas(caminho):
    organismos = ler_fasta(caminho)
    
    for organismo in organismos:
        sequencia_obj = Sequencia(organismo.sequencia)
        sequencia_proteina = sequencia_obj.traduzir()
        print(f'ID: {organismo.id}')
        print(f'Nome: {organismo.nome}')
        print(f'Sequencia de Proteinas: {sequencia_proteina}\n')
        print('\n--------------------------------------------------------\n')

arquivo_fasta = './arquivos/Flaviviridae-genomes.fasta'
traduzir_sequencias_em_proteinas(arquivo_fasta)
