#### Projeto Escolhido no Github: Age Calculator - [Link](https://github.com/clarencesarmiento/CS50P-Final-Project)
#### Framework Teste Unitário: Pytest - [Link](https://docs.pytest.org/en/stable/)
#### Toolkit Cobertura de Testes: Pytest-cov- [Link](https://pypi.org/project/pytest-cov/)
#### Toolkit Teste de Mutação: Mutmut - [Link](https://mutmut.readthedocs.io/en/latest/)

## Clonar e Configurar Projeto
  Primeiro será necessário fazer um clone do projeto para a sua máquina, e após clonar o
repositório, entre no diretório criado, usando os comandos abaixo:
```
$ git clone https://github.com/clarencesarmiento/CS50P-Final-Project.git
$ cd CS50P-Final-Project
```

  Logo em seguida, execute os comandos abaixo para instalar o python e as ferramentas
necessárias para rodar o projeto:
```
$ sudo apt update
$ sudo apt install python3 python3-pip
$ pip install -r requirements.txt
```

  Por fim rode o comando _python3 project.py_, e insira a string “Apr 01, 2000”. Assim o
programa irá te retornar a idade e os dias que faltam até o próximo aniversário, referente à data
adicionada.

<img src="https://github.com/user-attachments/assets/875a0f9c-94cc-4d5f-b0df-32f85acb93f3" width="400">

## Explicar o Projeto
  Para essa atividade foi escolhido o projeto de calculadora de idade, este programa
recebe como input a data de nascimento, no formato de “mês dia, ano” , e devolve como output a
idade calculada e os dias antes da data de aniversário.
  A idade é determinada, inicialmente, pela diferença entre o ano atual e o ano de
nascimento. Após isto, é avaliado se o mês de nascimento é maior que o mês atual, caso a
afirmação seja verdadeira, é retirada uma unidade da idade final, e retorna a idade final. Caso o
contrário, é avaliada mais uma afirmação, se o mês atual for igual ao mês de nascimento e o dia
atual for maior que o dia atual, é retirada uma unidade da idade final, e retorna a idade final. E
por fim, no cenário que nenhuma das afirmações anteriores foram verdadeiras, apenas retorna a
idade final. Na imagem abaixo é possível ver a função que calcula a idade.

<img src="https://github.com/user-attachments/assets/75d478ce-2ac2-49be-ad88-defa74871fc0" width="600">


  Já no cálculo dos dias que faltam para a data do aniversário, é avaliado se a data de
aniversário é menor que a data atual, caso seja verdadeira a afirmação, é feita a diferença entre
a data do aniversário do próximo ano e a data atual. Caso o contrário, se a data de aniversário
for maior que a data atual, é calculada a diferença entre a data de aniversário e a data atual. Na
imagem a seguir é apresentada a função que executa o cálculo dos dias.

<img src="https://github.com/user-attachments/assets/0b403c6e-a381-4b1c-9a72-c4d6e2224dad" width="550">


## Testes Unitários
Os testes unitários estão localizados no arquivo _test_project.py_. Para executar os testes
basta rodar o comando abaixo:
```
$ pytest
```

  Porém, ao executar os teste é retornado dois erros, demonstrados na imagem abaixo. O
desenvolvedor que criou o projeto, não se atentou à data que os testes estão sendo executados,
então, os testes passaram no dia que ele criou os testes, mas não não passa para qualquer
outro dia.

<img src="https://github.com/user-attachments/assets/3a6febd3-bc89-412f-8e42-46e975915c82" width="400">


  Para corrigir as falhas, vamos instalar a biblioteca _freezegun_, essa ferramenta fornece a
possibilidade de “congelar” a data que será considerada na execução do teste. Instale usando o
comando:
```
$ pip install freezegun
```

  Importe a biblioteca no arquivo de teste, adicionando:
```
from freezegun import freeze_time
```

  E também, adicionando a função que congela a data antes da declaração do caso de
teste:
```
@freeze_time("2023-08-21")
```

  Após as correções, a suite de teste passam sem nenhuma falha:

<img src="https://github.com/user-attachments/assets/f1cec6ed-3953-4c0c-afd2-85c67cf262e0" width="550">

Agora vamos gerar o relatório da cobertura de testes. Primeiro precisamos instalar o
plugin pytest-cov:
```
$ pip install pytest-cov
```

  Precisamos também reorganizar a estrutura dos códigos para conseguirmos executar o
comando que gera o relatório da cobertura de testes. Inicialmente crie e mova o arquivo
_“test_project.py”_, para a pasta _“test”_, e por fim crie um arquivo em branco com o nome
“__int__.py”. Por fim o novo arquivo ficará assim:

![image](https://github.com/user-attachments/assets/c7e3445a-6a4f-4d30-b339-7b34ca8e5d98)

Tudo pronto, agora vamos executar o comando para gerar o relatório:
```
$ pytest --cov=. --cov-report=html
```

  O resultado gerado é disponibilizado em HTML, apresentado na imagem abaixo:

  ![image](https://github.com/user-attachments/assets/56f1fd7e-5d87-4369-b9cc-4ff7b81b28e8)

## Testes de Mutação
  Por fim, vamos aplicar testes de mutação no projeto para conferir a qualidade dos testes
unitários. A ferramenta escolhida para realizar os testes de mutação foi o mutmut.
Para instalar execute no terminal o comando:
```
$ pip install mutmut
```

  Após a instalação, é preciso configurar a ferramenta, para isso criaremos um arquivo
chamado _“pyproject.toml”_, na raiz do projeto e adicione as seguintes informações:
```
[tool.mutmut]
paths_to_mutate="/diretorio/do/repositorio"
tests_dir="/diretorio/do/repositorio/test"
runner="pytest"
```

  E agora executamos os testes de mutação, com o comando :
```
$ mutmut run
```

  Como resultados temos 61 mutações que permaneceram vivas, de 91 mutações no total:

<img src="https://github.com/user-attachments/assets/3cf66703-b403-462d-a703-dc555251059e" width="600">

  E para gerar o relatório rodamos o comando:
```
$ mutmut html
```

  Com o relatório é possível identificar quais partes do código precisam de testes mais
eficazes, como por exemplo, a mutação 2, que muda uma linha na função main.

<img src="https://github.com/user-attachments/assets/99d96267-5123-4fbf-a35d-bc6c909deb5e" width="650">

No intuito de cobrir com teste unitário essa parte do código podemos, conferir se a
partir de um determinado input, a função retornará o output esperado. Para isso vamos
adicionar um novo caso de teste:
```
@freeze_time("2023-08-21")
def test_main_output(monkeypatch, capfd):
monkeypatch.setattr('sys.stdin', StringIO('October 20, 2000\n'))
main()
cature = capfd.readouterr()
assert "Your age as of August 21, 2023 is 22 years old." in cature.out
assert "60 days before your Birthday!" in cature.out
```

  E por último executamos novamente os testes de mutação, e geramos o relatório
para verificar que a mutação 2 foi eliminada. Após os testes vemos que a mutação 2 foi
eliminada e também outras mutações foram eliminadas apenas com o mesmo teste.

<img src="https://github.com/user-attachments/assets/c6cf7b17-b03f-4b86-91e5-8d6966f49b06" width="600">
