# Arquitetura de microsserviços

Diferentemente das arquiteturas monolíticas, a arquitetura orientada a microsserviços descreve que cada funcionalidade deve ser desenvolvida de forma independente, permitindo que o tie de desenvolvimento possa atualizar ou modificar alguma feature sem que outra seja afetada.

## Projeto AFA-BD

### Arquitetura atual 

![image](https://github.com/AfaBD/AFA-BD-2024/assets/58821700/dabe816f-8764-4004-9ecc-59e817a1f9ab)

Pontos para melhoria:

 - Escalar horizontalmente a aplicação custaria muito recurso, já que seria necessário escalar todas as funcionalidades
 - Manutenção custosa, ja que todas as funcionalidades estão acopladas

### Arquitetura em microsserviços

![WhatsApp Image 2024-04-05 at 9 56 06 PM](https://github.com/AfaBD/AFA-BD-2024/assets/58821700/ec099deb-cb91-4b4c-9b78-be1b829f58f2)

Serviços para a nova arquitetura:

 - Frontend: camada de interação direta com o usuário
 - Backend: camada para operações na camada de persistência (BD)
 - IA-Model: Camada para operações com modelos de ML/IA

Todos os serviços estarão sendo orquestrados com kubernetes
