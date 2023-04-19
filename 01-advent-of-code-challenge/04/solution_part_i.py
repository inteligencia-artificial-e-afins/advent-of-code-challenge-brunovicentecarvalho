with open('sample.in', 'r') as file:
    section_pairs = [line.strip().split(',') for line in file.readlines()]

count = 0
for pair in section_pairs:
    a = set(range(int(pair[0].split('-')[0]), int(pair[0].split('-')[1])+1))
    b = set(range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1])+1))
    if a.issubset(b) or b.issubset(a):
        count += 1

print(count)
