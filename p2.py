#A chocalate cost $1
# you have n rupees
#after eating , you get 1 wrapper
# you can exchnage 3 wrapers for 1 new chocalate
# how many chocalates can you eat in total

amount=5
chocalate=amount
wraper=amount
while wraper>=3:
    e=wraper//3
    chocalate+=e
    wraper=e+wraper%3
print(chocalate)