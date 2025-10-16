# AWS CloudWatch

O **Amazon CloudWatch** é um serviço da AWS para **monitoramento e observabilidade** de recursos, aplicações e serviços em nuvem.  
Ele coleta e analisa métricas, logs e eventos, permitindo acompanhar o desempenho da infraestrutura e reagir automaticamente a mudanças operacionais.

---

## Conceito de AWS CloudWatch

- **Monitoramento em tempo real:** coleta métricas de serviços AWS como EC2, RDS, Lambda, EBS, S3, entre outros.  
- **Centralização de logs e métricas:** unifica dados operacionais em um único painel.  
- **Alertas automáticos:** permite definir alarmes que notificam ou executam ações quando determinados limites são atingidos.  
- **Integração com automações:** aciona respostas automáticas via SNS, Lambda ou Auto Scaling.

---

## Principais Componentes

- **Metrics (Métricas):** dados numéricos que representam o desempenho de um recurso (ex: CPU, memória, I/O).  
- **Logs:** registros detalhados de aplicações e sistemas, enviados de forma contínua para o CloudWatch Logs.  
- **Alarms (Alarmes):** regras que disparam ações ou notificações baseadas em métricas definidas.  
- **Dashboards:** painéis personalizados para visualizar métricas e logs em tempo real.  
- **Events (Eventos):** detectam mudanças no ambiente AWS e executam ações automáticas.  
- **CloudWatch Agent:** coletor instalado em instâncias EC2 ou servidores locais para capturar métricas adicionais do sistema.

---

## Benefícios

- **Monitoramento centralizado:** visão completa de toda a infraestrutura AWS.  
- **Detecção proativa:** identifica anomalias e problemas antes de impactarem usuários.  
- **Automação de respostas:** aciona ações automáticas (ex: reiniciar instância, enviar alerta, escalar recursos).  
- **Customização:** métricas e dashboards configuráveis de acordo com as necessidades da aplicação.  
- **Integração com Machine Learning:** o CloudWatch Anomaly Detection identifica padrões e desvios de comportamento automaticamente.

---

## Casos de Uso Comuns

- Monitorar desempenho de instâncias EC2, bancos de dados e funções Lambda.  
- Coletar e analisar logs de aplicações distribuídas.  
- Criar alertas de uso de CPU, falhas de rede ou erros de aplicação.  
- Acionar automações via SNS ou Auto Scaling com base em métricas.  
- Observar tendências de uso para otimizar custos e capacidade.

---
