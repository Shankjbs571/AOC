with open('day4.txt', 'r') as f:
    lines = [row.split(":")[1].strip() for row in f.read().split('\n')]
# print("lines: ",lines)

total_points = 0
for card in lines:
    count=0
    points=0
    winCards_and_myCards = card.split("|")
    
    winCards=winCards_and_myCards[0].strip().split(" ")
    myCards=winCards_and_myCards[1].strip().split(" ")
    
    
    for card_no in winCards:
        if card_no!='':
            if card_no in myCards:
                # print(card_no)
                count+=1
    
        
    if count>0:
        points=2**(count-1)
    # print("points",points)
    total_points+=points
    

print("total points are =",total_points)
