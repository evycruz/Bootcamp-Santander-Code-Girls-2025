# Serviços AWS e suas descrições
servicos = {
    "Amazon EC2": "Serviço de máquinas virtuais sob demanda",
    "Amazon S3": "Armazenamento de objetos na nuvem",
    "AWS Lambda": "Executa código sem gerenciar servidores",
    "Amazon Machine Image": "Modelo de instância EC2 pré-configurado"
}

# Lê a entrada do usuário (STDIN)
entrada = input()

# Imprime a descrição correspondente (STDOUT)
if entrada in servicos:
    print(servicos[entrada])
else:
    print("Serviço não encontrado")
