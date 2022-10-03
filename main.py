import time
import string
from itertools import permutations

def chiffrement(message,dec):
    caracteresNonTraite=[' ',"'",'!','.']
    message=message.lower()
    resultat=""
    for c in message:
        if c not in caracteresNonTraite:
            x=ord(c)+dec
            if x>ord('z'):
                x=x-26
        else:
            x=ord(c)
        resultat=resultat+chr(x)
    return resultat

def dechiffrement(message,dec):
    caracteresNonTraite=[' ',"'",'!','.']
    message=message.lower()
    retour=""
    for c in message:
        if c not in caracteresNonTraite:
            x=ord(c)-dec
            if x<ord('a'):
                x=x+26
        else:
            x=ord(c)
        retour=retour+chr(x)
    return retour

def chiffrement_vigenere(mot,cle):
    mot_code = ""
    # i récupère l'indice c le caractère du mot
    for i,c in enumerate(mot):
        # d va récupérer le caractère de la cle et boucler
        d = cle[i % len(cle)]
        # On ramène la lettre A à l'indice 0 (ord('A')=65)
        # d va être le décalage
        d = ord(d) - 65
        # On ramène aussi le caractère c sur le même principe
        c = ord(c) - 65
        # On va calculer le nouveau caractère pour chiffrer
        # en applicant le décalage c+d et on oublie pas d'ajouter 65
        # %26 permet de boucler quand on arrive après Z
        nouveauCaractere = chr((c+d)%26+65)
        mot_code += nouveauCaractere
    return mot_code

def dechiffrement_vigenere(mot,cle ):
    mot_code = ""
    for i,c in enumerate(mot):
        d = cle[ i % len(cle)]
        d = ord(d) - 65
        mot_code += chr((ord(c)-65-d)%26+65)
    return mot_code

def attaque_dict(mot):
    start = time.time()
    mot=mot.upper()
    with open('dic.txt', encoding ='utf-8', errors='ignore') as file:
        lignes = []
        for readline in file:
            lignes.append((readline.upper()))
    file.close()

    for clef in lignes:
        clef=clef.strip().upper()
        dechif=dechiffrement_vigenere(mot,clef)
        if dechif+"\n" in lignes:
            end = time.time()
            print("Mot de passe KC \nMot trouvé c'était :"+dechif+"\nLe mot de passe utlisé était "+clef)
            print("\nen ",end-start, " secondes")

def attaque_brute(mot):
    print("Début du déchiffrement brute pour le mot "+mot)
    print("Patience je bosse ",end='')
    comp=0
    with open('dic.txt', encoding ='utf-8', errors='ignore') as file:
        dic = []
        for readline in file:
            dic.append((readline.upper()))
    file.close()
    start = time.time()
    mot=mot.upper()
    L=list(string.ascii_uppercase)
    # combinaisons sur 4 lettres
    combinaisons =  permutations(L,4)
    lignes =[''.join(j) for j in combinaisons]
    for clef in lignes:
        comp+=1
        if comp>8000:
            print('.', end='')
            comp-=8000
        clef=clef.strip().upper()
        dechif=dechiffrement_vigenere(mot,clef)
        if dechif+"\n" in dic:
            end = time.time()
            print("Mot de passe KC \nMot trouvé c'était :"+dechif+"\nLe mot de passe utlisé était "+clef)
            print("\nen ",end-start, " secondes")
            return 1
    return 0

#cryp=chiffrement("C'est lundi et tout le monde est heureux de faire du python !",2)
#print(cryp)
#for dec in range(1,26):
#    claire=dechiffrement(cryp,dec)
#    print(claire)
chiff=chiffrement_vigenere("VENDREDI","GFKU")
print(chiff)
#dechiff=dechiffrement_vigenere(chiff,"BTS_SIO")
#print(dechiff)
#attaque_dict("SCNYILAECHF")
#attaque_dict("XLRYRPFP")
attaque_brute("BBJXXXJNC")
