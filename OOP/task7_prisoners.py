def prisoners_dilemma(prisoners, treats, chair_start):
#    for i in range(treats-1):
#        chair_start+=1
#        if chair_start>prisoners:
#            chair_start=1
#    return chair_start
    i=treats%prisoners
    return chair_start+i-1


print(prisoners_dilemma(7,19,2))