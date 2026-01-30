# main.py
import lib
import rich.console
console = rich.console.Console()

def main():
    arquivo_alunos = 'alunos.csv'
    arquivo_treinos = 'treinos.csv'

    alunos = lib.ler_csv(arquivo_alunos)
    treinos = lib.ler_csv(arquivo_treinos)

    while True:
        console.print("[bold green]\nSistema de Academia[/bold green]")
        console.print("1.[green] Cadastrar Aluno[/green]")
        console.print("2.[green] Listar Alunos[/green]")
        console.print("3.[green] Cadastrar Treino[/green]")
        console.print("4.[green] Listar Treinos[/green]")
        console.print("5.[green] Consultar Treinos por Aluno[/green]")
        console.print("6.[green] Alterar séries e repetições do Treino[/green]")
        console.print("7.[red] Excluir Treino[/red]")
        console.print("8.[red] Remover Aluno[/red]")
        console.print("9.[bold red] Sair do sistema[/bold red]")

        escolha = input("Escolha uma opção: ")

        #essa funcao lista os alunos cadastrados
        if escolha == '1':
            nome = input("\nNome do aluno: ")
            plano = input("Plano (Mensal/Trimestral/Anual): ")
            vencimento = input("Data de vencimento (dd/mm/aaaa): ")
            lib.adicionar_aluno(alunos, nome, plano, vencimento)
            lib.escrever_csv(alunos, arquivo_alunos, ['Nome', 'Plano', 'Vencimento'])
            console.print(f"[green]Aluno '{nome}' cadastrado com sucesso![/green]")
        
        #essa funcao lista os alunos cadastrados
        elif escolha == '2':
            console.print("\n[bold green]Alunos cadastrados:[/bold green]")
            lista = lib.listar(alunos)
            if not lista:
                console.print("[red]Nenhum aluno cadastrado.[/red]")
            else:
                for i, aluno in enumerate(lista, start=1):
                    console.print(f"[cyan]{i}.[/cyan] {aluno[0]} - {aluno[1]} (Vencimento: [yellow]{aluno[2]}[/yellow])")
                    
        #essa funcao cadastra treinos para os alunos ja cadastrados
        elif escolha == '3':
            aluno = input("\nNome do aluno: ")
            lista = lib.consultar_aluno(alunos, aluno)
            if not lista:
                console.print(f"[red]Aluno {aluno} não encontrado. Cadastre o aluno antes de adicionar um treino.[/red]")
                continue
            exercicio = input("Exercício: ")
            series = input("Séries: ")
            repeticoes = input("Repetições: ")
            lib.adicionar_treino(treinos, aluno, exercicio, series, repeticoes)
            lib.escrever_csv(treinos, arquivo_treinos, ['Aluno', 'Exercício', 'Séries', 'Repetições'])
            console.print(f"[green]Treino para '{aluno}' cadastrado com sucesso![/green]")

        #essa funcao lista os treinos cadastrados
        elif escolha == '4':
            console.print("\n[bold green]Treinos cadastrados:[/bold green]")
            lista = lib.listar_treinos(treinos)
            if not lista:
                console.print("[red]Nenhum treino cadastrado.[/red]")
                continue
            for i, treino in enumerate(lista, start=1):
                console.print(f"[cyan]{i}.[/cyan] {treino[0]} - {treino[1]} ([yellow]{treino[2]} séries[/yellow] de [yellow]{treino[3]} repetições[/yellow])")

        #essa funcao consulta os treinos de um aluno especifico
        elif escolha == '5':
            aluno = input("\nNome do aluno: ")
            lista = lib.consultar_treinos(treinos, aluno)
            if not lista:
                console.print("[red]Nenhum treino encontrado para esse aluno.[/red]")
            else:
                console.print(f"\n[bold green]Treinos de {aluno}:[/bold green]")
                for treino in lista:
                    console.print(f"- {treino[1]} ([yellow]{treino[2]} séries[/yellow] de [yellow]{treino[3]} repetições[/yellow])")

        #essa funcao altera as series e repeticoes de um treino ja cadastrado
        elif escolha == '6':
            aluno = input("\nNome do aluno: ")
            exercicio = input("Exercício a alterar séries e repetições: ")
            novas_series = input("Novas séries: ")
            novas_repeticoes = input("Novas repetições: ")
            if lib.alterar_treino(treinos, aluno, exercicio, novas_series, novas_repeticoes):
                lib.escrever_csv(treinos, arquivo_treinos, ['Aluno', 'Exercício', 'Séries', 'Repetições'])
                console.print("[green]Treino alterado com sucesso![/green]")
            else:
                console.print("[red]Treino não encontrado.[/red]")

        #essa funcao exclui um treino cadastrado
        elif escolha == '7':
            aluno = input("\nNome do aluno: ")
            exercicio = input("Exercício a excluir: ")
            if lib.excluir_treino(treinos, aluno, exercicio):
                lib.escrever_csv(treinos, arquivo_treinos, ['Aluno', 'Exercício', 'Séries', 'Repetições'])
                console.print("[green]Treino excluído com sucesso![/green]")
            else:
                console.print("[red]Treino não encontrado.[/red]")

        #essa funcao remove um aluno cadastrado
        elif escolha == '8':
            nome = input("\nNome do aluno a remover: ")
            if lib.remover_aluno(alunos, nome):
                lib.escrever_csv(alunos, arquivo_alunos, ['Nome', 'Plano', 'Vencimento'])
                console.print(f"[green]Aluno '{nome}' removido com sucesso![/green]")
            else:
                console.print("[red]Aluno não encontrado.[/red]")

        #essa funcao encerra o programa
        elif escolha == '9':
            console.print("[bold red]\nSaindo do sistema... Até breve![/bold red]")
            break

        else:
            console.print("[red]Opção inválida! Escolha novamente.[/red]")

if __name__ == '__main__':
    main()
