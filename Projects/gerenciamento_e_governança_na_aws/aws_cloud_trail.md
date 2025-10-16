# AWS CloudTrail

O **AWS CloudTrail** é um serviço da AWS que registra e monitora **todas as ações realizadas na sua conta**, proporcionando **auditoria, conformidade e segurança**.  
Com ele, é possível saber **quem fez o quê, quando e de onde**, acompanhando as atividades de usuários, serviços e APIs.

---

## O que é o AWS CloudTrail?

O **CloudTrail** captura automaticamente os eventos da conta AWS, incluindo:

- Chamadas de **API** realizadas via Console, CLI, SDKs ou serviços.  
- **Alterações em recursos** e configurações (ex: criação de instâncias EC2, exclusão de buckets S3).  
- **Ações administrativas**, como modificações em políticas de IAM ou grupos de segurança.

Esses eventos são armazenados em **logs detalhados**, que podem ser enviados para o **Amazon S3**, analisados no **CloudWatch Logs** ou visualizados diretamente no **console do CloudTrail**.

---

## Principais Componentes

- **Event History (Histórico de Eventos):** exibe as últimas atividades da conta nos últimos 90 dias.  
- **Trails (Trilhas):** configuração personalizada para registrar e armazenar eventos em buckets S3.  
- **Management Events:** ações de gerenciamento (ex: criar, deletar ou modificar recursos).  
- **Data Events:** ações que afetam os dados (ex: leitura e gravação em S3 ou chamadas Lambda).  
- **Insight Events:** detectam atividades anômalas e não usuais automaticamente.

---

## Benefícios

- **Auditoria completa:** rastreia todas as ações realizadas nos serviços AWS.  
- **Segurança aprimorada:** identifica atividades suspeitas e acessos indevidos.  
- **Conformidade regulatória:** atende normas de governança como ISO, PCI-DSS e HIPAA.  
- **Integração com CloudWatch:** permite gerar alertas automáticos com base nos eventos.  
- **Análise detalhada:** logs podem ser processados com Athena ou visualizados em dashboards personalizados.

---

## Casos de Uso Comuns

- **Auditar operações administrativas** (ex: quem criou ou deletou um recurso).  
- **Detectar comportamentos anômalos**, como logins de locais incomuns.  
- **Investigar incidentes de segurança** e recuperar histórico de eventos.  
- **Gerar relatórios de conformidade** e evidências para auditorias.  
- **Automatizar alertas** em conjunto com o Amazon CloudWatch e AWS SNS.

---

## Boas Práticas

- Habilite o **CloudTrail em todas as regiões** para não perder eventos globais.  
- Envie os **logs para um bucket S3 dedicado e protegido**.  
- Ative o **CloudTrail Insights** para detectar atividades fora do padrão.  
- Combine com o **AWS Config** para ter rastreamento completo de alterações de configuração.  

---
