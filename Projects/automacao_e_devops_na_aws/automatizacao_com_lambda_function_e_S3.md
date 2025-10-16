# Automatizações com AWS Lambda e Amazon S3

O **AWS Lambda** e o **Amazon S3** permitem criar **automatizações baseadas em eventos** de forma simples e escalável. Essa integração é ideal para **processamento de arquivos, backup, ETL e acionamento de workflows** sem necessidade de servidores dedicados.

---

## Como Funciona

1. **Evento no S3:**  
   - O S3 dispara eventos quando um arquivo é criado, modificado ou removido em um bucket.  
   - Exemplos: `s3:ObjectCreated:*`, `s3:ObjectRemoved:*`.

2. **Função Lambda:**  
   - Executa **código automaticamente** em resposta ao evento.  
   - Pode processar o arquivo, gerar thumbnails, mover dados para outro bucket ou acionar outros serviços AWS.  

3. **Integração com outros serviços:**  
   - Lambda pode enviar dados para **DynamoDB**, **SQS**, **SNS** ou iniciar fluxos no **Step Functions**.  

---

## Exemplo de Fluxo Automático

1. Usuário faz upload de arquivo no bucket S3.  
2. Evento `ObjectCreated` aciona uma função Lambda.  
3. Lambda processa o arquivo (por exemplo, redimensiona imagens).  
4. Resultado é salvo em outro bucket S3 ou enviado para análise.  

```python
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Exemplo simples: copiar arquivo para outro bucket
    s3_client.copy_object(
        Bucket='bucket-destino',
        Key=key,
        CopySource={'Bucket': bucket_name, 'Key': key}
    )
    return f'Arquivo {key} processado com sucesso!'
```
# Benefícios da Automação Lambda + S3

O uso de **AWS Lambda** em conjunto com **Amazon S3** permite criar **automatizações baseadas em eventos**, aumentando a eficiência e reduzindo a necessidade de intervenção manual.

---

## Benefícios

- **Automação completa:** Processamento de arquivos sem intervenção manual.  
- **Escalabilidade:** Lambda ajusta automaticamente recursos conforme a demanda.  
- **Segurança:** Controle de acesso via políticas de **IAM** e **buckets S3**.  
- **Monitoramento:** Integração com **CloudWatch** para logs e métricas.  
- **Custo eficiente:** Paga-se apenas pelo tempo de execução da função Lambda.

---

## Referências

- [AWS Lambda – Documentação Oficial](https://docs.aws.amazon.com/lambda/)  
- [Amazon S3 – Documentação Oficial](https://docs.aws.amazon.com/s3/)  
- [Event-Driven Automation com Lambda e S3](https://aws.amazon.com/blogs/compute/automating-s3-tasks-with-lambda/)
