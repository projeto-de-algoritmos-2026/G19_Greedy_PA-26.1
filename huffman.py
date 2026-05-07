import heapq

class No:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.esq = None
        self.dir = None

    def __lt__(self, other):
        return self.freq < other.freq #comparar frequência de nós


def Huffman(text):
    freq = {}

    #para contar a frequência de um caractere 
    for letra in text:
        freq[letra] = freq.get(letra, 0) + 1

    # criar heap
    heap = []
    #heappush insere o nó (incluindo inserção com shift_up())
    #heappop retira o nó da raiz (incluindo remoção com heapify())   
    for caractere, frequencia in freq.items():
        heapq.heappush(heap, No(caractere, frequencia))
    

    # construir árvore
    while len(heap) > 1:
        esq = heapq.heappop(heap)
        dir = heapq.heappop(heap)

        juntar_no = No(None, esq.freq + dir.freq)
        juntar_no.esq = esq
        juntar_no.dir = dir

        heapq.heappush(heap, juntar_no)

    return heap[0]