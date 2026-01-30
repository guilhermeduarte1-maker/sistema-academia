# lib.py
import csv

#essa funcao le os arquivos csv e retorna uma lista de listas(matriz)
def ler_csv(arquivo):
    dados = []
    try:
        with open(arquivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                dados.append(row)
    except FileNotFoundError:
        pass
    return dados

#essa funcao escreve os dados na matriz de volta para o arquivo csv
def escrever_csv(dados, arquivo, campos):
    with open(arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(campos)
        writer.writerows(dados)

# Funções de Alunos

#essa funcao adiciona um novo aluno na matriz de alunos
def adicionar_aluno(alunos, nome, plano, vencimento):
    alunos.append([nome, plano, vencimento])

#essa funcao lista os alunos cadastrados
def listar(dados):
    return dados

#essa funcao remove um aluno da matriz de alunos
def remover_aluno(alunos, nome):
    for aluno in alunos:
        if aluno[0].lower() == nome.lower():
            alunos.remove(aluno)
            return True
    return False

# Funções de Treinos

#essa funcao adiciona um novo treino na matriz de treinos
def adicionar_treino(treinos, aluno, exercicio, series, repeticoes):
    treinos.append([aluno, exercicio, series, repeticoes])

#essa funcao lista os treinos cadastrados
def listar_treinos(treinos):
    return treinos

#essa funcao consulta os treinos de um aluno especifico
def consultar_treinos(treinos, aluno):
    return [treino for treino in treinos if treino[0].lower() == aluno.lower()]

#essa funcao consulta um aluno especifico
def consultar_aluno(alunos, nome):
    return [aluno for aluno in alunos if aluno[0].lower() == nome.lower()]

#essa funcao altera as series e repeticoes de um treino ja cadastrado
def alterar_treino(treinos, aluno, exercicio, novas_series, novas_repeticoes):
    for treino in treinos:
        if treino[0].lower() == aluno.lower() and treino[1].lower() == exercicio.lower():
            treino[2] = novas_series
            treino[3] = novas_repeticoes
            return True
    return False

#essa funcao exclui um treino cadastrado
def excluir_treino(treinos, aluno, exercicio):
    for treino in treinos:
        if treino[0].lower() == aluno.lower() and treino[1].lower() == exercicio.lower():
            treinos.remove(treino)
            return True
    return False

