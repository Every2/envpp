# Como funciona a CLI para Javascript?

Basicamente você vai escolher o gerenciador de pacotes de sua preferencia com o subcomando init e ele irá utilizar o vite pra criação de seus projetos.

# Por que Docker compose e não Dockerfile?

Basicamente porque o vite cria um projeto e utiliza um servidor local, então o docker compose acaba encaixando melhor.

# Por que o npm não vem ativado por padrão?

Bom, pra evitar conflitos futuros. Imagina você roda o script desavisado e cria um projeto com npm e depois yarn, já pensou a dor de cabeça que ia ser?

# A CLI tem compatibilidade com Typescript?

Sim, você pode escolher se vai usar Typescript ou Javascript.

# Por que não tem uma opção para testes e por que javascript tem menos opções?

Não sei o que a comunidade em si gosta para testes em JS, então optei por não colocar. Sobre a falta de opções, basicamente o Vite já cria um ambiente inteiro praticamente então acaba que não se faz necessário mais opções.
