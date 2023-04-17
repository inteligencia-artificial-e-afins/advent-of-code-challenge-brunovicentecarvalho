with open("sample.in", "r") as f:
    strategy = [line.strip().split() for line in f.readlines()]

score = 0
for round_num in range(len(strategy)):
    opp_play = strategy[round_num][0]
    your_play = strategy[round_num][1]
    if your_play == 'Y':
        score += 2
    elif your_play == 'X':
        score += 1 
    else:
        score += 3       
    if opp_play == "A":
        if your_play == "X":
            score += 3
        elif your_play == "Y":
            score += 6
        else:
            score += 0
    elif opp_play == "B":
        if your_play == "Y":
            score += 3
        elif your_play == "Z":
            score += 6
        else:
            score += 0
    elif opp_play == "C":
        if your_play == "Z":
            score += 3
        elif your_play == "X":
            score += 6
        else:
            score += 0
        
                

print(score)

