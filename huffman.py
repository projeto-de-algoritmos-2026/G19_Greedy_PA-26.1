class No:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.esq = None
        self.dir = None

    def __lt__(self, other):
        return self.freq < other.freq #comparar frequência de nós

# insere e faz shift up
def push_heap(heap, no):
    heap.append(no)
    idx = len(heap) - 1
    while idx > 0:
        pai = (idx - 1) // 2
        if heap[idx] < heap[pai]:
            heap[idx], heap[pai] = heap[pai], heap[idx]
            idx = pai
        else:
            break

# remove a raiz faz heapify
def pop_heap(heap):
    if len(heap) == 1:
        return heap.pop()
    raiz = heap[0]
    heap[0] = heap.pop()
    idx = 0
    while True:
        esq = 2 * idx + 1
        dir = 2 * idx + 2
        menor = idx
        if esq < len(heap) and heap[esq] < heap[menor]: menor = esq
        if dir < len(heap) and heap[dir] < heap[menor]: menor = dir
        if menor != idx:
            heap[idx], heap[menor] = heap[menor], heap[idx]
            idx = menor
        else: break
    return raiz

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
        push_heap(heap, No(caractere, frequencia))

    # construir árvore
    while len(heap) > 1:
        esq = pop_heap(heap)
        dir = pop_heap(heap)

        juntar_no = No(None, esq.freq + dir.freq)
        juntar_no.esq = esq
        juntar_no.dir = dir

        push_heap(heap, juntar_no)

    return heap[0]