import math

def readFromXML_toDict(XMLMap):
    pointsWithRoutes = {}
    
    for point in XMLMap[0]:
        try:
            prop = {'x': float(point.attrib['x']), 'y': float(point.attrib['y'])}

            pointsWithRoutes.update({int(point.attrib['id']): {'prop': prop, 'routes': []} })
        except:
            continue
        
    for route in XMLMap[1]:
        try:
            point_from = int(route.attrib['from'])
            point_to = int(route.attrib['to'])
            
            route_distance = math.sqrt(pow(pointsWithRoutes[point_from]['prop']['x'] - pointsWithRoutes[point_to]['prop']['x'], 2) + pow(pointsWithRoutes[point_from]['prop']['y'] - pointsWithRoutes[point_to]['prop']['y'], 2))
            route_vmax = float(route.attrib['vmax'])
            
            new_route = {'to': point_to, 'weight': route_distance / route_vmax}

            pointsWithRoutes[point_from]['routes'].append(new_route)
        except:
            continue

    return pointsWithRoutes
