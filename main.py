import time
import string
from itertools import permutations
import unidecode

def chiffrementCesar(message,dec):
    dec=dec%25
    caracteresNonTraite=[' ',"'",'!','.',',']
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


def dechiffrement_cesar(message,dec):
    caracteresNonTraite=[' ',"'",'!','.',',']
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
    """
    Chiffre une chaîne avec le chiffrement de Vigenère (alphabet A–Z, majuscules).

    Chaque lettre du message clair est décalée d'un nombre de positions donné par
    la lettre correspondante de la clé (répétée), avec A=0, B=1, …, Z=25.
    Le calcul se fait modulo 26.

    Args:
        mot (str): Message en clair à chiffrer. Doit contenir uniquement des
            lettres majuscules A–Z (pas d'accents, pas d'espaces).
        cle (str): Clé de chiffrement non vide, en lettres majuscules A–Z.

    Returns:
        str: Message chiffré en majuscules A–Z.

    Raises:
        ZeroDivisionError: Si `cle` est vide (len(cle) == 0).
        ValueError: (recommandé côté appelant) si `mot` ou `cle` contient des
            caractères hors A–Z. Cette implémentation ne le vérifie pas.

    Notes:
        - Le décalage d'une lettre `L` de la clé est `ord(L) - 65` (A->0, …, Z->25).
        - Les caractères non alphabétiques ne sont pas gérés ici : normalisez
          en amont (ex. `mot = re.sub('[^A-Z]', '', mot.upper())`).

    Examples:
        >>> chiffrement_vigenere("HELLOWORLD", "KEY")
        'RIJVSUYVJN'
        >>> chiffrement_vigenere("BONJOUR", "CLE")
        'DZRLZYT'
        >>> chiffrement_vigenere("VIGENERE", "CLE")
        'XTKGYITP'
    """
    if not cle:
        raise ValueError("La clé ne doit pas être vide.")

        # Normalisation : majuscules
    mot = mot.upper()
    cle = cle.upper()

    mot_code = ""
    # i récupère l'indice c le caractère du mot
    for i,c in enumerate(mot):
        # d va récupérer le caractère de la cle (mot de passe) et boucle
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

print (chiffrement_vigenere("SCIENCE","RABELAIS"))

def dechiffrement_vigenere(mot,cle):
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
            print(lignes.__sizeof__())
            print("Mot de passe KC \nLe mot à trouver c'était :"+dechif+"\nLe mot de passe utlisé était "+clef)
            print("\nen ",end-start, " secondes")


def chiffrement_substitution(texte, cle_substitution):
    texte_chiffre = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for caractere in texte:
        if caractere.upper() in alphabet:
            # Trouver l'indice de la lettre dans l'alphabet
            index = alphabet.index(caractere.upper())
            # Appliquer la substitution en fonction de la clé
            nouveau_caractere = cle_substitution[index]

            # Conserver la casse (majuscule ou minuscule)
            if caractere.islower():
                texte_chiffre += nouveau_caractere.lower()
            else:
                texte_chiffre += nouveau_caractere
        else:
            texte_chiffre += caractere  # Conserver la ponctuation et les espaces

    return texte_chiffre

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
    combinaisons =  permutations(L,5)
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



#print(dechiffrement_cesar(result,7))

#Cesar2=chiffrementCesar("C'est Mardi et tout le monde est heureux de faire du Python en bloc 3 !",2)
#print(Cesar2)
#print(cryp)
#for dec in range(1,26):
#    claire=dechiffrement(cryp,dec)
#    print(claire)
#chiff=chiffrement_vigenere("VENDREDI","B")
#print(chiff)
#dechiff=dechiffrement_vigenere(chiff,"B")
#print(dechiff)
#attaque_dict("SCNYILAECHF")
#attaque_dict("XLRYRPFP")
#attaque_brute("BJXXQKIS")
#print(Cesar2);

#print (dechiffrement_cesar("ivuqvby !", 7))
#print (dechiffrement_cesar("e'guv octfk gv vqwv ng oqpfg guv jgwtgwz fg hcktg fw ravjqp gp dnqe 5 !",2))



def normaliser_texte(texte):
    # Supprimer les accents et convertir en majuscules
    texte_normalise = unidecode.unidecode(texte).upper()
    return texte_normalise

texte = """
À m'asseoir sur un banc, cinq minutes, avec toi
Et regarder les gens, tant qu'y en a
Te parler du bon temps, qui est mort ou qui reviendra
En serrant dans ma main tes petits doigts
Pis donner à bouffer à des pigeons idiots
Leur filer des coups de pied pour de faux
Et entendre ton rire qui lézarde les murs
Qui sait surtout guérir mes blessures
Te raconter un peu comment j'étais, minot
Les bombecs fabuleux qu'on piquait chez l'marchand
Car-en-sac et Minto, caramels à un franc
Et les Mistral Gagnants
À remarcher sous la pluie, cinq minutes, avec toi
Et regarder la vie, tant qu'y en a
Te raconter la Terre en te bouffant des yeux
Te parler de ta mère, un petit peu
Et sauter dans les flaques pour la faire râler
Bousiller nos godasses et s'marrer
Et entendre ton rire comme on entend la mer
S'arrêter, repartir en arrière
Te raconter surtout les Carambars d'antan et les Coco Boers
Et les vrais Roudoudous qui nous coupaient les lèvres
Et nous niquaient les dents
Et les Mistral Gagnants
À m'asseoir sur un banc, cinq minutes, avec toi
Regarder le soleil qui s'en va
Te parler du bon temps, qui est mort et je m'en fous
Te dire que les méchants, c'est pas nous
Que si moi je suis barge, ce n'est que de tes yeux
Car ils ont l'avantage d'être deux
Et entendre ton rire s'envoler aussi haut
Que s'envolent les cris des oiseaux
Te raconter, enfin, qu'il faut aimer la vie
L'aimer même si le temps est assassin et emporte avec lui
Les rires des enfants
Et les Mistral Gagnants
Et les Mistral Gagnants"""
#cle_substitution = "ZXVQRWYTPNMKJBFGLHDOAISCUE"
#print(chiffrement_substitution(normaliser_texte(texte), cle_substitution))