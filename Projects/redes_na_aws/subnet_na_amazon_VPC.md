# Subnets na Amazon VPC

Dentro de uma **Amazon VPC (Virtual Private Cloud)**, as **subnets** são segmentos de rede que permitem organizar e isolar recursos de forma eficiente, proporcionando controle detalhado sobre roteamento e segurança.

---

## Conceito de Subnet

- **Subnet (Sub-rede):**  
  É uma divisão lógica da VPC que contém um intervalo de endereços IP específicos.  
  Cada subnet está localizada dentro de uma **Availability Zone (AZ)**, garantindo alta disponibilidade e resiliência.

- **Tipos de Subnets:**
  - **Pública:**  
    - Possui rota para o **Internet Gateway (IGW)**.  
    - Ideal para servidores web, NAT Gateways ou recursos que precisam de acesso à internet.
  - **Privada:**  
    - Não possui rota direta para a internet.  
    - Ideal para bancos de dados, serviços internos e recursos sensíveis.  
    - Pode acessar a internet via **NAT Gateway** se necessário.

---

## Características Principais

- Cada subnet é associada a uma **tabela de roteamento**, definindo como o tráfego é direcionado.  
- Permite segmentação de rede dentro de uma VPC para **isolamento e organização de recursos**.  
- Trabalha em conjunto com **Security Groups** e **NACLs** para controle de tráfego e segurança.  
- Pode ser expandida ou reduzida conforme a demanda de recursos da aplicação.

---

## Benefícios de Usar Subnets

- **Isolamento:** separa recursos públicos e privados, aumentando a segurança.  
- **Alta disponibilidade:** distribui recursos em diferentes **AZs** dentro da VPC.  
- **Gerenciamento eficiente:** facilita organização de recursos, roteamento e políticas de segurança.  
- **Flexibilidade:** permite criar arquiteturas multi-camadas e segmentadas.

---

## Casos de Uso Comuns

- Hospedagem de servidores web em subnets públicas e bancos de dados em subnets privadas.  
- Criação de ambientes seguros para aplicações corporativas com múltiplas camadas.  
- Configuração de arquiteturas híbridas conectadas a data centers locais via VPN ou Direct Connect.

---
