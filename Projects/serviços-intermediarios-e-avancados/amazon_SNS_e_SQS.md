# Comunicação Assíncrona com Amazon SNS e SQS

A AWS oferece serviços de mensageria que permitem **comunicação assíncrona entre aplicações**, facilitando integração, escalabilidade e desacoplamento de sistemas.

---

## Amazon SNS (Simple Notification Service)

- **Serviço de publicação/assinatura (Pub/Sub):** envia mensagens para múltiplos assinantes simultaneamente.  
- **Gatilho de eventos:** usado para enviar notificações a aplicações, e-mails, SMS ou endpoints HTTP/S.  
- **Integração com AWS:** funciona com Lambda, SQS, HTTP endpoints, email e outros serviços AWS.

### Benefícios do SNS

- Comunicação em tempo real para múltiplos consumidores.  
- Redução de acoplamento entre sistemas.  
- Suporte a alta escala e confiabilidade de entrega.  
- Ideal para notificações, alertas e fan-out de eventos.

---

## Amazon SQS (Simple Queue Service)

- **Serviço de filas de mensagens:** armazena mensagens temporariamente até que sejam processadas por consumidores.  
- **Entrega confiável:** garante que cada mensagem seja processada pelo menos uma vez.  
- **Tipos de fila:** Standard (alto throughput e entrega eventual) e FIFO (ordem garantida e entrega única).  
- **Integração com AWS:** funciona com Lambda, EC2, ECS e outros serviços.

### Benefícios do SQS

- Desacoplamento de componentes da aplicação.  
- Escalabilidade automática do processamento de mensagens.  
- Garantia de entrega e persistência temporária de mensagens.  
- Flexibilidade para criar pipelines de processamento assíncrono.

---

## Como SNS e SQS trabalham juntos

- **Fan-out pattern:** SNS envia uma mensagem para múltiplas filas SQS simultaneamente, permitindo que diferentes consumidores processem dados de forma independente.  
- **Desacoplamento e resiliência:** produtores e consumidores não precisam estar ativos ao mesmo tempo; a fila garante entrega confiável.  
- **Integração com Lambda:** SQS pode acionar funções Lambda para processamento automático de mensagens.

---

## Casos de Uso Comuns

- Notificações de eventos em tempo real para usuários e sistemas.  
- Processamento assíncrono de tarefas em filas, como envio de e-mails ou processamento de arquivos.  
- Orquestração de microservices desacoplados.  
- Implementação de pipelines de dados e workflows distribuídos.

---
