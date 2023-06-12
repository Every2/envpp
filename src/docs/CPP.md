# Como funciona a CLI para C++? 

Basicamente você tem um subcomando chamado init com algumas opções, mas no geral, ele já irá criar um projeto de C++ para você.

vcpkg: Instala um gerenciador de pacotes para você utilizar em seus projetos.

build: É deixado opcional, mas você pode usar caso queira usar arquivos de build para seu projeto ou cmake

tests: Cria um diretório de testes para você escrever seus testes em c++.

# Por que o vcpkg?

Foi o que eu utilizei para desenvolver meus projetos, sei da existências de outros gerenciadores de pacotes, mas não testei, é possível que seja mudado no futuro, mas por enquanto será a versão utilizada. 

# Posso usar a cli com Visual Studio?

Sim, cheque na documentação oficial do visual studio como rodar um projeto já existente no visual studio.

# Por que o uso de CMAKE?

Para portabilidade. Porém, se preferir pode não usar. 

# Como funciona a estrutura de um projeto C++ nessa CLI?

Include: É utilizado para colocar seus arquivos .h ou .hpp, colocamos numa pasta com o nome do projeto para evitar conflitos de namespace

src: Aqui vai o código fonte do seu projeto que são os arquivos .cpp

bin: Armazena os executáveis gerado no seu projeto

tests: Cria um diretório de testes para você escrever seus testes em c++, mas pode ser usado qualquer coisa relacionada a testes.

build: É usado para armazenar arquivos de compilação e artefatos intermediários gerados durante o processo de compilação.

# Nessa estrutura de arquivos geralmente se tem um diretório lib, por que na CLI não tem?

O vcpkg tira a utlidade do diretório.

