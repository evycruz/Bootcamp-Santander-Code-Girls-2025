# Backup e Recuperação de Dados na AWS

Garantir a **disponibilidade e integridade dos dados** é essencial em qualquer aplicação. A AWS oferece soluções robustas para **backup, restauração e recuperação de desastres**, permitindo proteção confiável e escalável na nuvem.

---

## Conceito de Backup e Recuperação na AWS

- **Backup:** cópia de dados para proteção contra perda ou corrupção.  
- **Recuperação de dados:** processo de restaurar dados a partir de backups ou snapshots em caso de falha.  
- **Serviços gerenciados:** AWS oferece soluções que automatizam backup, versionamento e replicação de dados.

---

## Principais Serviços de Backup

- **Amazon S3:** armazenamento durável para backups e arquivos.  
  - **Versioning:** mantém múltiplas versões de objetos.  
  - **Cross-Region Replication (CRR):** replica dados entre regiões para maior resiliência.  

- **Amazon EBS:** snapshots de volumes EBS para restaurar instâncias EC2 rapidamente.  

- **Amazon RDS:** backups automáticos e snapshots manuais de bancos de dados relacionais.  

- **AWS Backup:** serviço centralizado para gerenciar backups de múltiplos serviços AWS (EBS, RDS, DynamoDB, EFS, Storage Gateway).  

- **Amazon Glacier:** armazenamento de longo prazo e baixo custo para dados arquivados.

---

## Estratégias de Backup

- **Automatização:** use políticas de backup e schedules para reduzir erros manuais.  
- **Multi-região:** replique dados em diferentes regiões para proteção contra desastres.  
- **Versionamento:** mantenha versões antigas de arquivos para recuperar estados anteriores.  
- **Testes de recuperação:** valide regularmente que os backups podem ser restaurados corretamente.

---

## Benefícios

- **Alta disponibilidade e durabilidade:** dados armazenados em múltiplas AZs e regiões.  
- **Redução de risco:** protege contra perda de dados, corrupção ou falhas de infraestrutura.  
- **Eficiência operacional:** serviços gerenciados reduzem necessidade de manutenção manual.  
- **Flexibilidade de custo:** armazenamento escalável e opções de arquivamento econômico.

---

## Casos de Uso Comuns

- Recuperação de instâncias EC2 ou volumes EBS após falhas.  
- Proteção de bancos de dados relacionais com RDS Backup e snapshots.  
- Arquivamento de dados antigos com Amazon Glacier para compliance e auditoria.  
- Estratégias de disaster recovery para aplicações críticas corporativas.

---
