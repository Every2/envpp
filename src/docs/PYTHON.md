# Como funciona a CLI para Python?

Bom, basicamente você tem um commando chamado "python" que cria um projeto pra você com o pdm, caso você não tenha instalado, não se preocupe. A cli vai instalar e configurar tudo pra você. 

Dentro desse commando "python" temos os subcomandos docker, init, docs, scripts, tests. 

Docs e scripts: Basicamente vai criar uma pasta com nome docs e scripts, dentro da pasta você pode ter scripts de shell, python mesmo ou alguma outra lang que você utiliza pra lidar com algo que rode isolado e não se encaixe nos outros diretórios. Docs basicamente é pra criar uma documentação para o seu projeto, foi utilizado markdown, mas você pode usar txt, html e etc... se preferir.

Init: Cria seu projeto, instala as dependencias e usa pdm por de baixo dos panos.

Tests: Cria um diretório de testes pra você e usa pytest, por padrão essa opção vem ativada diferente das outras, mas caso não queira testes no seu projeto, você pode usar a flag --no-tests e aí não será criado esse diretório.

Docker: Vai criar um dockerfile na pasta do seu projeto.

# Por que o PDM e não mais o pipenv?

Bom, ambos tem funções parecidas e tem o mesmo proposito que é fazer o script ser portatil. Porém, venho utilizando o pdm e gostando mais, então optei por usar ele nessa nova versão.

# Por que não um docker compose igual em Javascript?

Como não lido direto com APIs ou algo que necessite de um docker compose, então optei por deixar o design para python mais simples e usar um dockerfile. 

# Por que a parte de Python tem mais comandos?

Algumas coisas não vem por padrão no pip, então acaba que você tem que fazer manualmente, por isso mais comandos.

# Por que lint não tem mais opções iguais na antiga cli?

Basicamente é incorporado dentro do proprio mypy então achei bem redundante manter.

# Por que eu não teria testes no meu projeto?

A Cli visa atender vários públicos então um iniciante talvez não saiba testes e deixar o diretório ali acaba ficando sem sentido, então é dada a opção de não usar. 