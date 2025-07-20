"""
# Problema 1: Análise de Composição de Nucleotídeos
Tarefa: Escreva um script que:

Faça o parse do arquivo multiFASTA, usando a função ler_fasta.
Imprima o percentual de cada nucleotídeo (A, T, C, G) e o conteúdo GC (percentual de C + G) para cada sequência.
Dica: Use sua classe Sequencia e sua função .calcular_percentual(bases)
"""
from bio.ler_fasta import ler_fasta

def main():
    sequencias = ler_fasta("./arquivos/Flaviviridae-genomes.fasta")

    for org in sequencias:
        a = org.calcular_percentual("A")
        t = org.calcular_percentual("T")
        c = org.calcular_percentual("C")
        g = org.calcular_percentual("G")
      
        gc = org.calcular_percentual(["G", "C"])

        print(f"> {org}")
      
        print(f"A: {a:.2f}%")
        print(f"T: {t:.2f}%")
        print(f"C: {c:.2f}%")
        print(f"G: {g:.2f}%\n")
        
        print(f"GC Content: {gc:.2f}%\n")

if __name__ == "__main__":
    main()
