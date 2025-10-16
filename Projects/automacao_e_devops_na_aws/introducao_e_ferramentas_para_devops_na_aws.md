# DevOps na AWS

O **DevOps** é uma abordagem que integra **desenvolvimento (Dev)** e **operações (Ops)** para aumentar a **agilidade, automação e confiabilidade** de sistemas. Na AWS, diversas ferramentas e serviços permitem implementar práticas DevOps de forma eficiente e escalável.

---

## Principais Conceitos

- **Integração Contínua (CI):** Automatiza a construção e testes de código sempre que há mudanças.  
- **Entrega Contínua / Deploy Contínuo (CD):** Automatiza a entrega de aplicações em diferentes ambientes.  
- **Infraestrutura como Código (IaC):** Permite definir recursos de infraestrutura via arquivos de configuração, garantindo reprodutibilidade e versionamento.  
- **Monitoramento e Observabilidade:** Captura métricas, logs e eventos para análise e resolução de problemas.  

---

## Ferramentas AWS para DevOps

### 1. **AWS CodeCommit**
- Repositório Git totalmente gerenciado para armazenar código fonte de forma segura.

### 2. **AWS CodeBuild**
- Serviço de **build e teste contínuo** que compila código e gera artefatos automaticamente.

### 3. **AWS CodePipeline**
- Orquestra o fluxo de CI/CD, integrando CodeCommit, CodeBuild, CodeDeploy e outros serviços.

### 4. **AWS CodeDeploy**
- Automatiza o **deploy de aplicações** em instâncias EC2, Lambda ou servidores on-premises.

### 5. **AWS CloudFormation**
- Permite criar e gerenciar infraestrutura de forma **automatizada e declarativa** usando templates.

### 6. **AWS CloudWatch**
- Monitoramento em tempo real de logs, métricas e eventos para aplicações e infraestrutura.

### 7. **AWS Systems Manager**
- Gestão e automação de operações em servidores e recursos AWS, incluindo execução de scripts e patches.

---

## Benefícios do DevOps na AWS

- **Agilidade:** Reduz o tempo entre desenvolvimento e entrega em produção.  
- **Automação:** Menos tarefas manuais, maior consistência e confiabilidade.  
- **Segurança:** Controle de acesso granular via IAM, integração com auditoria e logs.  
- **Escalabilidade:** Gerencia pipelines e infraestrutura complexa em grande escala.  
- **Visibilidade:** Monitoramento centralizado e métricas detalhadas de performance.

---

## Referências

- [AWS DevOps – Documentação Oficial](https://aws.amazon.com/devops/)  
- [CI/CD na AWS – Guia de Boas Práticas](https://docs.aws.amazon.com/codepipeline/)  
- [Infraestrutura como Código com CloudFormation](https://docs.aws.amazon.com/cloudformation/)
