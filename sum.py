scores = [10,20,30,40,50,70,30,20,10,50]
total = 0
count = {}

for score in scores:
    total = total + score
    if score in count: 
        count[score] = count[score] + 1
    else: 
        count[score] = 1    
print(total)
        
print("________________")
print(sum(scores))
print(count)
print("count of 50: " + str(count[50]))