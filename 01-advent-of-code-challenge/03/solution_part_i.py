# lê o arquivo com os dados de entrada
with open("sample.in", "r") as f:
    data = f.read().splitlines()

# define uma função para converter letras em suas prioridades
def get_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

# percorre cada rucksack
total_priority = 0
for rucksack in data:
    # divide o conteúdo em duas metades
    half_length = len(rucksack) // 2
    first_half = rucksack[:half_length]
    second_half = rucksack[half_length:]
    
    # encontra a intersecção entre as duas metades
    intersection = set(first_half) & set(second_half)
    
    # calcula a soma das prioridades dos elementos em comum
    rucksack_priority = sum([get_priority(char) for char in intersection])
    total_priority += rucksack_priority

print(total_priority)
