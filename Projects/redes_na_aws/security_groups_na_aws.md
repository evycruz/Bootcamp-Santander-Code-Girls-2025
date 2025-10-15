# Security Groups na AWS

Os **Security Groups** são firewalls virtuais da AWS que controlam o **tráfego de entrada e saída** de instâncias e outros recursos, garantindo segurança e controle detalhado na nuvem.

---

## Conceito de Security Group

- Um **Security Group (SG)** funciona como um **conjunto de regras de firewall virtual** associado a recursos como **Amazon EC2, RDS, ELB** e outros.  
- Ele define **quais portas e protocolos são permitidos** para tráfego de entrada (inbound) e saída (outbound).  
- Diferente de firewalls tradicionais, **Security Groups são stateful**, ou seja, se o tráfego de entrada é permitido, a resposta de saída é automaticamente permitida.

---

## Principais Características

- **Regras Inbound:** definem quais fontes podem acessar o recurso e em quais portas.  
- **Regras Outbound:** definem para quais destinos o recurso pode enviar tráfego.  
- **Stateful:** não é necessário criar regras de resposta para o tráfego permitido; a AWS gerencia automaticamente.  
- **Aplicável a múltiplos recursos:** um mesmo SG pode ser associado a várias instâncias.  
- **Atualização dinâmica:** alterações em um SG são aplicadas instantaneamente aos recursos associados.

---

## Boas Práticas de Security Groups

- **Princípio do menor privilégio:** permita apenas o tráfego necessário.  
- **Separação por função:** crie SGs diferentes para bancos de dados, servidores web e aplicações.  
- **Uso de tags:** nomeie e categorize SGs para fácil identificação e gerenciamento.  
- **Monitoramento e auditoria:** use **CloudTrail** e **VPC Flow Logs** para acompanhar alterações e tráfego.  
- **Evite regras de acesso aberto:** minimize o uso de `0.0.0.0/0` e restrinja IPs ou redes específicas.

---

## Benefícios

- **Segurança reforçada:** controla exatamente quem acessa os recursos e de onde.  
- **Flexibilidade:** regras podem ser ajustadas a qualquer momento sem reiniciar instâncias.  
- **Escalabilidade:** SGs acompanham recursos dinamicamente, simplificando a administração.  
- **Integração nativa:** funciona com EC2, RDS, ELB e outros serviços AWS.

---

## Casos de Uso Comuns

- Permitir acesso SSH (porta 22) apenas de IPs confiáveis.  
- Liberar tráfego HTTP/HTTPS (portas 80/443) para servidores web públicos.  
- Restringir acesso a bancos de dados somente a instâncias específicas da aplicação.  

---
