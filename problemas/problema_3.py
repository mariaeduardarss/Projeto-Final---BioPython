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

# Ajusta o caminho do sistema para que o Python possa encontrar o pacote 'bio'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa a função ler_fasta do seu pacote 'bio'
from bio.ler_fasta import ler_fasta

def identificar_mutacao(caminho_arquivo_fasta, posicao_mutacao, nucleotideo_esperado_origem, nucleotideo_mutado_alvo):
    """
    Verifica a presença de uma mutação específica (substituição de nucleotídeo)
    em uma posição definida em cada sequência e gera um relatório.

    Args:
        caminho_arquivo_fasta (str): Caminho para o arquivo multiFASTA.
        posicao_mutacao (int): Posição (base 1) onde a mutação é esperada.
        nucleotideo_esperado_origem (str): O nucleotídeo que se espera que estivesse originalmente (ex: 'A').
        nucleotideo_mutado_alvo (str): O nucleotídeo que indica a mutação (ex: 'G').

    Nota: Sem uma sequência de referência 'selvagem' para cada genoma,
    assumimos que a mutação está presente se o nucleotídeo na 'posicao_mutacao'
    for igual ao 'nucleotideo_mutado_alvo' e o genoma for longo o suficiente.
    Idealmente, para validar a substituição 'A' por 'G', você precisaria
    saber que a base original naquela posição era 'A'. Aqui, simplesmente
    verificamos se a base na posição é 'G'.
    """
    print(f"--- Relatório de Mutação na Posição {posicao_mutacao} ({nucleotideo_esperado_origem} -> {nucleotideo_mutado_alvo}) ---")
    print(f"Arquivo analisado: {caminho_arquivo_fasta}")

    # 1. Faz o parse do arquivo multiFASTA contendo os genomas virais.
    organismos = ler_fasta(caminho_arquivo_fasta)

    if not organismos:
        print("Nenhuma sequência encontrada ou arquivo não existe ou está vazio.")
        return

    relatorio = [] # Lista para armazenar o status de cada sequência

    # Ajusta a posição para índice baseado em 0 para Python (pos 1000 no README -> índice 999)
    indice_mutacao = posicao_mutacao - 1

    # 2. Verifica se a mutação específica está presente em cada sequência.
    for org in organismos:
        seq_str = org.sequencia.sequencia # Acessa a string da sequência do objeto Sequencia
        mutacao_presente = False
        detalhe_verificacao = ""

        if len(seq_str) > indice_mutacao:
            base_na_posicao_atual = seq_str[indice_mutacao].upper()

            if base_na_posicao_atual == nucleotideo_mutado_alvo.upper():
                # A mutação é considerada presente se o nucleotídeo na posição 1000 for 'G'
                # (Assumindo que esta é a mutação de interesse A->G)
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

    # 3. Gera um relatório que indica quais sequências possuem a mutação e quais não possuem.
    print("\n--- Sumário do Relatório ---")
    for entry in relatorio:
        status_texto = "POSSUI A MUTAÇÃO" if entry["mutacao_presente"] else "NÃO POSSUI A MUTAÇÃO"
        print(f"\nID: {entry['id']}")
        print(f"Nome: {entry['nome']}")
        print(f"  Status: {status_texto}")
        print(f"  Detalhe: {entry['detalhe']}")
        print("-" * 40)

if __name__ == "__main__":
    # Define o caminho para o arquivo FASTA dos genomas virais.
    fasta_file_path = os.path.join(os.path.dirname(__file__), '..', 'arquivos', 'Flaviviridae-genomes.fasta')

    # Define os parâmetros da mutação de interesse
    posicao_alvo = 1000 # Posição 1-based no genoma, como descrito no problema
    nucleotideo_origem_esperado = 'A' # O que *deveria ser* na referência (para fins de descrição da mutação)
    nucleotideo_mutado_encontrado = 'G'   # O que se encontra na sequência mutada

    identificar_mutacao(fasta_file_path, posicao_alvo, nucleotideo_origem_esperado, nucleotideo_mutado_encontrado)
