def bellmandord(graph, startknoten):

    for Knoten v in graph:
        distanz[v] = unendlich;
        vorgaenger[v] = undefiniert;

    distanz[startknoten] = 0;

    for Knoten n - 1:
        for benachbarte Knoten u, v in Kanten:
            if (distanz[u] + gewicht[u, v]) < distanz[v]:
                distanz[v] = distanz[u] + gewicht [u, v]
                vorgaenger[v] = u

    for Knoten u, v in Kanten:
        if (distanz[u] + gewicht[u, v]) < distanz[v]:
            STOPP: "Negativen Zyklus gefunden!"

return distanz, vorgaenger
