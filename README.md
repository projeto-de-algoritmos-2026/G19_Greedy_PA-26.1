# G19_Greedy_PA-26.1

Número da Lista: 19  
Conteúdo da Disciplina: Algoritmos Ambiciosos (greedy)

---

## Alunos

| Matrícula | Aluno |
|-----------|--------|
| 231033737 | Artur Mendonça Arruda|
| 231035464 | Lucas Mendonça Arruda |

---

## Sobre

Este projeto tem como objetivo usar o algoritmo de huffman em sequências de DNA de vírus, extraídas em tempo real da base de dados do NCBI.
O uso do algoritmo de Huffman foca na redução do tamanho dos dados através da análise de códons, que são trios de bases nitrogenadas que funcionam como unidades de informação genética. Como o DNA possui padrões de repetição desses códons, o algoritmo atribui códigos menores para as sequências de maior frequência. Isso diminui o volume de dados para armazenamento e transmissão, além de auxiliar na identificação de instruções genéticas que são mais recorrentes na replicação viral. 

## Importância do Algoritmo

A compressão de DNA baseada em bases nitrogenadas isoladas (A, T, C, G) apresenta baixo rendimento, uma vez que possui apenas 4 bases limitando a capacidade do algoritmo de reduzir o tamanho dos bits.

O diferencial ocorre ao agrupar o DNA em códons. Ao expandir as possibilidades de 4 para 64 combinações, o padrão de repetição torna-se muito mais evidente. O algoritmo de Huffman utiliza essa variação para gerar um dicionário otimizado, atribuindo códigos binários curtos para sequências recorrentes e códigos longos para códons mais raras.

Esta redução no tamanho dos dados possui aplicações diretas na bioinformática:

* **Logística de Dados:** Sequências genéticas comprimidas ocupam menos espaço em servidores e permitem a transmissão mais rápidas entre instituições de pesquisa.
* **Desempenho Computacional:** Arquivos com menor densidade de bits exigem menos memória RAM e tempo de CPU.
* **Identificação de Padrões:** O processo de compressão organiza a informação de forma a destacar as instruções genéticas mais utilizadas pelo vírus para sua replicação.



## Funcionamento

Ao executar o programa, o sistema realiza as seguintes etapas:

1. **Busca Automatizada:** O script acessa a API do NCBI e baixa a sequência de DNA utilizando o accession number fornecido.
2. **Mapeamento de Códons:** A sequência é segmentada em K-mers de tamanho 3 (códons) para análise de frequência.
3. **Geração da Árvore:** O algoritmo de Huffman cria uma árvore binária onde os códons mais frequentes ficam posicionados mais próximos da raiz. Isso garante que eles recebam os caminhos mais curtos, precisando menos bits para representar, enquanto os códons raros descem para os níveis mais profundos representand (mais bits).
4. **Relatório de Saída:** O programa exibe a comparação de tamanho entre o formato original (2 bits por base) e o formato comprimido, calculando a taxa de compressão e listando os códons mais frequentes.


## Vídeo

[Link Vídeo]()


## Screenshots


![Código do Huffman](/assets/huffman.png)


![Código da Heap](/assets/heap.png)


![Interface do sistema](/assets/tela.png)

O terminal exibe o resultado do processamento de cada segmento do vírus:

* **ID:** Registro oficial do DNA no banco de dados (NCBI).
* **FIXO:** O tamanho padrão do DNA sem compressão
* **HUFFMAN:** O novo tamanho após a compressão.
* **Taxa de compressão (%):** Quanto espaço foi economizado.
* **Top:** Os 3 códons mais comuns e seus novos códigos reduzidos.

## Instalação

Linguagem: Python  

Pré-requisitos:
- Python 3.x
- pip

```bash
pip install requests
```

ou para ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate
venv\Scripts\activate
pip3 pip install requests
```
## Uso

Após instalar as dependências, execute:

```bash
python src/main.py
```

## Histórico de versão

| Versão | Data | Descrição | Autor | Revisor | Revisão |
|-----------|---------|--------------|----------|------------|------------|
| `v1.0` | 11/05/2026 | Estruturação inicial da README | [Artur Mendonça](https://github.com/ArtyMend07) e [Lucas Mendonça](https://github.com/lucasarruda9)| | |
