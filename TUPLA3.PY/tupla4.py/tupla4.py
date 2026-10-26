# 3. Tuplas são imutáveis
print("="*60 + "\n")

print("3. TUPLAS SÃO IMUTÁVEIS:\n")

tupla = (1, 2, 3)
print(f"Tupla original: {tupla}\n")

print("Tentando modificar:")
try:
    tupla[0] = 99
except TypeError as e:
    print(f"Erro: {e}\n")

print("Tentando adicionar:")
try:
    tupla.append(4)
except AttributeError as e:
    print(f"Erro: Tuplas não têm append\n")

print("✓ Tuplas são imutáveis (proteção de dados)")
print("✓ Listas podem ser modificadas\n")

print("="*60 + "\n")

#CADASTRO
print("CADASTRO COM TUPLA:\n")

#(nome, cpf, idade, email)
pessoa = ("Maria Silva", "123.456.789-00", 25, "maria@email.com")

nome, cpf, idade, email = pessoa

print("---DADOS DO CADASTRO---")
print(f"Nome:  {nome}")
print(f"CPF:   {cpf}")
print(f"Idade: {idade}")
print(f"Email: {email}\n")

print("Tentando modificar:")
try:
    tupla[0] = 99
except TypeError as e:
    print(f"Erro: {e}\n")


print("Tentando alterar o CPF:")
try:
    pessoa[1] = "000.000.000-00"
except TypeError as e:
    print(f"Erro: {e}\n")

print("✓ Os dados do cadastro estão protegidos contra alteração")
print("="*60 + "\n")