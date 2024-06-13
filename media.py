def validar_nota(num):
  nota = float(input(f"Digite a nota {num}: "))
  while nota < 0 or nota > 10:
    print("Nota inválida! Digite um valor entre 0 e 10.")
    nota = float(input(f"Digite a nota {num}: "))
  return nota

print("Notas do Estudante")
nota1 = validar_nota(1)
nota2 = validar_nota(2)
nota3 = validar_nota(3)

notas = [nota1, nota2, nota3]
soma = sum(notas)
media = soma / len(notas)

print(f"Sua média é: {media:.2f}")

if media >=6:
  print("Estudante aprovado")
else:
  print("Estudante reprovado")
