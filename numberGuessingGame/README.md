JOGO DE ADIVINHAÇÃO DE NÚMEROS EM PYTHON 3

A maioria dos geeks com formação em CS ( Ciência da Computação ) pensa em seu primeiro projeto depois de fazer uma Linguagem de Programação. Aqui, você obterá seu primeiro projeto e o básico, neste artigo.

Tarefa: Abaixo estão as etapas:

Construa um jogo de adivinhação de números, no qual o usuário seleciona um intervalo.
Digamos que o usuário tenha selecionado um intervalo, ou seja, de A a B , onde A e B pertencem a inteiro.
Algum inteiro aleatório será selecionado pelo sistema e o usuário deve adivinhar esse inteiro no número mínimo de adivinhações
Análise:

Explicação 1 : Se as entradas do usuário variam, digamos de 1 a 100. E o compilador selecionou aleatoriamente 42 como o inteiro. E agora o jogo de adivinhação começou, então o usuário inseriu 50 como sua primeira estimativa . O compilador mostra “Tente novamente! Você adivinhou muito alto ”. Isso significa que o número aleatório (ou seja, 42) não cai na faixa de 50 a 100. Essa é a importância de adivinhar a metade da faixa. E novamente, o usuário adivinha metade de 50 (você poderia me dizer por quê?). Portanto, a metade de 50 é 25. O usuário insere 25 como sua segunda estimativa. Desta vez, o compilador mostrará “Tente novamente! Você adivinhou muito pequeno ”. Isso significa que os inteiros menores que 25 (de 1 a 25) são inúteis para serem adivinhados. Agora o intervalo de adivinhação do usuário é menor, ou seja, de 25 a 50. Inteligentemente! O usuário adivinhou a metade desse intervalo, de modo que o usuário adivinhou 37 como sua terceira estimativa . Desta vez, novamente o compilador mostra a saída, “Tente novamente! Você adivinhou muito pequeno ”. Para o usuário, o intervalo de adivinhação está ficando menor a cada adivinhação. Agora, o intervalo de adivinhação para o usuário é de 37 a 50, para o qual o usuário adivinhou 43 como sua quarta estimativa . Desta vez, o compilador mostrará uma saída “Tente novamente! Você adivinhou muito alto ”. Assim, o novo intervalo de suposição para os usuários será de 37 a 43, novamente para o qual o usuário adivinhou a metade desse intervalo, ou seja, 40 como seuquinto palpite . Desta vez, o compilador mostra a saída, “Tente novamente! Você adivinhou muito pequeno ”. Deixando a estimativa ainda menor, de 41 a 43. E agora o usuário adivinhou 41 como sua sexta estimativa . O que está errado e mostra a saída “Tente novamente! Você adivinhou muito pequeno ”. E, finalmente, o usuário adivinhou o número certo, que é 42 como sua sétima estimativa .

Número total de estimativas = 7

Explicação 2 : Se as entradas do usuário variam, digamos de 1 a 50. E o compilador selecionou aleatoriamente 42 como o inteiro. E agora o jogo de adivinhação começou. Portanto, a metade de 50 é 25. O usuário insere 25 como sua primeira estimativa . Desta vez, o compilador mostrará “Tente novamente! Você adivinhou muito pequeno ”. Isso significa que os inteiros menores que 25 (de 1 a 25) são inúteis para serem adivinhados. Agora o intervalo de adivinhação do usuário é menor, ou seja, de 25 a 50. Inteligentemente! O usuário adivinhou metade desse intervalo, de modo que o usuário adivinhou 37 como sua segunda estimativa . Desta vez, novamente o compilador mostra a saída, “Tente novamente! Você adivinhou muito pequeno ”. Para o usuário, o intervalo de adivinhação está ficando menor a cada adivinhação. Agora, o intervalo de adivinhação para o usuário é de 37 a 50, para o qual o usuário adivinhou 43 como seuterceira suposição . Desta vez, o compilador mostrará uma saída “Tente novamente! Você adivinhou muito alto ”. Portanto, o novo intervalo de adivinhação para usuários será de 37 a 43, novamente para o qual o usuário adivinhou a metade desse intervalo, ou seja, 40 como sua quarta estimativa . Desta vez, o compilador mostra a saída, “Tente novamente! Você adivinhou muito pequeno ”. Deixando a estimativa ainda menor, de 41 a 43. E agora o usuário adivinhou 41 como sua quinta estimativa. O que está errado e mostra a saída “Tente novamente! Você adivinhou muito pequeno ”. E, finalmente, o usuário adivinhou o número certo, que é 42 como sua sexta estimativa.

Número total de estimativas = 6

Portanto, o número mínimo de suposições depende do intervalo. E o compilador deve calcular o número mínimo de suposições que depende do intervalo, por conta própria. Para isso, temos uma fórmula: -

Número mínimo de adivinhação = log 2 (limite superior - limite inferior + 1)

Algoritmo : Abaixo estão as etapas:
O usuário insere o limite inferior e o limite superior do intervalo.
O compilador gera um inteiro aleatório entre o intervalo e o armazena em uma variável para referências futuras.
Para adivinhação repetitiva, um loop while será inicializado.
Se o usuário adivinhou um número maior do que um número selecionado aleatoriamente, o usuário obtém uma saída “ Tente novamente! Você adivinhou muito alto “
Caso contrário, se o usuário adivinhou um número menor do que um número selecionado aleatoriamente, o usuário obtém uma saída “ Tente novamente! Você adivinhou muito pequeno ”
E se o usuário adivinhou um número mínimo de adivinhações, o usuário recebe um “ Parabéns! " Resultado.
Do contrário, se o usuário não adivinhou o número inteiro no número mínimo de adivinhações, ele receberá “ Melhor sorte na próxima vez! " resultado.