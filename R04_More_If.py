print("hur mycket är klockan")

answer = input()

nummer = int(answer) ##gör om svarert till ett tal

if(nummer >19):
    print("det är kväll")
elif(nummer > 12):
    print("det är eftermiddag")
elif(nummer < 8): #ELIF betyder else if
    print("det är morgon")
else: #om inget av det tidigare stämmer
    print("det är förmiddag")