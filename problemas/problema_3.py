"""
# Problema 3: Identificação de Mutação em Genomas Virais
Contexto
Você está colaborando com uma equipe de virologistas que está estudando mutações específicas em genomas de vírus da família Flaviviridae.
Eles identificaram uma mutação de interesse que ocorre na posição 1000 das sequências, onde o nucleotídeo 'A' é substituído por 'G'.
Seu trabalho é identificar se essa mutação está presente nas sequências fornecidas e gerar um relatório.
Esta análise é crucial para entender a evolução dos vírus e suas possíveis implicações na virulência e resistência a tratamentos.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bio.ler_fasta import ler_fasta

def identificar_mutacao(caminho_arquivo_fasta, posicao_mutacao, nucleotideo_esperado_origem, nucleotideo_mutado_alvo):

    print(f"--- Relatório de Mutação na Posição {posicao_mutacao} ({nucleotideo_esperado_origem} -> {nucleotideo_mutado_alvo}) ---")
    print(f"Arquivo analisado: {caminho_arquivo_fasta}")

    organismos = ler_fasta(caminho_arquivo_fasta)

    if not organismos:
        print("Nenhuma sequência encontrada ou arquivo não existe ou está vazio.")
        return

    relatorio = [] 

    indice_mutacao = posicao_mutacao - 1

    for org in organismos:
        seq_str = org.sequencia.sequencia 
        mutacao_presente = False
        detalhe_verificacao = ""

        if len(seq_str) > indice_mutacao:
            base_na_posicao_atual = seq_str[indice_mutacao].upper()

            if base_na_posicao_atual == nucleotideo_mutado_alvo.upper():
                mutacao_presente = True
                detalhe_verificacao = f"Base na posição {posicao_mutacao}: '{base_na_posicao_atual}'. Mutaçāo ({nucleotideo_esperado_origem} -> {nucleotideo_mutado_alvo}) detectada."
            else:
                detalhe_verificacao = f"Base na posição {posicao_mutacao}: '{base_na_posicao_atual}'. Mutaçāo ({nucleotideo_esperado_origem} -> {nucleotideo_mutado_alvo}) NÃO detectada."
        else:
            detalhe_verificacao = f"Sequência muito curta (tamanho: {len(seq_str)}) para verificar a posição {posicao_mutacao}."

        relatorio.append({
            "id": org.id,
            "nome": org.nome,
            "mutacao_presente": mutacao_presente,
            "detalhe": detalhe_verificacao
        })

    print("\n--- Sumário do Relatório ---")
    for entry in relatorio:
        status_texto = "POSSUI A MUTAÇÃO" if entry["mutacao_presente"] else "NÃO POSSUI A MUTAÇÃO"
        print(f"\nID: {entry['id']}")
        print(f"Nome: {entry['nome']}")
        print(f"  Status: {status_texto}")
        print(f"  Detalhe: {entry['detalhe']}")
        print("-" * 40)

if __name__ == "__main__":
    fasta_file_path = os.path.join(os.path.dirname(__file__), '..', 'arquivos', 'Flaviviridae-genomes.fasta')

    posicao_alvo = 1000
    nucleotideo_origem_esperado = 'A'
    nucleotideo_mutado_encontrado = 'G'

    identificar_mutacao(fasta_file_path, posicao_alvo, nucleotideo_origem_esperado, nucleotideo_mutado_encontrado)
