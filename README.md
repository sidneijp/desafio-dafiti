# Dafiti | Desafio Técnico
___

## Instalação, desenvolvimento, manutenção e gestão da aplicação

* DISCLAIMER: os serviços do Docker devem contemplar a instalação de todas as dependências e facilitar o uso para desenvolvimento e deploy em produção. Portanto devem ser atualizados e não podem ser substituídos por Documentação. As documentações devem ser atualizadas conforme necessidade, refletindo as alterações no ambiente e arquitetura, portanto informações de pacotes, versões, dependências, etc., citadas neste documento auxiliam nas explicações, entretanto informações mais precisas - **single source of truth** - SEMPRE estarão no código, seja no docker-compose.yml, Dockerfile, Pipfile/Pipfile.lock, package.json/yarn.lock. AUTOMATIZE o que pode ser automatizado, documente o que foi automatizado e o que ainda não foi viável de automatizar.

### Dependências

- Docker >=18
- docker-compose >=1.21
- gnu make (opcional)

* As receitas do Makefile em sua maioria estão abstraindo simples comandos do docker-compose. Caso não o use o `make`, basta ler o Makefile
* Este Makefile foi desenhado especificamente para o Linux e testado no Ubuntu 18.04

### Setup ambiente

Para prepara o ambiente inicial execute uma única vez:

`$ make init`

Este comando irá:

1. gerar o arquivo `.env` com as configurações e segredos para o ambiente local com base no arquivo `.env.sample` e informações do usuário que o executa;
2. parar e remover os serviços (containers) declarados no arquivo `docker-compose.yml` e então reconstruir (build) as imagens docker;
3. recriar o banco de dados e executar todas as migrações de banco de dados.

* Conforme o desenvolvimenot acontece, o ambiente contruído localmente na máquina pode ficar muito defasado. Caso tenha problemas, principalmente ao trocar de branches, utilize o `make init` para reconstruir o ambiente.
* Para personalizar o ambiente local, altere o arquivo `.env`, mas sempre que precisar de uma nova variável de ambiente atualize o .env.sample com um valor favorável aos ambientes de desenvolvimento. O .env.sample não define valores padrões, mas traz um conjunto de valores que podem ser expostos no git sem problemas, logo, defina valores padrões seguros (e.g. DEBUG=False). Concentre as configurações da aplicação no arquivo `src/main/settings.py` usando o [python-decouple](https://github.com/henriquebastos/python-decouple) para obter variáveis de ambiente.

Para executar todo o ambiente localmente,

`$ make up`

### Comandos com o Makefile

Estará disponível:
- [http://localhost:8000/](http://localhost:8000/) - Home da apicação
- [http://localhost:8000/admin/](http://localhost:8000/admin/) - Django Admin's Site
- [http://localhost:8025/](http://localhost:8025/) - Mailhog ("Inbox" para teste de envio/recebimento de email)

Para visualizar todos os logs da aplicação:

`$ make logs [nome do serviço]`

Para criar um `superuser` para utilizar a aplicação:

`$ make dj createsuperuser`

Para executar qualquer comando do Django (Django management commmands):

`$ make dj "<comando> e opções entre aspas"`

* `make dj` sobe um container docker e executa o `manage.py`
* comando necessita que o container esteja em execução

Para instalar um novo pacote python:

`$ make install "<pacote> [pacote]"`

* Isso instala o pacote no container e atualiza os arquivos Pipfile
* Caso o pacote instalado seja usado apenas para o desenvolvimento, use a flag `--dev`
* comando necessita que o container esteja em execução

Para visualizar o status dos serviços (containers) do projeto, execute:

`$ make status`

Para iniciar, parar ou reiniciar um serviço/container, respectivamente, use:

`$ make start "[nome do servico] [nome do servico] ..."`
`$ make stop "[nome do servico] [nome do servico] ..."`
`$ make restart "[nome do servico] [nome do servico] ..."`

* Se não passar um nome de serviço, a ação ocorrerá sobre todos os serviços
* Um container parado ou reiniciado não perde os dados (e.g., o banco de dados continua com os dados).
Os dados serão perdidos se o container for removido

Os serviços disponíveis são:

- db: postgres
- mailhog: serviço de email para capturar os emails enviados pela aplicação
- web: a aplicação django

Para usar um shell dentro de um container (para depuração, por exemplo):

`$ make sh <nome do servico>`

* comando necessita que o container esteja em execução

Para executar os tests:

`$ make test`

* comando necessita que o container esteja em execução

... ou executá-los em "watcher mode":

`$ make test-watch`

* comando necessita que o container esteja em execução

Para gerar relatório de cobertura de testes:

`$ make coverage`

* comando necessita que o container esteja em execução

... e então visualizar o relatório (precisa rodar o `make coverage` antes):

`$ make report`

* comando necessita que o container esteja em execução

Para gerar um HTML do relatório de cobertura (precisa rodar o `make coverage` antes):

`$ make html`

* O relatório HTML estará disponível em `./src/htmlcov/index.html` - abra o `index.html` no seu web browser.
* comando necessita que o container esteja em execução
