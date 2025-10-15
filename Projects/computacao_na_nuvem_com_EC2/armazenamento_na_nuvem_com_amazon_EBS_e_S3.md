# Armazenamento na Nuvem com Amazon EBS e S3

A AWS oferece soluções de **armazenamento na nuvem** flexíveis, escaláveis e seguras, permitindo que empresas e desenvolvedores armazenem e gerenciem dados de forma eficiente.  
Duas das soluções mais utilizadas são **Amazon EBS** e **Amazon S3**.

---

## Amazon EBS (Elastic Block Store)

O **Amazon EBS** fornece **armazenamento em blocos** persistente para instâncias EC2, ideal para aplicações que exigem **alta performance e baixa latência**.

### Características principais:

- **Volumes de armazenamento:** anexados a instâncias EC2 como discos rígidos virtuais.  
- **Tipos de volume:** SSDs (gp3, io2) e HDDs (st1, sc1) para diferentes necessidades de performance.  
- **Persistência:** os dados permanecem mesmo se a instância for desligada.  
- **Snapshots:** backups incrementais que podem ser armazenados no S3 para recuperação e replicação.  

---

## Amazon S3 (Simple Storage Service)

O **Amazon S3** é um serviço de **armazenamento de objetos** altamente escalável, seguro e durável, usado para arquivos, backups, dados de aplicações e muito mais.

### Características principais:

- **Objetos e buckets:** dados armazenados como objetos em buckets organizados hierarquicamente.  
- **Escalabilidade automática:** suporta desde pequenos arquivos até petabytes de dados.  
- **Classes de armazenamento:** Standard, Intelligent-Tiering, Glacier, Deep Archive para otimização de custos e desempenho.  
- **Controle de acesso:** políticas, ACLs e integração com IAM para segurança refinada.  
- **Integração:** se conecta com diversos serviços AWS como Lambda, CloudFront, RDS e Redshift.  

---

## Diferenças e Casos de Uso

| Serviço | Tipo de armazenamento | Ideal para | Persistência |
|---------|--------------------|------------|--------------|
| **EBS** | Blocos (attached to EC2) | Sistemas operacionais, bancos de dados, aplicações com alta performance | Sim, ligado a uma instância EC2 |
| **S3** | Objetos (independente) | Backups, arquivos estáticos, dados de aplicações e big data | Sim, durável e replicável globalmente |

---

## Benefícios

- **Escalabilidade:** armazene dados sem limites rígidos de tamanho.  
- **Segurança:** controle refinado de acesso e criptografia nativa.  
- **Alta disponibilidade:** replicação automática em múltiplas AZs (S3) e integração com snapshots (EBS).  
- **Custo eficiente:** escolha tipos de armazenamento de acordo com desempenho e frequência de acesso.  

---





