def bellmanford(graph, startknoten):
	distanz = {} #Initialisierung einer leeren Liste für die Distanzen
	vorgaenger = {} #Initialisierung einer leeren Liste für die Vorgänger
	
	for i in graph: #Schleife für jede Kante im Graphen
		distanz[i['start']] = float('inf') #Startknoten der Kante bekommt das Gewicht unendlich
		distanz[i['ziel']] = float('inf') #Endknoten der Kante bekommt das Gewicht unendlich
	distanz[startknoten] = 0 #Distanz des Startknotens wird auf 0 gesetzt
	
	for i in range(len(graph)-1): #Schleife, die für jede Kante, bis auf eine, ausgeführt wird
		for j in range(len(graph)): #Schleife, die jede Kanten im Graphen ausführtt wird
			start = graph[j]["start"]    #Für eine bessere Übersicht wird 
			ziel = graph[j]["ziel"]      #start, ziel und gewicht in einzelnen
			gewicht = graph[j]["gewicht"]#Variablen gespeichert

			if distanz[start] != float('inf') and distanz[start] + gewicht < distanz[ziel]: #Wenn neue Abkürzung gefunden wurde
				distanz[ziel] = distanz[start] + gewicht #Distanzupdate für den Zielknoten
				vorgaenger[ziel] = start #Vorgänger vom Zielknoten wird der Startknoten
				
	for j in range(len(graph)):
		start = graph[j]["start"]    #Für eine bessere Übersicht wird 
		ziel = graph[j]["ziel"]      #start, ziel und gewicht in einzelnen
		gewicht = graph[j]["gewicht"]#Variablen gespeichert

		if distanz[start] != float('inf') and distanz[start] + gewicht < distanz[ziel]: #Wenn neue Abkürzung gefunden wurde
			return -1, -1, -1 #Fehlerrückgabe, da ein negativer Kreis identifiziert wurde
		else:
			return startknoten, distanz, vorgaenger #Sonst werden die Ergebnisse zurückgegeben

def ausgabe(start, ende, distanz, vorgaenger): #Funktion zum ausgeben der Werte, die die dijkstra-Funktion liefert
    if distanz is -1 or vorgaenger is -1: #Kein Weg wurde gefunden oder es wurde ein negativer Kreis gefunden
        print("Von "+start+" nach "+ende+" wurde kein Weg gefunden!")
    else: #Sonst soll der Weg ausgegeben werden
        print("Der kürzeste Weg von "+start+" nach "+ende+" lautet:")
        vorvorgaenger = [vorgaenger[ende]] #Neue Liste wird erstellt und der Vorgänger vom Endknoten wrd hinzugefügt
        while True:
            if vorvorgaenger[-1] is start: #Wenn der Startknoten erreicht wurde, soll die Schleife verlassen werden
                break
            vorvorgaenger.append(vorgaenger[vorvorgaenger[-1]]) #Der Vorgänger vom Vorgänger wird hinzugefügt
        vorvorgaenger.reverse() #Die Liste wird gedreht, da die Ausgabe mit dem Startknoten anfangen soll
        for knoten in vorvorgaenger: #Jeder knoten wird aufgerufen
            print(knoten+" ->", end=" ") #Und Ausgegeben
        print(ende)
        print("Distanzen: "+str(distanz)) #Ausgabe der Distanzen


G = [{"start": 'A', "ziel": 'B', "gewicht": 12},
     {"start": 'A', "ziel": 'E', "gewicht": 18},
     {"start": 'A', "ziel": 'D', "gewicht": -23},
     {"start": 'B', "ziel": 'E', "gewicht": -7},
     {"start": 'D', "ziel": 'E', "gewicht": 36},
     {"start": 'E', "ziel": 'F', "gewicht": 16}]

startknoten = 'A'
endknoten = 'F'

startknoten, distanz, vorgaenger = bellmanford(G, startknoten)
ausgabe(startknoten, endknoten, distanz, vorgaenger)
