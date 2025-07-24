"""
# Problema 2: Tradução de Sequências de Nucleotídeos para Sequências de Proteínas
Objetivo: Traduzir sequências de nucleotídeos para sequências de proteínas.

Tarefa: Escreva um script em Python para:

Fazer o parse do arquivo multiFASTA.
Traduzir cada sequência de nucleotídeos para sua sequência de proteína correspondente.
Imprimir as sequências de proteínas.
Dica: Use sua classe Sequencia e sua função de traduzir
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bio.ler_fasta import ler_fasta

def traduzir_fasta(caminho_arquivo_fasta):
    print(f"--- Tradução de Sequências para o arquivo: {caminho_arquivo_fasta} ---")

    organismos = ler_fasta(caminho_arquivo_fasta)

    if not organismos:
        print("Nenhuma sequência encontrada ou arquivo não existe ou está vazio.")
        return

    for org in organismos:
        print(f"\nID: {org.id}")
        print(f"Nome: {org.nome}")

        proteina = org.sequencia.traduzir(parar=True)
        print(f"  Sequência de Proteína (parada no stop códon): {proteina}")
        
        proteina_completa = org.sequencia.traduzir(parar=False)
        print(f"  Sequência de Proteína (completa c/ '*'): {proteina_completa}")

        print("-" * 40) 

if __name__ == "__main__":
    fasta_file_path = os.path.join(os.path.dirname(__file__), '..', 'arquivos', 'Flaviviridae-genomes.fasta')

    traduzir_fasta(fasta_file_path)
