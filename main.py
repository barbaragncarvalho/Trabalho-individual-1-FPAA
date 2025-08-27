import re

# função para encontrar a soma dos maiores números representados como string
def findSum(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    resultado = ""
    n1, n2 = len(str1), len(str2)
    str1, str2 = str1.zfill(n2), str2.zfill(n2)
    carry = 0

    # Faz a adição de dígito por dígito da direita para esquerda
    for i in range(n2 - 1, -1, -1):
        sum_val = (int(str1[i]) - 0) + (int(str2[i]) - 0) + carry
        resultado = str(sum_val % 10 + 0) + resultado
        carry = sum_val // 10

    if carry:
        resultado = str(carry + 0) + resultado

    return resultado

# função para encontrar a diferença de maiores números representados como strings
def findDiff(str1, str2):
    resultado = ""
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
        resultado = str(sub + 0) + resultado

    return resultado

# Função para remover todos os zeros iniciais de uma string
def removeLeadingZeros(s):
    pattern = "^0+(?!$)"
    s = re.sub(pattern, "", s)
    return s

# Função para multiplicar dois números usando o Karatsuba
def multiply(A, B):
    if len(A) < 4 or len(B) < 4:
        return str(int(A) * int(B))

    # Garante que 'n' seja par para uma divisão simétrica
    n = max(len(A), len(B))
    if n % 2 != 0:
        n += 1
    
    A = A.zfill(n)
    B = B.zfill(n)

    n2 = n // 2

    # Divide os números pela metade
    Al, Ar = A[:n2], A[n2:]
    Bl, Br = B[:n2], B[n2:]

    p = multiply(Al, Bl)
    q = multiply(Ar, Br)
    soma_A = findSum(Al, Ar)
    soma_B = findSum(Bl, Br)
    r = multiply(soma_A, soma_B)

    termo_meio = findDiff(r, findSum(p, q))

    resultado_p = p + '0' * n
    resultado_r = termo_meio + '0' * n2
    
    resultado_final = findSum(findSum(resultado_p, resultado_r), q)

    return removeLeadingZeros(resultado_final)

if __name__ == "__main__":
    A = "12345"
    B = "6789"
    print(multiply(A, B)) 