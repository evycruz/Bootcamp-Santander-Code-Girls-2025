# Serviços AWS e suas descrições
servicos = {
    "Amazon S3 Versioning": "Controle de versões de objetos no S3",
    "Amazon CloudFront": "CDN para entrega rápida de conteúdo",
    "Amazon Glacier": "Arquivamento de longo prazo com baixo custo",
    "Amazon S3": "Armazenamento de objetos na nuvem"
}

# Lê a entrada do usuário (STDIN)
entrada = input()

# Imprime a descrição correspondente (STDOUT)
if entrada in servicos:
    print(servicos[entrada])
else:
    print("Serviço não encontrado")
