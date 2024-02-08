import random
import time

# declare variables #
thanks = "Thank you!"
fine = "Ok, fine..."
haveFL = False
IQ = 75

# start asking #

# we have a button that either lets me buy it or doesn't, and you can click yes or no #

yesNo = input('Are you going to let me buy FL Studio? (y/n) ')

if yesNo == 'y':
    print(thanks)
    haveFL = True
elif yesNo == 'n':
    print(fine)
    haveFL = False

if haveFL == True:
    print('Im going to not play Minecraft today, instead I will make music')
    print('IQ + 50')
    IQ = IQ + 50
elif haveFL == False:
    print('Im going to rot my brain away playing video games')
    print('IQ - 50')
    IQ = IQ - 50

print('Your IQ is: ' + str(IQ))
cont = input('Continue? (y/n) ')

if cont == 'y':
    pass
else:
    exit()

if (haveFL == True) and (IQ == 125):
    print('You win and you are smart!')
if(haveFL == False) and (IQ == 25):
    print('You lose and you are not smart')
    time.sleep(3)
    exit()
