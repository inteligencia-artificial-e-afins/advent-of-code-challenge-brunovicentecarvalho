with open('sample.in', 'r') as f:
    pairs = [line.strip().split(',') for line in f.readlines()]

overlap_count = 0

for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        a, b = pairs[i], pairs[j]
        for section_a in a:
            start_a, end_a = map(int, section_a.split('-'))
            for section_b in b:
                start_b, end_b = map(int, section_b.split('-'))
                if start_a <= end_b and start_b <= end_a:
                    overlap_count += 1
                    break
            else:
                continue
            break

print(overlap_count)






