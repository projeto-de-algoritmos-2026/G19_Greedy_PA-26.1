import requests

def get_dna_sequence(accession):
    """
    Busca uma sequência de DNA no banco de dados Nucleotide do NCBI via E-fetch.
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "nuccore",
        "id": accession,
        "rettype": "fasta",
        "retmode": "text"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        # O formato FASTA tem o cabeçalho na primeira linha começando com '>'
        lines = response.text.strip().split('\n')
        # Filtra as linhas que não são cabeçalho e as junta
        sequence = "".join(line.strip() for line in lines if not line.startswith('>'))
        
        return sequence
    except Exception as e:
        print(f"Erro ao buscar sequência {accession}: {e}")
        return None
