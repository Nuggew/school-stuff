# Sinceramente prof, só fazer um questionario de pergunta e digitar resposta é muito facil e até ineficiente ao usuário, por isso eu dei uma melhorada no sistema que vc provavelmente queria, dá uma olhada aí
# tá em inglês por preferência minha, tem algumas explicações pra ficar mais simples o meu código pra vc sem precisar ficar lendo ;)

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
questions = [ #[ PERGUNTA, [ [RESPOSTAS, CORRETA?] ] ]
    ["O que é overclocking?", [
        ["Reduzir a frequência do processador para economizar energia", False],
        ["Aumentar a frequência de operação de um componente além das especificações de fábrica", True],
        ["Aumentar a capacidade de armazenamento do computador", False],
        ["Substituir a memória RAM por uma mais rápida", False],
    ]],
    ["Qual é um dos principais motivos para realizar overclock em um processador?", [
        ["Diminuir o desempenho", False],
        ["Reduzir a temperatura do computador", False],
        ["Obter maior desempenho em tarefas e jogos", True],
        ["Diminuir a quantidade de memória RAM utilizada", False],
    ]],
    ["Qual componente é especialmente importante para manter a estabilidade durante um overclock?", [
        ["Sistema de refrigeração (air/water cooler)", True],
        ["Monitor", False],
        ["Teclado", False],
        ["Placa de som", False],
    ]],
    ["O aumento excessivo da tensão de um processador pode:", [
        ["Reduzir permanentemente sua temperatura", False],
        ["Aumentar o consumo de energia e a temperatura, podendo causar danos", True],
        ["Aumentar a capacidade do SSD", False],
        ["Impedir que a memória RAM seja utilizada", False],
    ]],
    ["O que pode acontecer quando um overclock não está estável?", [
        ["O computador pode apresentar travamentos, erros ou reinicializações", True],
        ["O computador sempre terá maior duração da bateria", False],
        ["O armazenamento ficará automaticamente mais rápido", False],
        ["A capacidade da RAM será duplicada", False],
    ]],
    ["Qual é uma boa prática ao fazer overclock?", [
        ["Aumentar frequência e tensão ao máximo imediatamente", False],
        ["Ignorar as temperaturas do componente", False],
        ["Fazer alterações gradualmente e testar a estabilidade e as temperaturas", True],
        ["Desativar todos os sistemas de proteção da placa-mãe", False],
    ]],
]

correctAnswers = 0

questionId = 0
while (questionId < len(questions)):
    question = questions[questionId]

    print("\n\n=== PERGUNTA", questionId+1, "===")
    print(question[0]) #cabeçalho

    correctAnswer = None
    answerId = 0
    for answer in question[1]: #passa pelas respostas da pergunta
        letter = alfabeto[answerId]
        print(letter.capitalize() + ")", answer[0]) #pergunta enumerada com letra tipo A)
        if answer[1] == True:
            correctAnswer = letter
        answerId += 1

    if correctAnswer == None:
        print("Essa questão tem um erro de formatação por parte do criador do quiz.")
        questionId += 1
        continue

    userAnswer = input(">> ") #pega a resposta do usuário
    if correctAnswer == userAnswer.lower():
        print("\n[Correto!]\n")
        correctAnswers += 1
    else:
        print("\n[Errado!]\n")

    questionId += 1

print("\n\n=== ESTATÍSTICAS ===")
print("Respostas certas:", str(correctAnswers))
print("Respostas erradas:", str(len(questions) - correctAnswers))
print("Nota:", str(correctAnswers) + "/" + str(len(questions)))