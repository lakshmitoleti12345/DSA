#3700 -input
# dividing the 3700 with 1000
#3700//1000=3
#3700%1000-remainder=700
#700//500=1
#700%500-remainder=200
def change(ammount):
    thousands=ammount//1000
    remaining_change=ammount%1000
    fivehundreds=remaining_change//500
    finalchange=remaining_change%500
    print("thousands=",thousands,"five hundreds=",fivehundreds,"final change=",finalchange) 
change(3700)

