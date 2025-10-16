# Orquestração de Contêineres com Amazon ECS e EKS

A **AWS** oferece serviços robustos para **orquestrar contêineres**, permitindo que aplicações em containers sejam **implantadas, escaladas e gerenciadas** de forma confiável e eficiente na nuvem.

---

## Amazon ECS (Elastic Container Service)

- **Serviço gerenciado de contêineres:** permite executar e gerenciar contêineres Docker sem gerenciar a infraestrutura subjacente.  
- **Integração com AWS:** funciona nativamente com EC2 e Fargate (serverless para containers).  
- **Escalabilidade:** ajusta automaticamente o número de contêineres com base na demanda.  
- **Segurança:** integração com IAM, VPC, Security Groups e políticas de execução de tarefas.

### Benefícios do ECS

- Simplicidade: fácil configuração e gerenciamento de clusters de contêineres.  
- Flexibilidade: escolha entre execução em EC2 (clusters gerenciados) ou Fargate (serverless).  
- Integração nativa: funciona com CloudWatch, ELB, IAM, S3 e outros serviços AWS.

---

## Amazon EKS (Elastic Kubernetes Service)

- **Kubernetes gerenciado pela AWS:** permite executar clusters Kubernetes de forma simplificada.  
- **Totalmente compatível com Kubernetes:** permite migrar aplicações existentes de Kubernetes para a AWS sem alterações.  
- **Escalabilidade e resiliência:** gerencia automaticamente nós e clusters, distribuindo cargas de forma eficiente.  
- **Segurança:** integração com IAM, VPC, Security Groups e criptografia para comunicação entre pods.

### Benefícios do EKS

- Compatibilidade com Kubernetes padrão do mercado.  
- Redução da complexidade de manutenção do cluster Kubernetes.  
- Suporte a workloads híbridas e multi-região.  
- Integração com serviços AWS como ALB, CloudWatch, IAM e RDS.

---

## Casos de Uso Comuns

- Execução de aplicações microservices escaláveis em containers.  
- Modernização de aplicações legadas usando contêineres Docker.  
- Workloads que exigem alta disponibilidade, escalabilidade automática e orquestração avançada.  
- Pipelines de CI/CD com deploys automáticos em clusters gerenciados.

---
