def dijkstra(graph, startknoten):

    erstelle Knotensatz Q;

    for Knoten v in graph:
        distanz[v] = unendlich;
        vorgaenger[v] = undefiniert;
        fuege v in Q hinzu;

    distanz[startknoten] = 0;

    while Q:
        u = Knoten in Q mit minimaler distanz[u];
        entferne u aus Q;

        for Nachbarn v in u:
            neueDistanz = distanz[u] + laenge(u,v);

            if neueDistanz < distanz[v]:
                distanz[v] = neueDistanz;
                vorgaenger[v] = u;

return distanz, vorgaenger
