import geometria

def main():

    print("--- Calculadora de Areas ---")
    print("1. Calcular area do retangulo")
    print("2. Calcular area do triangulo")
    print("3. Calcular area do circulo")
    print("4. Sair")
    
    escolha = int(input("Escolha uma opção entre (1-4): "))
    
    if escolha == 1:
         base = float(input("Digite a base do retângulo: "))
         altura = float(input("Digite a altura do retângulo: "))
         area = geometria.calcular_area_retangulo(base, altura)
         print(f"A área do retângulo é: {area:.2f}")
    elif escolha == 2:
         base = float(input("Digite a base do triângulo: "))
         altura = float(input("Digite a altura do triângulo: "))
         area = geometria.calcular_area_triangulo(base, altura)
         print(f"A área do triângulo é: {area:.2f}")
    elif escolha == 3:
         raio = float(input("Digite o raio do círculo: "))
         area = geometria.calcular_area_circulo(raio)
         print(f"A área do círculo é: {area:.2f}")
    elif escolha == 4:
        print("Saindo da calculadora.")
    else:
         print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
         
main()
