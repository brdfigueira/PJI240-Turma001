# Projeto Advocacia Digital

## RESUMO
 
 Partindo dos problemas e oportunidades de melhoria identificados no diálogo com a advogada Janaina de Borba Larisca sobre sua rotina de trabalho, em particular no que concerne à comunicação com clientes, esse projeto se propõe ao desenvolvimento de uma aplicação web voltada ao apoio às atividades de atendimento advocatício. Tal aplicação, além de assegurar o armazenamento estruturado de informações relativas aos clientes e processos, deverá apresentar funcionalidades que propiciem melhorias na qualidade das interações entre advogado e cliente, tornando mais práticas e ágeis a triagem para o atendimento inicial e o acompanhamento dos processos em curso. O desenvolvimento desta aplicação está sendo realizado seguindo um processo fundamentado nos princípios do design thinking e de métodos ágeis para engenharia de software. Em consonância com a natureza da demanda e a metodologia escolhida, foram adotadas estratégias que facilitam o processo de desenvolvimento, tais como o uso de frameworks (Django e Bootstrap) e APIs. É realizada a apresentação do protótipo desenvolvido nas primeiras etapas do projeto com o objetivo de constituir o núcleo da aplicação e funcionar como disparador para coleta de feedback da advogada, alimentando as próximas etapas do processo de desenvolvimento.


## Desenvolvimento e plano de ação.

### OBJETIVOS

O objetivo geral deste projeto é realizar o desenvolvimento de uma aplicação web voltada para o apoio às atividades de atendimento advocatício. Essa aplicação deverá facilitar o registro e armazenamento, de maneira estruturada relacionalmente, de informações de clientes, processos e documentos correspondentes, bem como apresentar funcionalidades que assegurem melhorias na qualidade das interações entre advogados e clientes, tornando mais ágeis e práticas a triagem para o atendimento inicial e a comunicação com o cliente durante o acompanhamento do processo.
Podemos indicar como objetivos específicos a garantia dos principais requisitos identificados até o momento, bem como características esperadas para sua apresentação aos usuários:

- Elaborar um website que: (1) contenha as informações sobre a advogada, tais como seus dados de contato e área de atuação, (2) permita ao usuário registrado ou não o acesso ao formulário de triagem e (3) permita ao usuário registrado o acesso à interface com o banco de dados.
- Implementar um banco de dados que persista as informações sobre os clientes, suas demandas, os processos correspondentes e as atualizações desses processos.
- Desenvolver uma interface para interação com o mencionado banco de dados e que disponha de dois perfis de acesso: (1) um perfil para os clientes, que permitirá acesso somente às suas informações e às de seus processos, com capacidades limitadas de edição; (2) o perfil para a advogada, que permitirá acesso amplo às informações dos clientes e dos processos, com amplas capacidades de edição.
- Criar um formulário de triagem legal, acessível para usuários previamente registrados ou não, através do qual um cliente ou possível cliente possa apresentar uma demanda jurídica à advogada. Tal formulário deverá apresentar informações fundamentais sobre a demanda que permitam à advogada se preparar para o atendimento, reconhecer sua natureza e se pertence à sua área de atuação. Essas informações devem ser processadas e entregues de maneira conveniente para a advogada. Esse mesmo formulário será denominado “formulário de apresentação de demandas” em outros pontos do presente projeto.
- Estabelecer um mecanismo que permita ao sistema consumir as atualizações dos processos informadas pelos sistemas de processo eletrônico e reagir a elas, facilitando para o advogado a criação e envio de mensagens explicativas para o cliente sobre essa movimentação e permitindo o monitoramento dessa comunicação.

