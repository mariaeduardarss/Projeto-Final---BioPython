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

# Ajusta o caminho do sistema para que o Python possa encontrar o pacote 'bio'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa a função ler_fasta do seu pacote 'bio'
from bio.ler_fasta import ler_fasta

def traduzir_fasta(caminho_arquivo_fasta):
    """
    Faz o parse de um arquivo FASTA, traduz cada sequência de nucleotídeos
    para proteína e imprime as sequências de proteínas resultantes.
    """
    print(f"--- Tradução de Sequências para o arquivo: {caminho_arquivo_fasta} ---")

    # 1) Faz o parse do arquivo multiFASTA.
    organismos = ler_fasta(caminho_arquivo_fasta)

    if not organismos:
        print("Nenhuma sequência encontrada ou arquivo não existe ou está vazio.")
        return

    # 2) Traduz cada sequência de nucleotídeos para sua sequência de proteína correspondente.
    # 3) Imprime as sequências de proteínas.
    for org in organismos:
        print(f"\nID: {org.id}")
        print(f"Nome: {org.nome}")

        # A sequência dentro do objeto OrganismoFasta já é um objeto Sequencia.
        # Chama o método .traduzir() do objeto Sequencia.
        # Por padrão, vamos usar parar=True, o que significa que a tradução para no primeiro stop códon.
        # Se quiser que continue e marque '*', mude para parar=False.
        proteina = org.sequencia.traduzir(parar=True)
        print(f"  Sequência de Proteína (parada no stop códon): {proteina}")
        
        # Imprimir a versão que continua após o stop códon
        proteina_completa = org.sequencia.traduzir(parar=False)
        print(f"  Sequência de Proteína (completa c/ '*'): {proteina_completa}")

        print("-" * 40) # Linha separadora para melhor legibilidade

if __name__ == "__main__":
    # Define o caminho para o arquivo FASTA.
    fasta_file_path = os.path.join(os.path.dirname(__file__), '..', 'arquivos', 'Flaviviridae-genomes.fasta')

    traduzir_fasta(fasta_file_path)
