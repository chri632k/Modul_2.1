#Fiber power budget
import math

def MM_850(x):
    sum=x*2.5
    return sum

def MM_1300(x):
    sum=x*0.6
    return sum

def SM_1310(x):
    sum=x*0.35
    return sum
    
def SM_1550(x):
    sum=x*0.20
    return sum

loop = 1
while loop==1:
    total=0
    
    kon=int(input('Indtast antal konnekteringer'))
    kon_db=kon*0.5
    
    fus=int(input('Indtast antal fusionsspidsninger'))
    fus_db=fus*0.1
    
    rep=int(input('Indtast antal kommende reparationer'))
        
    sikkmarkin=3
        
    x=float(input("Indtast antal km"))
    
    z=(math.ceil(x/10)*0.5)
    
    
    daempmm850=MM_850(x)
    daempmm1300=MM_1300(x)
    daempsm1310=SM_1310(x)
    daempsm1550=SM_1550(x)
    
    totalmm850=total+kon_db+fus_db+z+sikkmarkin+daempmm850
    totalmm1300=total+kon_db+fus_db+z+sikkmarkin+daempmm1300
    totalsm1310=total+kon_db+fus_db+z+sikkmarkin+daempsm1310
    totalsm1550=total+kon_db+fus_db+z+sikkmarkin+daempsm1550
    
  
    
    
    if x>2:
        print('Fiberstraekningen er for lang til Multi Mode')
        print('Daemp ved SM 1310', totalsm1310, 'dB')
        print('Daemp ved SM 1550', totalsm1550, 'dB')
        
        
    else:
        print('Daemp ved MM 850', totalmm850, 'dB')
        print('Daemp ved MM 1300', totalmm1300, 'dB')
        print('Daemp ved SM 1310', totalsm1310, 'dB')
        print('Daemp ved SM 1550', totalsm1550, 'dB')
    
    
    loop=int(input('Vil du fortsaette (1) eller stoppe (0)?'))
    if loop==0:
        exit