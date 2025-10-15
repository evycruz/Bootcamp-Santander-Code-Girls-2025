# Amazon VPC (Virtual Private Cloud)

O **Amazon VPC (Virtual Private Cloud)** é um serviço que permite criar **uma rede virtual isolada na nuvem AWS**, oferecendo controle total sobre seu ambiente de rede, incluindo endereçamento IP, sub-redes, roteamento e segurança.

---

## Conceitos Principais

- **VPC (Virtual Private Cloud):**  
  Rede virtual isolada dentro da AWS, onde você pode lançar recursos como instâncias EC2, bancos de dados RDS, e serviços gerenciados.  

- **Sub-redes (Subnets):**  
  Segmentos de rede dentro da VPC.  
  - **Sub-redes públicas:** conectadas à internet através de um Internet Gateway.  
  - **Sub-redes privadas:** isoladas da internet, geralmente para bancos de dados e serviços internos.  

- **Gateways:**  
  - **Internet Gateway (IGW):** permite comunicação entre a VPC e a internet.  
  - **NAT Gateway:** permite que instâncias privadas acessem a internet sem expor IP público.  

- **Tabelas de Roteamento (Route Tables):**  
  Controlam como o tráfego é direcionado entre sub-redes, internet e outros recursos.

- **Security Groups e NACLs:**  
  - **Security Groups:** firewall virtual para instâncias, controlando tráfego de entrada e saída.  
  - **Network ACLs (Access Control Lists):** camada adicional de controle de tráfego para sub-redes.

---

## Benefícios da Amazon VPC

- **Isolamento:** cria ambientes de rede totalmente separados dentro da AWS.  
- **Controle total:** gerencie endereçamento IP, rotas, gateways e regras de firewall.  
- **Segurança:** múltiplas camadas de proteção com Security Groups e NACLs.  
- **Flexibilidade:** integre com VPNs, Direct Connect e peering de VPCs para redes híbridas.  
- **Escalabilidade:** adicione sub-redes, instâncias e serviços conforme a necessidade do projeto.  

---

## Casos de Uso Comuns

- Hospedagem de aplicações web com sub-redes públicas e privadas.  
- Criação de ambientes isolados para bancos de dados e microserviços.  
- Integração de data centers on-premises com AWS via VPN ou Direct Connect.  
- Configuração de arquiteturas multi-camadas com controle de tráfego e segurança.

---
