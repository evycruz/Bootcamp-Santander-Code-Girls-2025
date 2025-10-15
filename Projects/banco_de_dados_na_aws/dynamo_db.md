# Amazon DynamoDB

O **Amazon DynamoDB** é um serviço de **banco de dados NoSQL totalmente gerenciado** pela AWS, projetado para oferecer **alta performance, escalabilidade automática e baixa latência**, ideal para aplicações modernas que exigem grande volume de leitura e escrita.

---

## Conceito de DynamoDB

- **NoSQL:** armazena dados em formato de chave-valor ou documentos, sem esquema rígido.  
- **Gerenciado:** AWS cuida de provisionamento, patching, replicação, backups e escalabilidade.  
- **Alta performance:** oferece leitura e escrita de milissegundos em qualquer escala.  
- **Escalabilidade automática:** ajusta throughput e armazenamento conforme demanda.

---

## Principais Recursos

- **Tabelas, itens e atributos:** estrutura flexível para armazenar dados sem necessidade de esquema fixo.  
- **Particionamento automático:** distribui dados para suportar grandes volumes de acesso simultâneo.  
- **Índices secundários:** Global Secondary Index (GSI) e Local Secondary Index (LSI) para consultas eficientes.  
- **Streams:** captura alterações em tabelas para processamento em tempo real (ex.: Lambda).  
- **Backup e restauração:** snapshots contínuos ou sob demanda para recuperação de dados.  
- **Segurança:** integração com IAM, criptografia em repouso e TLS para dados em trânsito.  

---

## Benefícios

- **Baixa latência:** respostas rápidas mesmo em alta carga de usuários.  
- **Escalabilidade automática:** lida com picos de tráfego sem intervenção manual.  
- **Alta disponibilidade:** replicação de dados entre múltiplas AZs.  
- **Flexibilidade:** estrutura de dados dinâmica, perfeita para aplicações ágeis.  
- **Integração com AWS:** funciona com Lambda, API Gateway, S3, CloudWatch e outros serviços.

---

## Casos de Uso Comuns

- Aplicações web e mobile com alta taxa de leitura e escrita.  
- Jogos online que exigem escalabilidade global e baixa latência.  
- IoT e dispositivos conectados que geram grande volume de dados em tempo real.  
- Analytics em tempo real, caching de dados e sessões de usuário.

---
