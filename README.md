# Projeto de Fundamentos de Projeto e Análise de Algoritmos - Implementação do Algoritmo de Karatsuba em Python

## Sobre o Projeto
Este projeto consiste na implementação do algoritmo de Karatsuba em Python para a multiplicação eficiente de números inteiros grandes. O algoritmo de Karatsuba utiliza a estratégia de "dividir para conquistar" para realizar a multiplicação com uma complexidade assintótica melhor do que o algoritmo de multiplicação tradicional. Então, em vez de fazer uma multiplicação gigante, ele a transforma em três multiplicações menores e algumas somas.

### Lógica do Algoritmo Implementado
O código trata os números como texto (strings), para que se possa trabalhar com números gigantes sem limites. Basicamente, se os números inseridos para multiplicar forem pequenos (com menos de 4 dígitos), o algoritmo só multiplica eles normalmente e retorna o resultado. 

Porém, se os números forem grandes, o algoritmo:
1. Verifica o tamanho do maior número e, se for ímpar, ele "arredonda" para o próximo número par. Depois, ele adiciona zeros à esquerda no número menor até que os dois fiquem com o mesmo tamanho. Isso simplifica a divisão dos números em duas metades de tamanho igual. Exemplo: 12345 e 6789 viram 012345 e 006789.
2. Posteriormente, divide ambos ao meio. Exemplo: 012345 vira Al = "012" e Ar = "345".
3. Realiza 3 contas: multiplica as metades da esquerda dos dois números; multiplica as metades da direita; soma as metades de cada número inicial e multiplica os resultados dessa soma.
4. Soma os resultados das 3 contas, de modo que adiciona zeros à direita de alguns para alinhar as casas decimais e retorna o resultado.
