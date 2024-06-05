def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n-1)

def main():
    num = int(input("Digite um número inteiro positivo: "))
    if num < 0:
        print("Erro: O número deve ser positivo.")
        return
    print(f"O fatorial de {num} é {calcular_fatorial(num)}")

if __name__ == "__main__":
    main()
