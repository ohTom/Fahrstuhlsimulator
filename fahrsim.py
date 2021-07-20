import os
import time
from collections import deque
from random import randint

#Eigene files
import render

#Für das updaten des Terminals für die graphische Simulation.
os.system('cls')

#Ein Gebäude kann, nach Größe, mehrere Fahrstuhlsysteme beinhalten.
class Gebäude:
    def __init__(self, stockwerke, systeme) -> None:
        self.stockwerke = stockwerke
        self.systeme = systeme

#Ein System besteht aus mehreren Fahrstühlen und einem Treppenhaus.
class Fahrstuhlsysteme:
    def __init__(self,anz_stuehle,stockwerke) -> None:
        self.anz_stuehle = anz_stuehle
        self.stockwerke = stockwerke

class Fahrstuhl:
    def __init__(self, stockwerke, position, plaetze) -> None:
        self.plaetze = plaetze
        self.fahrgaeste = []
        self.position = position
        self.stockwerke = stockwerke
        self.zaehler = 0
        self.faehert = False
        self.wunsch = {}
    def hochfahren(self, stockwerke):
        self.faehert = True
        self.position += stockwerke
    def runterfahren(self, stockwerke):
        self.faehert = True
        self.position -= stockwerke
         
    def fahrgaeste_aufnehmen(self):
        for i in range (self.plaetze - len(self.fahrgaeste)):
            #self.warteschlange
            #self.fahrgaeste.append(warteschlangen[self.position].popleft)
            pass
        
    def fahrgaeste_absetzen(self):
        pass


class Fahrgast:
    def __init__(self, ziel) -> None:
        #self.name 
        self.ziel = ziel

#Gebäude/System
#Montage
stockwerke = 5
lift1 = Fahrstuhl(stockwerke,0,6)
warteschlangen = [deque() for i in range(stockwerke)]
zeitalt = time.time()
#print (zeitalt)

#Zum Testen erstmal hartkodiert. Später mit einem Zufallsgenerator:
zeitabstand = 1.0 


#Betrieb
zaehler = 0
im_betrieb = True
while (im_betrieb):
    zeitneu = time.time()
    if (zeitneu - zeitalt) > zeitabstand:
        #print (zeitneu)
        zuf_stockwerk = randint(0,lift1.stockwerke - 1)
        print ('Debug: stockwerk' + str(zuf_stockwerk))
        while True:
            zuf_ziel = randint(0,lift1.stockwerke - 1)
            print ('Debug: ziel' + str(zuf_ziel))
            if zuf_stockwerk != zuf_ziel:
                print ('Debug: (approved)' + str(zuf_ziel))
                break
        warteschlangen[zuf_stockwerk].append(Fahrgast(zuf_ziel))
        zaehler += 1
        zeitalt = zeitneu
        print('Debug:' + str(zaehler))
    #Stopper, damit die Testphase nicht zu lange dauert.
    if zaehler >10:
        im_betrieb = False
render.render()
print(len(warteschlangen[lift1.position]))
#for i in range(len(warteschlangen[lift1.position]))
#lift1.fahrgaeste_aufnehmen()

# for i in range(len(lift1.fahrgaeste)):
#     print (str(lift1.fahrgaeste[i].ziel))

#print (warteschlangen)
#lift1.fahrgaeste_aufnehmen()
#print(lift1.__dict__)


# Mögliche Features:
#   -Erstellen einer XML oder json Datei zum Loggen der durchgeführten Simulation.
#   -Das selbe mit einer SQL Datenbank
#   -zeitabstand für das erscheine der Fahrgäste abhängig von Tagszeit