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
