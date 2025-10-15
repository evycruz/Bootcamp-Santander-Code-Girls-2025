# Instâncias EC2 e Otimização de Recursos na AWS

O **Amazon EC2 (Elastic Compute Cloud)** é o serviço de computação da AWS que permite criar **máquinas virtuais escaláveis** na nuvem, oferecendo flexibilidade para executar aplicações, testar ambientes e gerenciar workloads com eficiência.

---

## Conceitos de EC2

- **Instâncias:** máquinas virtuais com diferentes tipos de CPU, memória e armazenamento.  
- **AMIs (Amazon Machine Images):** imagens pré-configuradas para criar instâncias rapidamente.  
- **Tipos de instância:** otimizado para computação, memória, armazenamento ou uso geral.  
- **Elastic IPs:** endereços IP fixos para instâncias, garantindo acessibilidade estável.  
- **Grupos de segurança:** firewall virtual para controlar tráfego de entrada e saída.  

---

## Estratégias de Otimização de Recursos

Para reduzir custos e melhorar a performance, a AWS oferece ferramentas e boas práticas:

- **Escolha correta do tipo de instância:** selecione instâncias alinhadas à carga de trabalho (compute, memory ou storage optimized).  
- **Escalabilidade automática (Auto Scaling):** ajuste automaticamente o número de instâncias conforme a demanda.  
- **Instâncias Spot:** utilize instâncias de baixo custo para workloads flexíveis e interrupíveis.  
- **Instâncias reservadas:** comprometa-se com capacidade por longo prazo para reduzir custos de instâncias contínuas.  
- **Monitoramento com CloudWatch:** acompanhe CPU, memória, I/O e outros indicadores para identificar recursos ociosos ou sobrecarregados.  
- **Desligamento de instâncias ociosas:** desligue instâncias que não estão em uso para evitar gastos desnecessários.  

---

## Benefícios da Otimização

- **Redução de custos:** paga-se apenas pelo que é realmente utilizado.  
- **Melhoria de performance:** instâncias adequadas ao workload garantem maior eficiência.  
- **Escalabilidade:** capacidade de ajustar recursos automaticamente conforme a demanda.  
- **Gestão eficiente:** monitoramento contínuo permite decisões estratégicas sobre recursos.  

---

