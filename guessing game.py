import random
num = random.randint(1,100)
print(num)
attempt = 5
while attempt>0:
    x = int(input("guess number"))
    if x ==num:
        print("congratulation")
    if x > num:
        print("to high") 
    if x < num:
        print("to low")  
         
        
    attempt -=1
else:
     print("game over")
     