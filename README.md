Sistema de Academia

Projeto final da disciplina Introdução a Programação – IFRN.

Reitor: Demetrios Araujo Magalhaes Coutinho

Aluno
- José Guilherme Duarte da Silva 


Descrição
Este projeto simula um sistema de academia.  
Ele permite cadastrar alunos e treinos, consultar, alterar e excluir informações.  
Os dados são armazenados em arquivos CSV.

Funcionalidades
- Cadastrar aluno (nome, plano, vencimento)
- Listar alunos
- Remover aluno
- Cadastrar treino (aluno, exercício, séries, repetições)
- Listar treinos
- Consultar treinos por aluno
- Alterar treino
- Excluir treino

Estrutura do Projeto
- `main.py` → contém o menu principal e interação com o usuário (arquivo principal, deve ser executado para iniciar o sistema)
- `lib.py` → funções para manipulação de alunos, treinos e arquivos
- `alunos.csv` → lista de alunos cadastrados
- `treinos.csv` → lista de treinos cadastrados

Como executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/guilhermeduarte1-maker/sistema-academia.git
