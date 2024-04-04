import math

lado_a = float(input("informe o primeiro lado do triângulo: "))
lado_b = float(input("informe o segundo lado do triângulo: "))
lado_c = float(input("informe o terceiro lado do triângulo: "))

s = (lado_a + lado_b + lado_c) / 2

area = math.sqrt((s * (s - lado_a) * (s - lado_b) * (s - lado_c)))
print(f"Área do triângulo: {area:.1f}")
