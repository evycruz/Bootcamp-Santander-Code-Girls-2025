# Amazon S3 (Simple Storage Service)

O **Amazon S3** é um serviço de **armazenamento de objetos altamente escalável e durável** na nuvem AWS, ideal para armazenar e proteger qualquer tipo de dados, desde arquivos estáticos até backups e dados de aplicações corporativas.

---

## Conceito de Amazon S3

- **Armazenamento de objetos:** cada arquivo é armazenado como um objeto, composto por dados, metadados e uma chave única (Key).  
- **Durabilidade e disponibilidade:** S3 oferece **99,999999999% de durabilidade (11 9s)** e alta disponibilidade para objetos.  
- **Escalabilidade automática:** armazena qualquer volume de dados sem necessidade de provisionamento manual.

---

## Principais Componentes

- **Buckets:** contêineres que armazenam objetos no S3. Cada bucket deve ter um nome único global.  
- **Objetos:** arquivos individuais armazenados dentro dos buckets.  
- **Chaves (Keys):** identificadores únicos para objetos dentro de um bucket.  
- **Versioning:** mantém múltiplas versões de um mesmo objeto, permitindo recuperação de versões antigas.  
- **Lifecycle Policies:** regras automáticas para mover ou excluir objetos com base em critérios definidos.  
- **Storage Classes:** diferentes classes de armazenamento para otimização de custo e performance:
  - **S3 Standard:** uso geral, alta disponibilidade e durabilidade.  
  - **S3 Intelligent-Tiering:** ajusta automaticamente entre camadas de custo com base em acesso.  
  - **S3 Glacier:** arquivamento de longo prazo com baixo custo.  

---

## Benefícios

- **Alta durabilidade e disponibilidade:** protege dados críticos com replicação automática em múltiplas AZs.  
- **Segurança:** suporte a IAM, políticas de bucket, criptografia em repouso e em trânsito.  
- **Flexibilidade de acesso:** suporte a APIs, SDKs, console e integração com outros serviços AWS.  
- **Eficiência de custos:** escolha de classes de armazenamento e políticas de ciclo de vida para otimização.  
- **Escalabilidade automática:** armazena desde pequenos arquivos até petabytes de dados sem limite.

---

## Casos de Uso Comuns

- Armazenamento de arquivos estáticos de sites e aplicações web.  
- Backup e recuperação de dados corporativos.  
- Data lakes e pipelines de análise de dados.  
- Armazenamento de mídia, imagens e vídeos para streaming.  
- Arquivamento de dados com S3 Glacier para compliance.

---
