#tarefa da urna eletronica
# Fiz de um jeito diferente do passado em aula pois é a logica que me dou melhor até agora, então vou mandar os dois exemplos.

candidatos = []

while True:
    print('='*20)
    print("Urna Eletrônica")
    print("1. Adicionar Candidato")
    print("2. Remover Candidato")
    print("3. Listar Candidatos")
    print("4. Sair")
    print('='*20)

    opcao = input("Escolha uma opção: ")

    if opcao == "1": #Adicionar candidato
        nome = input("Digite o nome do candidato: ")
        partido = input("Digite o partido do candidato: ")
        candidato = {"nome": nome, "partido": partido}
        candidatos.append(candidato)
        print("Candidato adicionado com sucesso!")

    elif opcao == "2": #Remover candidato
        nome = input("Digite o nome do candidato que deseja remover: ")
        removido = False
        for candidato in candidatos:
            if candidato["nome"] == nome:
                candidatos.remove(candidato)
                print("Candidato removido com sucesso!")
                removido = True
                break
        if not removido:
            print("Candidato não encontrado!")
    elif opcao == "3": #listar candidatos incluidos na lista
        print("Lista de Candidatos:")
        for candidato in candidatos:
            print("Nome: ", candidato["nome"], "Partido: ", candidato["partido"])
    elif opcao == "4": # encerra o programa
        print("Encerrando Urna Eletrônica...")
        break
    else: 
        print("Opção inválida, tente novamente!")
