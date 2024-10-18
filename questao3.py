import json
import xml.etree.ElementTree as ET

# Função para ler dados JSON
def ler_dados_json(caminho):
    with open(caminho, 'r') as f:
        dados = json.load(f)
    return [dia['valor'] for dia in dados if dia['valor'] > 0]

# Função para ler dados XML
def ler_dados_xml(caminho):
    tree = ET.parse(caminho)
    root = tree.getroot()
    return [float(row.find('valor').text) for row in root if float(row.find('valor').text) > 0]

# Ler os dados dos arquivos
faturamento_json = ler_dados_json('dados.json')
faturamento_xml = ler_dados_xml('dados (2).xml')

# Combinar os dados de ambos os arquivos
faturamentos = faturamento_json + faturamento_xml

# Cálculos
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)
dias_acima_media = sum(1 for valor in faturamentos if valor > media_mensal)

# Exibir resultados
print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
