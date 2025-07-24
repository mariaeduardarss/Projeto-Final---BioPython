"""
# Problema 1: Análise de Composição de Nucleotídeos
Tarefa: Escreva um script que:

Faça o parse do arquivo multiFASTA, usando a função ler_fasta.
Imprima o percentual de cada nucleotídeo (A, T, C, G) e o conteúdo GC (percentual de C + G) para cada sequência.
Dica: Use sua classe Sequencia e sua função .calcular_percentual(bases)
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bio.ler_fasta import ler_fasta

def analisar_composicao(caminho_arquivo_fasta):
    print(f"--- Análise de Composição para o arquivo: {caminho_arquivo_fasta} ---")

    organismos = ler_fasta(caminho_arquivo_fasta)

    if not organismos:
        print("Nenhuma sequência encontrada ou arquivo não existe ou está vazio.")
        return

    for org in organismos:
        print(f"\nID: {org.id}")
        print(f"Nome: {org.nome}")

        percent_A = org.calcular_percentual(bases=["A"]) * 100
        percent_T = org.calcular_percentual(bases=["T"]) * 100
        percent_C = org.calcular_percentual(bases=["C"]) * 100
        percent_G = org.calcular_percentual(bases=["G"]) * 100

        gc_content = org.calcular_percentual(bases=["G", "C"]) * 100

        print(f"  Percentual de A: {percent_A:.2f}%")
        print(f"  Percentual de T: {percent_T:.2f}%")
        print(f"  Percentual de C: {percent_C:.2f}%")
        print(f"  Percentual de G: {percent_G:.2f}%")
        print(f"  Conteúdo GC: {gc_content:.2f}%")
        print("-" * 40) 

if __name__ == "__main__":
   
    fasta_file_path = os.path.join(os.path.dirname(__file__), '..', 'arquivos', 'Flaviviridae-genomes.fasta')

    analisar_composicao(fasta_file_path)
