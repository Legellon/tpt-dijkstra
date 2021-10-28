import xml.etree.ElementTree as ET
from read import readFromXML_toDict
from dijkstra import dijkstra_search
import os

location_root = ET.parse('09.02.2021/graph_1.xml')
recievedXMLMap = location_root.getroot()

xml_dict = readFromXML_toDict(recievedXMLMap)

turns = [[9, 5], [5, 13], [2, 16], [6, 11], [10, 15],
         [12, 7], [7, 15], [13, 5], [14, 9], [15, 10]]

for turn in range(len(turns)):
    START_POINT = turns[turn][0]
    END_POINT = turns[turn][1]

    print("Turn:", turn + 1)
    print("From " + str(START_POINT) + " to " + str(END_POINT))

    shortest_way = dijkstra_search(xml_dict, START_POINT, END_POINT, 0)
    shortest_weight = dijkstra_search(xml_dict, START_POINT, END_POINT, 1)

    print("Shortest way:", shortest_way[0])
    print("Shortest path:", shortest_weight[0])
    print("Shortest time of path:", shortest_weight[1][END_POINT-1])
