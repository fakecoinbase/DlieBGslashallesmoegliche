import heapq

def dijkstra(graph, start, ende):
    Q = [(0, start)] #Initialisierung von Q mit zuweisung von dem Startknoten start und dem Gewicht 0
    besucht = [] #Initialisierung der besuchten Knoten ohne Zuweisung, da noch kein Knoten besucht wurde
    vorgaenger = {} #Initialisierung der Vorgänger ohne Zuweisung, da die Vorgänger noch ermittelt werden müssen

    while Q: #Schleife die solange läuft, bis Q leer ist
        (distanz, u) = heapq.heappop(Q) #Aus der Queue wird das Element mit dem kleinsten Gewicht/Distanz entommen
        if u in besucht: #Wenn u schon besucht wurde, soll direkt das nächste Element betrachtet werden
            continue
        besucht.append(u) #u wird als besucht gespeichert

        if u is ende: #Wenn der Endknoten erreicht ist, sollen die Ergebnisse zurückgegeben werden
            return start, ende, distanz, vorgaenger

        for v, c in graph[u]: #v sind alle Nachbarn von u
            if v in besucht: #Wenn der Nachbar schon besucht wurde, soll direkt der nächste Nachbar untersucht werden
                continue
            
            neueDistanz = c + distanz #Neue Distanz zum aktuellen Nachbarn wird berechnet
            heapq.heappush(Q, (neueDistanz, v)) #Wenn die neue Distanz kleiner ist als die alte, wird der Eintrag überschrieben
            vorgaenger[v] = u #Um später den Weg zu bestimmen, wird hier der schnellste Vorgänger zum Startknoten gespeichert

    return start, ende, -1, -1

def ausgabe(start, ende, distanz, vorgaenger): #Funktion zum ausgeben der Werte, die die dijkstra-Funktion liefert
    if distanz is -1 or vorgaenger is -1: #Kein Weg wurde gefunden
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
        print("Distanz: "+str(distanz)) #Ausgabe der Distanzen


G = {'A': [['B', 14], ['C', 18], ['D', 7]],
     'B': [['A', 14], ['C', 2], ['F', 46]],
     'C': [['A', 18], ['B', 2], ['E', 25]],
     'D': [['A', 7], ['E', 42]],
     'E': [['D', 42], ['F', 16]],
     'F': [['B', 46], ['E', 16]]}
    
start, ende, distanz, vorgaenger= dijkstra(G, "A", "F")
ausgabe(start, ende, distanz, vorgaenger)