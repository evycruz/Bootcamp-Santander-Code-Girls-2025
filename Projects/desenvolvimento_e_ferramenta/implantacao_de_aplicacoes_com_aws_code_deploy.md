# Implantação de Aplicações com AWS CodeDeploy

O **AWS CodeDeploy** é um serviço da AWS que automatiza a **implantação de aplicações** em instâncias EC2, servidores on-premises ou serviços de contêiner, garantindo **atualizações consistentes e seguras** sem interrupção do serviço.

---

## Principais Conceitos

- **Deployment Group:** Conjunto de instâncias ou recursos onde a aplicação será implantada.  
- **Application:** Representa a aplicação que será implantada (pode ser web app, serviço backend, etc.).  
- **Deployment Config:** Define como a implantação será realizada (ex.: **AllAtOnce**, **Rolling**, **Blue/Green**).  
- **Revision:** Versão da aplicação a ser implantada, normalmente armazenada no S3 ou GitHub.  

---

## Como Funciona

1. **Preparação:** Configure a aplicação e o arquivo de **AppSpec** (appspec.yml ou appspec.json) que define as etapas da implantação.  
2. **Criação do Deployment Group:** Selecione as instâncias ou recursos de destino.  
3. **Escolha do Deployment Type:**  
   - **In-place Deployment:** Atualiza a aplicação nas mesmas instâncias.  
   - **Blue/Green Deployment:** Cria um novo conjunto de instâncias e faz o switch após validação.  
4. **Execução da Implantação:** CodeDeploy distribui a aplicação automaticamente seguindo o fluxo definido no **AppSpec**.  
5. **Monitoramento e Rollback:** CodeDeploy oferece monitoramento em tempo real e rollback automático em caso de falha.  

---

## Estrutura do AppSpec File

O **AppSpec** define **as ações de instalação, atualização e teste** da aplicação:

```yaml
version: 0.0
os: linux
files:
  - source: /
    destination: /var/www/html
hooks:
  BeforeInstall:
    - location: scripts/backup.sh
      timeout: 300
      runas: root
  AfterInstall:
    - location: scripts/configure.sh
      timeout: 300
      runas: root
  ApplicationStart:
    - location: scripts/start_server.sh
      timeout: 300
      runas: root
  ValidateService:
    - location: scripts/health_check.sh
      timeout: 300
      runas: root
```
## Vantagens do AWS CodeDeploy

- **Automação Completa:** Implantações repetíveis sem intervenção manual.  
- **Redução de Downtime:** Estratégias de implantação como **Blue/Green** evitam interrupções.  
- **Rollback Automático:** Em caso de falhas, a versão anterior é restaurada automaticamente.  
- **Integração com CI/CD:** Funciona com **CodePipeline**, **Jenkins**, **GitHub Actions** e outros.  
- **Monitoramento e Logs:** Integração com **CloudWatch** e logs detalhados para auditoria.

---

## Referências

-  [Documentação Oficial – AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/)  
-  [Guia de Boas Práticas – AWS CodeDeploy](https://aws.amazon.com/codedeploy/getting-started/)
