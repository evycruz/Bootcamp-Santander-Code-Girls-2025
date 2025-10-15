# Distribuição de Conteúdo com Amazon CloudFront

O **Amazon CloudFront** é o serviço de **Content Delivery Network (CDN)** da AWS, projetado para entregar **conteúdo web, vídeos, APIs e aplicações** com **baixa latência** e alta performance em escala global.

---

## Conceito de CloudFront

- **CDN (Content Delivery Network):** distribui conteúdo em servidores localizados ao redor do mundo (edge locations).  
- **Objetivo:** reduzir o tempo de carregamento e melhorar a experiência do usuário final.  
- **Integração nativa com AWS:** funciona perfeitamente com S3, EC2, Lambda@Edge, API Gateway, entre outros serviços.  

---

## Componentes Principais

- **Edge Locations:** servidores distribuídos globalmente que armazenam cópias em cache do conteúdo.  
- **Distribuições:** configuração que define como o CloudFront entrega o conteúdo.  
- **Origins:** origem do conteúdo, como S3, EC2 ou servidores externos.  
- **Cache Behavior:** regras de cache e roteamento do conteúdo para diferentes endpoints.  
- **Lambda@Edge:** permite executar código em pontos de presença da CDN, personalizando o conteúdo antes da entrega.  

---

## Benefícios

- **Baixa latência:** entrega rápida de conteúdo graças à proximidade das edge locations com os usuários.  
- **Alta disponibilidade:** distribuição global garante redundância e resiliência.  
- **Segurança:** integração com AWS Shield, WAF (Web Application Firewall) e HTTPS.  
- **Escalabilidade automática:** suporta picos de tráfego sem necessidade de gerenciamento manual.  
- **Otimização de custos:** cache eficiente reduz chamadas diretas à origem, economizando largura de banda.  

---

## Casos de Uso Comuns

- Distribuição de sites e aplicações web estáticas e dinâmicas.  
- Streaming de vídeo e mídia ao redor do mundo.  
- Distribuição de APIs e conteúdo de aplicações mobile.  
- Redução de carga em servidores de origem e aumento da performance global.  

---
