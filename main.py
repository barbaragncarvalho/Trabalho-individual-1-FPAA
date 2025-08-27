import re

# função para encontrar a soma dos maiores números representados como string
def findSum(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    result = ""
    n1, n2 = len(str1), len(str2)
    str1, str2 = str1.zfill(n2), str2.zfill(n2)
    carry = 0

    # Faz a adição de dígito por dígito da direita para esquerda
    for i in range(n2 - 1, -1, -1):
        sum_val = (int(str1[i]) - 0) + (int(str2[i]) - 0) + carry
        result = str(sum_val % 10 + 0) + result
        carry = sum_val // 10

    if carry:
        result = str(carry + 0) + result

    return result

# função para encontrar a diferença de maiores números representados como strings
def findDiff(str1, str2):
    result = ""
    n1, n2 = len(str1), len(str2)
    str1, str2 = str1.zfill(n2), str2.zfill(n2)
    carry = 0

    # Faz a subtração de dígito por dígito da direita
    for i in range(n2 - 1, -1, -1):
        sub = (int(str1[i]) - 0) - (int(str2[i]) - 0) - carry

        if sub < 0:
            sub += 10
            carry = 1
        else:
            carry = 0

        # Acrescenta o dígito ao resultado
        result = str(sub + 0) + result

    return result

# Função para remover todos os zeros iniciais de uma string
def removeLeadingZeros(s):
    pattern = "^0+(?!$)"
    s = re.sub(pattern, "", s)
    return s

# Função para multiplicar dois números usando o Karatsuba
def multiply(A, B):
    # Caso base para números pequenos: realiza multiplicação normal
    if len(A) < 10 or len(B) < 10:
        return str(int(A) * int(B))

    n = max(len(A), len(B))
    n2 = n // 2

    # Preenche os números com zeros à esquerda para que fiquem com mesmo comprimento
    A = A.zfill(n)
    B = B.zfill(n)

    # Divide os números pela metade
    Al, Ar = A[:n2], A[n2:]
    Bl, Br = B[:n2], B[n2:]

    # Calcula recursivamente produtos parciais e soma usando o Karatsuba
    p = multiply(Al, Bl)
    q = multiply(Ar, Br)
    r = multiply(findSum(Al, Ar), findSum(Bl, Br))
    r = findDiff(r, findSum(p, q))

    # Combina os produtos parciais para obter o resultado final
    return removeLeadingZeros(findSum(findSum(p + '0' * n, r + '0' * n2), q))

if __name__ == "__main__":
    A = "458933"
    B = "5439"

    print(multiply(A, B))