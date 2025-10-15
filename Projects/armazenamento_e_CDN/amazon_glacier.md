# Amazon Glacier (AWS Glacier)

O **Amazon Glacier** é um serviço de **armazenamento de longo prazo e baixo custo** da AWS, projetado para arquivar dados que **não precisam de acesso frequente**, garantindo durabilidade e segurança.

---

## Conceito de Amazon Glacier

- **Armazenamento de arquivamento:** ideal para backups, arquivos históricos e dados de compliance.  
- **Baixo custo:** oferece armazenamento econômico, com cobrança baseada em volume e tempo de retenção.  
- **Durabilidade:** dados armazenados com **alta durabilidade (11 9s)**, replicados automaticamente em múltiplas **Availability Zones (AZs)**.  
- **Acesso sob demanda:** recuperação de dados pode levar de minutos a horas, dependendo da opção escolhida.

---

## Principais Componentes

- **Vaults:** contêineres que armazenam arquivos (archives) no Glacier.  
- **Archives:** arquivos individuais armazenados dentro dos vaults.  
- **Vault Lock:** permite aplicar políticas imutáveis para compliance e retenção obrigatória de dados.  
- **Retrieval Options:** modos de recuperação que equilibram custo e tempo de acesso:
  - **Expedited:** recuperação rápida (minutos).  
  - **Standard:** recuperação em algumas horas.  
  - **Bulk:** recuperação em até 12 horas, opção mais econômica.

---

## Benefícios

- **Custo extremamente baixo:** ideal para dados que não precisam de acesso imediato.  
- **Alta durabilidade:** proteção contra perda de dados graças à replicação em múltiplas AZs.  
- **Compliance e segurança:** suporta criptografia em repouso, políticas de retenção e Vault Lock.  
- **Integração com AWS:** funciona com S3, AWS Backup, CloudTrail e outros serviços.  
- **Escalabilidade:** armazena petabytes de dados sem limite.

---

## Casos de Uso Comuns

- Arquivamento de registros financeiros e históricos corporativos.  
- Backup de longo prazo de bancos de dados e aplicações.  
- Retenção de logs e informações para compliance e auditoria.  
- Arquivamento de mídia ou conteúdo digital que não é acessado frequentemente.

---
