# Conceitos AWS e suas descrições
conceitos = {
    "Lifecycle Policy": "Regras para mover ou excluir arquivos",
    "Cross-Region Replication": "Replica objetos S3 em outra região",
    "Cache Behavior": "Define como o CloudFront armazena conteúdo",
    "Storage Class": "Define o tipo de armazenamento no S3"
}

# Lê a entrada do usuário (STDIN)
entrada = input()

# Imprime a descrição correspondente (STDOUT)
if entrada in conceitos:
    print(conceitos[entrada])
else:
    print("Conceito não encontrado")
