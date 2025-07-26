import sys
import os

from problemas.problema_1 import problema_1
from problemas.problema_2 import problema_2
from problemas.problema_3 import problema_3

caminho_do_arquivo = "arquivos/Flaviviridae-genomes.fasta"

def run_all_problems():
    print("===========================================")
    print("   Iniciando Projeto Final - BioPython    ")
    print("===========================================\n")

    fasta_file_path = os.path.join(os.path.dirname(__file__), 'arquivos', 'Flaviviridae-genomes.fasta')
    
    # --- Executa o Problema 1 ---
    print("\n-------------------------------------------")
    print("           Executando Problema 1           ")
    print("     Análise de Composição de Nucleotídeos")
    print("-------------------------------------------")
    problema_1.analisar_composicao(fasta_file_path)

    # --- Executa o Problema 2 ---
    print("\n-------------------------------------------")
    print("           Executando Problema 2           ")
    print("    Tradução de Sequências para Proteínas  ")
    print("-------------------------------------------")
    problema_2.traduzir_fasta(fasta_file_path)

    # --- Executa o Problema 3 ---
    print("\n-------------------------------------------")
    print("           Executando Problema 3           ")
    print("   Identificação de Mutação em Genomas Virais")
    print("-------------------------------------------")
    # Para o problema 3, defina os parâmetros específicos da mutação
    posicao_mutacao = 1000
    nucleotideo_esperado_origem = 'A'
    nucleotideo_mutado_alvo = 'G'
    problema_3.identificar_mutacao(fasta_file_path, posicao_mutacao, nucleotideo_esperado_origem, nucleotideo_mutado_alvo)

    print("\n===========================================")
    print("   Execução de todos os Problemas Concluída")
    print("===========================================\n")

def main_menu():
    """
    Exibe um menu para o usuário escolher qual problema executar.
    """
    fasta_file_path = os.path.join(os.path.dirname(__file__), 'arquivos', 'Flaviviridae-genomes.fasta')

    while True:
        print("\n===========================================")
        print("           Menu do Projeto BioPython       ")
        print("===========================================")
        print("1. Executar Problema 1 (Composição de Nucleotídeos)")
        print("2. Executar Problema 2 (Tradução para Proteínas)")
        print("3. Executar Problema 3 (Identificação de Mutação)")
        print("4. Executar TODOS os Problemas")
        print("0. Sair")
        print("-------------------------------------------")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            print("\n>>> Executando Problema 1...")
            problema_1.analisar_composicao(fasta_file_path)
        elif choice == '2':
            print("\n>>> Executando Problema 2...")
            problema_2.traduzir_fasta(fasta_file_path)
        elif choice == '3':
            print("\n>>> Executando Problema 3...")
            posicao_mutacao = 1000
            nucleotideo_esperado_origem = 'A'
            nucleotideo_mutado_alvo = 'G'
            problema_3.identificar_mutacao(fasta_file_path, posicao_mutacao, nucleotideo_esperado_origem, nucleotideo_mutado_alvo)
        elif choice == '4':
            run_all_problems()
        elif choice == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número entre 0 e 4.")

if __name__ == "__main__":
    main_menu()
