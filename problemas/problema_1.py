"""
# Problema 1: Análise de Composição de Nucleotídeos
Tarefa: Escreva um script que:

Faça o parse do arquivo multiFASTA, usando a função ler_fasta.
Imprima o percentual de cada nucleotídeo (A, T, C, G) e o conteúdo GC (percentual de C + G) para cada sequência.
Dica: Use sua classe Sequencia e sua função .calcular_percentual(bases)
"""

import sys
import os

# Ajusta o caminho do sistema para que o Python possa encontrar o pacote 'bio'
# Isso é necessário porque problema_1.py está dentro de 'problemas/' e 'bio/' está no diretório pai
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa a função ler_fasta do seu pacote 'bio'
from bio.ler_fasta import ler_fasta

def analisar_composicao(caminho_arquivo_fasta):
    """
    Realiza a análise de composição de nucleotídeos (A, T, C, G e GC-content)
    para cada sequência em um arquivo FASTA e imprime os resultados.
    """
    print(f"--- Análise de Composição para o arquivo: {caminho_arquivo_fasta} ---")

    # 1) Faz o parse do arquivo multiFASTA, usando a função ler_fasta.
    organismos = ler_fasta(caminho_arquivo_fasta)

    if not organismos:
        print("Nenhuma sequência encontrada ou arquivo não existe ou está vazio.")
        return

    # 2) Imprime o percentual de cada nucleotídeo (A, T, C, G) e o conteúdo GC
    # para cada sequência.
    for org in organismos:
        print(f"\nID: {org.id}")
        print(f"Nome: {org.nome}")

        # Como OrganismoFasta.calcular_percentual já delega para Sequencia.calcular_percentual,
        # e Sequencia.calcular_percentual retorna um float entre 0 e 1,
        # multiplicamos por 100 aqui para a exibição em percentual.
        percent_A = org.calcular_percentual(bases=["A"]) * 100
        percent_T = org.calcular_percentual(bases=["T"]) * 100
        percent_C = org.calcular_percentual(bases=["C"]) * 100
        percent_G = org.calcular_percentual(bases=["G"]) * 100

        # Calcula o conteúdo GC (Guanina + Citosina)
        gc_content = org.calcular_percentual(bases=["G", "C"]) * 100

        print(f"  Percentual de A: {percent_A:.2f}%")
        print(f"  Percentual de T: {percent_T:.2f}%")
        print(f"  Percentual de C: {percent_C:.2f}%")
        print(f"  Percentual de G: {percent_G:.2f}%")
        print(f"  Conteúdo GC: {gc_content:.2f}%")
        print("-" * 40) # Linha separadora para melhor legibilidade

if __name__ == "__main__":
    # Define o caminho para o arquivo FASTA.
    # Assumimos que 'Flaviviridae-genomes.fasta' está na pasta 'arquivos'.
    fasta_file_path = os.path.join(os.path.dirname(__file__), '..', 'arquivos', 'Flaviviridae-genomes.fasta')

    analisar_composicao(fasta_file_path)
