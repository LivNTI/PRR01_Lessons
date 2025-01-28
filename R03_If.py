print("hur mycket är klockan")

answer = input()

nummer = int(answer) ##gör om svarert till ett tal

if(nummer > 12):
    print("det är eftermiddag")
else: ##om nummret inte är över 12
    print("det är förmiddag")