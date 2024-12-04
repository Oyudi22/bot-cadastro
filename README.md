# Automação de Cadastro

Bot de cadastro feito em Python com a biblioteca PyAutoGUI e Time, para incluir funcionários em um sistema, coletando informações para a criação dos e-mails.
O programa inicia lendo um arquivo especificado dentro da função open(). Sendo um arquivo Txt, separando as informações por vírgulas.

O programa começa lendo as informações de um arquivo especificado e transformando em uma variável "file".
`with open('nome.txt', 'r', encoding="UTF-8") as file:`

Nesse arquivo que está sendo interpretado pelo programa, é formatado da seguinte maneira
`Nome, Sobrenome, UltimoSobrenome, CPF`

Lendo e guardando as informações na variável file, um laço for é chamado para que o programa só termine
caso todos os e-mail sejam feitos
`for linha in file:`

Antes do programa realizar o cadastro, ele define 5 variáveis: nome, nome2, sobrenome, cpf e senha.
Em todas as variáveis, é usado a função split(), separando cada informação pelo caractere selecionado e para as variáveis que coletam as informações, 
é definido um índice para sua respectiva variável, exemplo:
`nome = linha.split(',')[0]`

```
nome = linha.split(',')[0]
nome2 = linha.split(',')[1]
sobrenome = linha.split(',')[2]
cpf = linha.split(',')[3]
senha = 12345678
```

A partir dessa definição, cada bloco de comandos é separado para uma função, como:
Selecionar o botão de cadastro, Escrever o Nome, Sobrenome, Digitação do E-mail, Seleção do cargo,
Definição da Senha, Finalização do Cadastro, Seleção do email criado, Copia e cola em um arquivo e Pula para próxima linha.

Com esse bot, eu consegui realizar o cadastro de mais de 100 estagiários em 30 minutos, o que demoraria para fazer a mão umas 2 horas
