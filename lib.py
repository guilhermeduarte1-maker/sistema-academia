# lib.py
import csv

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

def escrever_csv(dados, arquivo, campos):
    with open(arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(campos)
        writer.writerows(dados)

# Funções de Alunos
def adicionar_aluno(alunos, nome, plano, vencimento):
    alunos.append([nome, plano, vencimento])

def listar(dados):
    return dados

def remover_aluno(alunos, nome):
    for aluno in alunos:
        if aluno[0].lower() == nome.lower():
            alunos.remove(aluno)
            return True
    return False

# Funções de Treinos
def adicionar_treino(treinos, aluno, exercicio, series, repeticoes):
    treinos.append([aluno, exercicio, series, repeticoes])
    
def listar_treinos(treinos):
    return treinos

def consultar_treinos(treinos, aluno):
    return [treino for treino in treinos if treino[0].lower() == aluno.lower()]

def consultar_aluno(alunos, nome):
    return [aluno for aluno in alunos if aluno[0].lower() == nome.lower()]

def alterar_treino(treinos, aluno, exercicio, novas_series, novas_repeticoes):
    for treino in treinos:
        if treino[0].lower() == aluno.lower() and treino[1].lower() == exercicio.lower():
            treino[2] = novas_series
            treino[3] = novas_repeticoes
            return True
    return False

def excluir_treino(treinos, aluno, exercicio):
    for treino in treinos:
        if treino[0].lower() == aluno.lower() and treino[1].lower() == exercicio.lower():
            treinos.remove(treino)
            return True
    return False

