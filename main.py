from re import X
from webbrowser import get


curso = {
    "nome": "Programando em python",
    "conteudos": [
        "Conceitos básicos da linguagem",
        "Biblioteca-padrão",
        "Coleções",
        "Estruturas de controle",
        "Funções e módulos",
        "Parâmetros default, variáveis e nomeados",
        "Programação funcional",
        "Classes e Objetos",
        "Herança e Polimorfismo",
        "Armazenamento de dados em arquivos",
        "Acesso a banco de dados",
        "Manipulação de API Rest",
        "Testes unitários"
                  ],
    "instrutor": {
        "Nome": "Júlio Pereira",
        "Contato": "33 99154-2651"
    },
    "alunos": [
        "Aldair Ribeiro",
        "André de Castro",
        "Danilo Pereira",
        "Elton Lima",
        "Fabio Ferraz",
        "Gideão Sudario",
        "Jefferson André",
        "Jeova Vieira",
        "Lucas Pires",
        "Marcelo São Pedro",
        "Meggy Mendes",
        "Michael Rochumback",
        "Nilza Ferreira",
        "Paulo Sergio"
    ]
}

# ========= USANDO  APENAS METHODOS, IF OU LIST COMPREENSHIONS

# CRIAR OS CONJUNTOS

# 1 - Lista de todas as keys do curso

keys_curso = [x for x in curso]
print(keys_curso)   

# 2 - Lista de tuplas para criar 5 relacionamento entre os alunos

import random as r #renomeia random para r
num_a = r.sample([1, 2, 3, 4, 5], k=2)
print (num_a)

# 3 - Lista com os nomes dos alunos

lista_alunos = [x for x in curso["alunos"]]
print(lista_alunos)

# 4 - Lista com os nomes dos alunos MOSTRANDO APENAS AS TRÊS PRIMEIRAS LETRAS

lista_alunos_3_letras = [x[0:3] for x in curso["alunos"]]
print(lista_alunos_3_letras)

# 5 - Lista de conteudos que COMECA COM A LETRA A

conteudos_a = [x for x in curso["conteudos"] if x[0] == 'A' or x[0] == 'a']
print(conteudos_a)

# ========= USANDO APENAS METHODOS, IF OU WHILE

conteudo_while = []

# 1 - Preencher o conjunto conteudo_while com uma lista de dicionarios dos conteudos conforme o exemplo:
# Exemplo: [{nome: "Conceitos básicos da linguagem", active: True}]

x = 0 

len(curso["conteudos"])

while x < len(curso["conteudos"]):
    conteudo_while.append({'nome':curso["conteudos"][x], 'active': True})
    x += 1

print(conteudo_while)

# ========= USANDO APENAS METHODOS, IF OU FOR

curso_for = {}
alunos_for = []
conteudos_for = []
instrutor_for = {}

# 1 - preenche a coleção curso_for com os dados do curso e acrecenta o atributo active com valor true

for x in curso.items:
    curso_for[x[0]] = x [1]
    
    curso_for['active'] = True
    

# 2 - preenche a coleção alunos_for com os nomes dos alunos.

for x in curso["alunos"]:
    alunos_for.append(x)
    print(alunos_for)
    

# 3 - preenche a coleção conteudos_for com os dados dos conteudos.

for x in curso["conteudos"]:
    conteudos_for.append(x)
print(conteudos_for)

# 4 - preenche a coleção instrutor_for com os dados dos instrutor e acrecentar os meios de contatos

for x in curso["instrutor"].items():
    instrutor_for[x[0]] = x[1]
instrutor_for['GitHub'] = 'http://'

# 5 - faça uma busca na coleção curso_for e imprime apenas os dados do instrutor

for x in curso_for["instrutor"].items():
    print(x)

# 6 - faça uma busca na coleção alunos e imprime o aluno com index 5

for x in alunos_for:
    if x == alunos_for[5]:
        print(x)

# 7 - Faça uma leitura na coleção conteudos_for ALTERANDO todos conteudos a partir do index 6 para "NÃO APLICADO"

for x in conteudos_for:
    if x == conteudos_for.index(x) > 5:
        conteudos_for[conteudos_for.index(x)] = 'Nao Aplicado'
        print(conteudos_for)
