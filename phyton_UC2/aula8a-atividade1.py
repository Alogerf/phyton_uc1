def main():
   num1 = float(input("Digite o primeiro número: "))
   num2 = float(input("Digite o segundo número: "))
   soma = num1 + num2
  ## 
   print(f"A soma é: {soma}")




##

def par_ou_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
# Exemplo de chamada
print("O número 41 é", par_ou_impar(41))
print("O número 14 é", par_ou_impar(12))


##


def fatorial(n, metodo='iterativo'):


    if not isinstance(n, int):
        raise TypeError("A entrada deve ser um número inteiro.")
    if n < 0:
        raise ValueError("Não é possível calcular o fatorial de um número negativo.")

    if metodo == 'iterativo':
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    elif metodo == 'recursivo':
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1, metodo='recursivo')

    else:
        raise ValueError("Método inválido. Use 'iterativo' ou 'recursivo'.")

print("Fatorial de 5 (iterativo):", fatorial(5, metodo='iterativo'))






## 

def media(lista):
    return sum(lista) / len(lista)
valores = [10, 15, 34, 21]
print("A média é:", media(valores))




##

def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1] 
print("ana é palíndromo?", eh_palindromo("ana")