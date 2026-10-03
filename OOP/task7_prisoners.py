def prisoners_dilemma(prisoners, chair_start, treats):
    for i in range(treats+1):
        chair_start+=1
        if chair_start>prisoners:
            chair_start=1
    return chair_start

print(prisoners_dilemma(4,6,2))
