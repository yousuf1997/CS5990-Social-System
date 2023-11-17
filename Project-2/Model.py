def getTheSumOfAllWeightsOfTheVertex(vertex, allVertex, computedShortestDistance):
    sum = 0
    for v in allVertex:
        if v != vertex:
            shortestDistance = 0
            try:
                shortestDistance = computedShortestDistance[(vertex, v)]
            except:
                try:
                    shortestDistance = computedShortestDistance[(v, vertex)]
                except:
                    shortestDistance = 0
            sum = sum + shortestDistance
    return sum