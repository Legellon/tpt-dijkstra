from math import inf as INF

def dijkstra_search(pointsWithRoutes, START_POINT, END_POINT, OPERATING_MODE):
    COUNT_OF_POINTS = len(pointsWithRoutes.keys())

    st_p = START_POINT - 1
    en_p = END_POINT

    if st_p < 1 and en_p - 1 >= COUNT_OF_POINTS:
        return 0

    used_point = [False] * COUNT_OF_POINTS
    previous_point = [None] * COUNT_OF_POINTS
    weights = [INF] * COUNT_OF_POINTS

    path_fromStart = []

    minimal_distance = 0
    OPERATING_MODE %= 2 # ==0 - shortest nearest / ==1 - shortest distance  

    weights[st_p] = minimal_distance

    while minimal_distance < INF:
        currentPoint = st_p
        used_point[currentPoint] = True
        
        for near_availablePoint in pointsWithRoutes[currentPoint + 1]['routes']:
            weight_availablePoint = near_availablePoint['weight']

            near_availablePoint = int(near_availablePoint['to']) - 1

            if OPERATING_MODE == 0:
                weight_availablePoint = 1
                
            if weights[currentPoint] + weight_availablePoint < weights[near_availablePoint]:
                weights[near_availablePoint] = weights[currentPoint] + weight_availablePoint
                previous_point[near_availablePoint] = currentPoint + 1
        
        minimal_distance = INF
        
        for currentPoint in range(COUNT_OF_POINTS):
            if not used_point[currentPoint] and weights[currentPoint] < minimal_distance:
                minimal_distance = weights[currentPoint]
                st_p = currentPoint

    while en_p is not None:
        path_fromStart.insert(0, en_p)
        en_p = previous_point[en_p - 1]
        
    if len(path_fromStart) == 1:
        path_fromStart = [START_POINT]

    result = [path_fromStart, weights]
    return result
