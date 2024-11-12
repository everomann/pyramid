# Pyramid Framework
Framework opensource focado em simplificar o desenvolvimento de aplicações web em Python.

O Pyramid oferece uma base simples para começar um projeto pequeno, mas permite que a aplicação cresça e se expanda de maneira simples à medida que as necessidades aumentam.

### Responsáveis pelo desenvolvimento
O framework surgiu em 2010 como um projeto da Pylons Project, influenciado pela falta de alguns recursos em ferramentas como o Zope e o Django,
e se porpos a ser mais flexível e permitindo ao desenvolvedor mais liberdade.

[Atualmente o projeto é mantido pela comunidade.](https://github.com/Pylons/pyramid)

### Licença
É distribuido sob a licença BSD, que permite a utilização em projetos pessoais e comerciais desde que os devidos créditos sejam atribuidos.

### Principais características
- **Simplicidade e Flexibilidade:** framework com premissa minimalista, permitindo ao desenvolvedor adicionar apenas os componentes de que precisa, evitando o peso de funcionalidades desnecessárias.
- **Extensibilidade e Compatibilidade:** possui uma rica coleção de bibliotecas e plugins além de permitir a criação de add-ons, sendo fácil adicionar novas funcionalidades ou substituir componentes existentes.
- **Arquitetura baseada em WSGI:**  é construído em cima do padrão Web Server Gateway Interface, o que significa que pode ser executado em qualquer servidor compatível.
- **Suporte a APIs RESTful:** a adaptabilidade do Pyramid para definir recursos e manipular requisições HTTP o torna muito adequado para a criação de microserviços web e APIs.

### Servidores Web Disponíveis
- **WSGI Servers:** compatível com servidores WSGI, como Gunicorn e uWSGI, que são frequentemente usados para aplicações Python em produção.
- **NGINX e Apache:** comum usá-lo por trás de servidores NGINX ou Apache para lidar com o balanceamento de carga, redirecionamento e segurança.

### Vantagens
- **Escalabilidade:** É apropriado tanto para projetos pequenos quanto para aplicações complexas, escalando bem conforme a necessidade.
- **Bom suporte para APIs:** Facilita a criação de APIs, tornando-o uma escolha adequada para sistemas que se comunicam com várias plataformas.
- **Roteamento:** Um dos mais flexíveis e poderosos entre os frameworks Python. Ele suporta rotas dinâmicas, parametrizadas e expressões regulares.

### Desvantagens.
- **Curva de Aprendizado:** mais complexo para iniciantes devido à sua flexibilidade.
- **Menos Recursos Embutidos:** Por ser minimalista, não possui tantos recursos prontos quanto frameworks mais opinativos, exigindo que o desenvolvedor tenha conhecimento para implementar funcionalidades adicionais.
- **Baixa popularidade:** perde por muito em popularidade pra outros frameworks python, tornando a criação de conteúdos específicos escasso .


## Configurações Necessárias para Rodar uma Aplicação (Windows)
- [Python versão 3.6 ou maior](https://www.python.org/downloads/)
- [Pycharm IDE](https://www.jetbrains.com/pycharm/): apenas a versão PRO ja vem com a opção de criar um projeto já com o framework Pyramid. A versão Community ou outras IDEs necessitam passos extras para a criação do projeto.
- [Pyramid](https://trypyramid.com/)

  ```
  
  pip install pyramid
  
  ```
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/): ferramenta para gerar modelos de projetos de forma automatizada. Necessário caso esteja utilizando Pycharm Community ou outra IDE que não seja o Pycharm PRO. 
  ```
  
  pip install cookiecutter
  
  ```
### Criando um projeto Pyramid
  
  Se você possui a IDE Pycharm PRO basta 
  1. Acessar File > New Project
  2. Selecionar no painel lateral o Pyramid
  3. Selecionar o Jinja2 como Template Language
  4. Selecionar o SQLAlchemy pra persistir no BackEnd
  5. Clicar em Create e o projeto será criado já com uma estrutura básica

Se estiver utilizando Pycharm Community
  1. Acessar File > New Project
  2. Selecionar no painel lateral se esta selecionada a opção Pure Python
  3. Após a criação do projeto python, abra o terminal vá até (View > Tool Windows > Terminal)
  4. Instalar a ferramenta cookiecutter pra criação do template do projeto
      ```
        
      pip install cookiecutter
      
      ```
  5. Executar o comando abaixo para a criação do template
     ```
        
      cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout 2.0-branch
      
      ```

  6. Serão exibidas no terminal algumas opções que precisam ser preenchidas:
     - project_name: insira o nome do projeto de de enter
     - repo_name: insira o nome do repositrio do projeto e de enter
     - Select template_language: digite 1 para selecionar o Jinja2 e de enter
     - Select backend: digite 2 para selecionar o SqlAchemy e de enter
  Como resultado disto será criada uma pasta com o nome inserido em project_name contendo o projeto criado.
 
  7. Com o projeto criado, mas ainda são necessárias alguns passos. Navegue pelo terminal até a pasta do seu projeto usando ```cd nomde_do_projeto```
  
  8. Instalar as dependencias definidas no arquivo setup.py:
      ```
        
      pip install -e .
      
      ```
  9. Precisamos agora gerar uma migration inicial para o nosso banco de dados usando os comandos:
      para criar a primeira revisão de migração.
      ```
        
      alembic -c development.ini revision --autogenerate -m "init"
      
      ```
      e para aplicar essa revisão ao banco de dados
      ```
        
      alembic -c development.ini upgrade head
      
      ```
      * Esses comandos precisam ser executados sempre que fizer mudanças no modelo de dados (adicionar uma nova tabela, modificar uma coluna existente, etc.)
        
  11. Inicializar o banco de dados carregando os dados padrão :
      ```
        
      initialize_myproject_db development.ini
      
      ```
  12. Executar o projeto
      ```
        
      pserve development.ini
      
      ```
      
