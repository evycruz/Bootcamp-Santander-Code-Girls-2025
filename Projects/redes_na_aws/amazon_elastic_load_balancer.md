# Amazon Elastic Load Balancer (ELB)

O **Amazon Elastic Load Balancer (ELB)** é um serviço da AWS que distribui automaticamente o **tráfego de entrada** entre múltiplas instâncias ou serviços, garantindo **alta disponibilidade, escalabilidade e resiliência** para aplicações na nuvem.

---

## Conceito de ELB

- **Balanceamento de carga:** distribui solicitações de usuários entre várias instâncias EC2, contêineres ou endpoints.  
- **Objetivo:** aumentar a disponibilidade e performance de aplicações, evitando sobrecarga em recursos individuais.  
- **Integração com AWS:** funciona com EC2, ECS, Lambda e outros serviços AWS.

---

## Tipos de ELB

- **Application Load Balancer (ALB):**  
  - Opera na camada 7 (HTTP/HTTPS).  
  - Roteamento baseado em conteúdo, host ou caminho.  
  - Ideal para aplicações web modernas e microserviços.

- **Network Load Balancer (NLB):**  
  - Opera na camada 4 (TCP/UDP).  
  - Suporta alta performance, baixa latência e tráfego em grande escala.  
  - Ideal para aplicações que exigem performance de rede.

- **Classic Load Balancer (CLB):**  
  - Suporta balanceamento em camadas 4 e 7.  
  - Recomendada apenas para aplicações legadas.

---

## Principais Características

- **Distribuição automática de tráfego:** evita sobrecarga em instâncias individuais.  
- **Alta disponibilidade:** balanceamento entre múltiplas **Availability Zones (AZs)**.  
- **Integração com Auto Scaling:** ajusta automaticamente o número de instâncias conforme demanda.  
- **Health Checks:** monitora a saúde das instâncias e direciona tráfego apenas para recursos saudáveis.  
- **SSL/TLS Termination:** termina conexões seguras no load balancer, simplificando a configuração de certificados.

---

## Benefícios

- **Escalabilidade:** suporta picos de tráfego sem intervenção manual.  
- **Resiliência:** mantém aplicações disponíveis mesmo se instâncias falharem.  
- **Segurança:** compatível com VPC, Security Groups e TLS/SSL.  
- **Eficiência operacional:** reduz complexidade de gerenciamento de tráfego e distribuição de carga.

---

## Casos de Uso Comuns

- Distribuição de tráfego de sites e aplicações web.  
- Balanceamento de carga para microserviços em containers (ECS/EKS).  
- Suporte a aplicações críticas que exigem alta disponibilidade e performance consistente.  
- Roteamento inteligente de solicitações baseado em host ou path com ALB.
