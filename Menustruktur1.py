#Dette er et program til bygge videre på, hvis man skal bruge en menu i sit Pythonprogram
def prmenu():
    print("1) menu 1")
    print("2) menu 2")
    print("3) menu 3")
    print("4) stop program")

prmenu()
Menunr=int(input("Vælg menu nr."))
wh=1

while wh==1:
    if Menunr == 1:
        # Her skal det kode sættes ind som skal udføre et eller andet
        #U=I*R
        I=float(input('Indtast strøm I'))
        R=float(input('Indtast modstand R'))
        print(U=I*R)

        print("du har valgt menu nr. 1")
        prmenu()
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 2:
         # Her skal det kode sættes ind som skal udføre et eller andet
         #I=U/R
        U=float(input('Indtast spænding U'))
        R=float(input('Indtast modstand R'))
        print('Udr_I=U/R')

        print("du har valgt menu nr. 2")
        prmenu()
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 3:
        # Her skal det kode sættes ind som skal udføre et eller andet
        #R=U/I
        U=float(input('Indtast strøm I'))
        I=float(input('Indtast modstand R'))
        print('Udr_R=U/I')

        print("du har valgt menu nr. 3")
        prmenu()
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 4:
        print("Nu stopper programmet!")
        wh=2

