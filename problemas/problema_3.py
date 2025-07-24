from bio.ler_fasta import ler_fasta

def verificar_mutacao(sequencia: str, posicao: int, original: str, mutado: str) -> bool:
    if len(sequencia) < posicao:
        return False  # Sequência muito curta, posição não existe

    # Verifica se o nucleotídeo na posição (posicao - 1, pois índice começa em 0)
    # é igual ao nucleotídeo mutado, comparando sem diferenciar maiúsculas/minúsculas
    return sequencia[posicao - 1].upper() == mutado.upper()

def main():
    caminho = 'exemplo.fasta'          # Caminho do arquivo FASTA a ser lido
    posicao = 1000                     # Posição que será verificada na sequência
    nucleotideo_original = 'A'         # Nucleotídeo esperado originalmente na posição
    nucleotideo_mutado = 'G'           # Nucleotídeo que indica mutação na posição

    organismos = ler_fasta(caminho)

    print("Relatório de Mutação (posição 1000 - A → G):\n")
    # Para cada organismo, verifica se possui a mutação e imprime o resultado
    for org in organismos:
        seq = str(org.sequencia)       # Converte a sequência para string para facilitar a manipulação
        if verificar_mutacao(seq, posicao, nucleotideo_original, nucleotideo_mutado):
            print(f'>{org.id, org.nome}: Possui mutação')
        else:
            print(f'>{org.id, org.nome}: Não possui mutação')

if __name__ == '__main__':
    main()
