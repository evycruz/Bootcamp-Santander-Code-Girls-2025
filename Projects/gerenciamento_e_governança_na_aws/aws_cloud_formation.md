# AWS CloudFormation

O **AWS CloudFormation** é um serviço que permite **criar, configurar e gerenciar infraestrutura como código (IaC)** na AWS.  
Com ele, é possível **provisionar recursos automaticamente**, como instâncias EC2, VPCs, buckets S3 e bancos de dados de forma **segura, padronizada e reproduzível**.

---

## O que é o AWS CloudFormation?

O **CloudFormation** utiliza **modelos declarativos (templates)** escritos em **YAML ou JSON** para descrever toda a infraestrutura desejada.  
Esses modelos informam à AWS quais recursos criar e como configurá-los, e o serviço se encarrega de **montar, atualizar e excluir** tudo automaticamente.

Em outras palavras, é como ter um **“roteiro” que constrói sua infraestrutura em minutos**, sem necessidade de cliques manuais no console.

---

## Principais Componentes

- **Template:** arquivo YAML ou JSON que descreve os recursos (ex: EC2, S3, IAM, etc).  
- **Stack:** conjunto de recursos criados a partir de um template (uma implantação da infraestrutura).  
- **Change Set:** mostra as alterações que serão aplicadas antes de atualizar um stack.  
- **StackSet:** permite implantar um mesmo template em múltiplas contas e regiões AWS.  
- **Parameters & Outputs:** entrada e saída de valores dinâmicos, facilitando a personalização dos templates.

---

## Benefícios

- **Infraestrutura como Código (IaC):** facilita versionamento, auditoria e automação da infraestrutura.  
- **Reprodutibilidade:** implante o mesmo ambiente (ex: dev, staging, produção) com consistência.  
- **Automação completa:** elimina a necessidade de configurações manuais.  
- **Gerenciamento de ciclo de vida:** atualize, modifique e exclua stacks de forma controlada.  
- **Integração com IAM:** controle de permissões sobre quem pode criar ou alterar recursos.  
- **Eficiência de custos:** reduz erros humanos e evita desperdício de recursos.

---

## Casos de Uso Comuns

- Criação automatizada de **ambientes de desenvolvimento e produção**.  
- Provisionamento de **infraestrutura completa** para aplicações web.  
- Automação de **pipelines CI/CD** integrando com CodePipeline e CodeBuild.  
- Padronização de ambientes em **grandes organizações** (via StackSets).  
- Auditoria e **controle de mudanças** em ambientes críticos.

---

## Boas Práticas

- Utilize **parâmetros e variáveis** para tornar os templates reutilizáveis.  
- Armazene templates no **AWS S3** ou em **repositórios Git** para versionamento.  
- Combine com o **AWS Config** e o **CloudTrail** para auditoria e conformidade.  
- Teste templates com o comando `aws cloudformation validate-template` antes de implantar.  
- Use **Change Sets** para revisar alterações antes da atualização de um stack.

---

## Exemplo Simplificado de Template (YAML)

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Exemplo simples de criação de uma instância EC2"
Resources:
  MyEC2Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: "t2.micro"
      ImageId: "ami-0abcdef1234567890"
      Tags:
        - Key: "Name"
          Value: "MinhaInstanciaEC2"
