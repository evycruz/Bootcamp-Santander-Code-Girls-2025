# Conceitos Lambda e suas descrições
lambda_conceitos = {
    "Lambda Function": "Função executada automaticamente na AWS",
    "Trigger": "Evento que dispara uma execução Lambda",
    "Runtime": "Ambiente de execução da função",
    "Execution Role": "Permissões para a função acessar serviços"
}

# Lê a entrada do usuário (STDIN)
entrada = input()

# Imprime a descrição correspondente (STDOUT)
if entrada in lambda_conceitos:
    print(lambda_conceitos[entrada])
else:
    print("Conceito não encontrado")
