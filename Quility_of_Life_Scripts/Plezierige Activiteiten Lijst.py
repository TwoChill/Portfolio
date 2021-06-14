from os import read
import MikeTools as mt

def readMe(MenuActions=False):
    if MenuActions is True:
        print(mt.bcolors.ENDC + """Op een schaal van """ + mt.bcolors.BOLD + """1""" + mt.bcolors.ENDC + """ tot """ + mt.bcolors.BOLD + """5""" + mt.bcolors.ENDC + """..
        
""" + mt.bcolors.BOLD + mt.bcolors.GREEN + """1""" + mt.bcolors.ENDC + """ = Helemaal niet             """ + mt.bcolors.BOLD + mt.bcolors.RED + """6""" + mt.bcolors.ENDC + """ = Laat huidige lijst zien
""" + mt.bcolors.BOLD + mt.bcolors.GREEN + """2""" + mt.bcolors.ENDC + """ = Een beetje                """ + mt.bcolors.BOLD + mt.bcolors.RED + """7""" + mt.bcolors.ENDC + """ = Sorteer en laat lijst zien
""" + mt.bcolors.BOLD + mt.bcolors.GREEN + """3""" + mt.bcolors.ENDC + """ = Nogal                     """ + mt.bcolors.BOLD + mt.bcolors.RED + """8""" + mt.bcolors.ENDC + """ = Sla huidige lijst op
""" + mt.bcolors.BOLD + mt.bcolors.GREEN + """4""" + mt.bcolors.ENDC + """ = Tamelijk                  """ + mt.bcolors.BOLD + mt.bcolors.RED + """9""" + mt.bcolors.ENDC + """ = Wis huidige lijst
""" + mt.bcolors.BOLD + mt.bcolors.GREEN + """5""" + mt.bcolors.ENDC + """ = Heel erg                  
                                                    """ + mt.bcolors.BOLD + mt.bcolors.RED + """ENTER""" + mt.bcolors.ENDC + """ = CONTINUE\n
        """)
    else:
        print(mt.bcolors.ENDC + """Op een schaal van """ + mt.bcolors.BOLD + """1""" + mt.bcolors.ENDC + """ tot """ + mt.bcolors.BOLD + """5""" + mt.bcolors.ENDC + """..
        
""" + mt.bcolors.BOLD + mt.bcolors.GREEN + """1""" + mt.bcolors.ENDC + """ = Helemaal niet
""" + mt.bcolors.BOLD + mt.bcolors.GREEN + """2""" + mt.bcolors.ENDC + """ = Een beetje
""" + mt.bcolors.BOLD + mt.bcolors.GREEN + """3""" + mt.bcolors.ENDC + """ = Nogal
""" + mt.bcolors.BOLD + mt.bcolors.GREEN + """4""" + mt.bcolors.ENDC + """ = Tamelijk
""" + mt.bcolors.BOLD + mt.bcolors.GREEN + """5""" + mt.bcolors.ENDC + """ = Heel erg\n
        """)

palDict = {}      

while True:
    
    mt.clear()
    bezigHeid = input(mt.bcolors.ENDC + "Wat is de bezigheid? :> ")
    mt.clear()
    
    while True:
        
        hoePlezierig = int()
        tijdValk = int()
        menuOptions = int()
        MenuActions = False

        
        readMe(MenuActions)

        try:
            tijdValk = int(input("Hoe vaak heb je de bezigheid: " + mt.bcolors.BOLD  + f"'{bezigHeid}'" + mt.bcolors.ENDC + " in de afgelopen " + mt.bcolors.BOLD + "30 dagen" + mt.bcolors.ENDC + " gendaan?\n" + mt.bcolors.BOLD + "\n(1/5) :> " + mt.bcolors.GREEN))
            if 1 < tijdValk > 5:
                raise ValueError
            
            mt.clear()
            readMe(MenuActions)
            
            hoePlezierig = int(input(mt.bcolors.ENDC + "Hoe plezierig vond je de bezigheid:" + mt.bcolors.BOLD  + f"'{bezigHeid}'" + mt.bcolors.ENDC + " in de afgelopen " + mt.bcolors.BOLD + "30 dagen" + mt.bcolors.ENDC + " gendaan?\n" + mt.bcolors.BOLD + "\n(1/5) :> " + mt.bcolors.GREEN))
            if 1 < hoePlezierig > 5:
                raise ValueError
            
            if type(palDict) == {}:
                MenuActions = False
            else:
                MenuActions = True
                
            if MenuActions == True:
                mt.clear()
                readMe(MenuActions)
                menuOptions = input(mt.bcolors.BOLD + mt.bcolors.RED + "(6/9) :> " + mt.bcolors.ENDC)

                break
            else:
                try:
                    palDict.update({bezigHeid:[tijdValk,hoePlezierig]})
                    mt.clear()
                    readMe(MenuActions)
                    input(mt.bcolors.BOLD + mt.bcolors.ORANGE + "Jouw invoering is opgenomen!" + mt.bcolors.RED + " (CONTINUE..)" +mt.bcolors.ORANGE +" :> " + mt.bcolors.ENDC)
                except:
                    mt.clear()
                    readMe(MenuActions)
                    input(mt.bcolors.BOLD + mt.bcolors.ORANGE + "Jouw invoering is" +mt.bcolors.ENDC + mt.bcolors.BOLD + mt.bcolors.RED + " NIET" + mt.bcolors.BOLD + mt.bcolors.ORANGE + " opgenomen!" + mt.bcolors.RED + " (CONTINUE..)" + mt.bcolors.ORANGE + " :> " + mt.bcolors.ENDC)     
                break
            
        except ValueError:
            if tijdValk == 0 and MenuActions == True or hoePlezierig == 0 and MenuActions == True or menuOptions == 0:
                mt.clear()
                continue
    
            if tijdValk == 6 and MenuActions == True or hoePlezierig == 6 and MenuActions == True or menuOptions == 6:
                mt.clear()
                print(palDict)
                input("Continue..")
                mt.clear()
                continue

            elif tijdValk == 7 and MenuActions == True or hoePlezierig == 7 and MenuActions == True or menuOptions == 7:
                mt.clear()
                readMe(MenuActions)
                print("Deze functie moet nog gemaakt worden! To Be Continued!!")
                input("Continue..")
                mt.clear()

            elif tijdValk == 8 and MenuActions == True or hoePlezierig == 8 and MenuActions == True or menuOptions == 8:
                mt.clear()
                readMe(MenuActions)
                mt.create_file(palDict, "w+")
                mt.clear()
                continue
            
            elif tijdValk == 9 and MenuActions == True or hoePlezierig == 9 and MenuActions == True or menuOptions == 9:
                mt.clear()
                readMe(MenuActions)
                answer = input("\n\n:> ")

            mt.clear()
            readMe(MenuActions)
            input(mt.bcolors.BOLD + mt.bcolors.ORANGE + "\nThat's not the input we're looking for.." +mt.bcolors.RED + " :> " + mt.bcolors.ENDC)
            mt.clear()

    