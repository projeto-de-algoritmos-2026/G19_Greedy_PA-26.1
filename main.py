from ncbi_api import get_dna_sequence
from huffman import Huffman, gerar_codigos
from collections import Counter

def processar_virus(nome, accession):
    print(f"\n--- Processando {nome} ({accession}) ---")
    dna = get_dna_sequence(accession)
    
    if not dna:
        print("Falha ao obter sequência.")
        return

    # Dividir em K-mers de tamanho 3 (Códons)
    codons = [dna[i:i+3] for i in range(0, len(dna) - 2, 3)]
    
    # Calcular frequências dos códons
    frequencias = Counter(codons)
    
    # Criar árvore de Huffman
    raiz = Huffman(codons)
    
    # Gerar dicionário de códigos
    tabela_codigos = gerar_codigos(raiz)
    
    # Cálculo de compressão
    total_bits_huffman = sum(frequencias[c] * len(tabela_codigos[c]) for c in frequencias)
    total_bits_original = len(dna) * 2 # Assumindo 2 bits por base (A, C, T, G)
    
    taxa = (1 - (total_bits_huffman / total_bits_original)) * 100

    print(f"Tamanho original (2 bits/base): {total_bits_original} bits")
    print(f"Tamanho comprimido (Huffman):   {total_bits_huffman} bits")
    print(f"Taxa de compressão:             {taxa:.2f}%")
    
    # Top 3 códons mais frequentes
    print("\nTop 3 Códons:")
    for codon, freq in frequencias.most_common(3):
        print(f"  {codon}: {freq} ocorrências (Código: {tabela_codigos[codon]})")

if __name__ == "__main__":
    segmentos = [
        ("Andes virus - Segmento S", "NC_003466"),
        ("Andes virus - Segmento M", "NC_003467"),
        ("Andes virus - Segmento L", "NC_003468")
    ]
    
    for nome, acc in segmentos:
        processar_virus(nome, acc)
