from tkinter import *
import math
import random
import os

top = Tk()

f_menu = Frame(top)
f_menu.pack(side = LEFT)

L1= Label(f_menu, text="Points:")
L1.pack()
E1= Entry(f_menu, bd = 5)
E1.insert(0,"10")
E1.pack()

L2= Label(f_menu, text="routes:")
L2.pack()
E2= Entry(f_menu, bd = 5)
E2.insert(0,"100")
E2.pack()

L3= Label(f_menu, text="Vmin:")
L3.pack()
E3= Entry(f_menu, bd = 5)
E3.insert(0,"5")
E3.pack()

L4= Label(f_menu, text="Vmax:")
L4.pack()
E4= Entry(f_menu, bd = 5)
E4.insert(0,"120")
E4.pack()

L5= Label(f_menu, text="Ymin:")
L5.pack()
E5= Entry(f_menu, bd = 5)
E5.insert(0,"0")
E5.pack()

L6= Label(f_menu, text="Ymax:")
L6.pack()
E6= Entry(f_menu, bd = 5)
E6.insert(0,"600")
E6.pack()

L7= Label(f_menu, text="Xmin:")
L7.pack()
E7= Entry(f_menu, bd = 5)
E7.insert(0,"0")
E7.pack()

L8= Label(f_menu, text="Xmax:")
L8.pack()
E8= Entry(f_menu, bd = 5)
E8.insert(0,"400")
E8.pack()

def delMap():
    x=0 

def drawMap():
    W = float(E6.get()) - float(E5.get())
    H = float(E8.get()) - float(E7.get())

    offset = 40
    canvas = Canvas(top, width=int(W + offset), height=int(H + offset))

    n_points = int(E1.get()) if int(E1.get()) > 2 else 3
    n_routes = int(E2.get()) if int(E2.get()) > n_points else n_points

    if n_routes > n_points and n_routes > n_points * (n_points - 1):
        n_routes = n_points * (n_points - 1)

    global points
    points = []

    while len(points) < n_points:
        X = int(random.randrange(float(E5.get()), float(E6.get())))
        Y = int(random.randrange(float(E7.get()), float(E8.get())))

        r = 7

        if X - (r * 2) <= 1:
            X += r
        elif X + (r * 2) >= W - 1:
            X -= r

        if Y - (r * 2) <= 1:
            Y += r
        elif Y + (r * 2) >= H - 1:
            Y -= r

        new_point = {'X': X, 'Y': Y}
        points.append(new_point)
  
        canvas.create_oval(X - r, Y - r, X + r, Y + r, outline="gray", fill="black")

    global routes
    routes = []

    p_route_from_to = [None, None]
    min_value_usagepoints = 0
    used_points = [0] * n_points, [0] * n_points

    while len(routes) < n_routes:
        speed_newRoute = int(random.randrange(float(E3.get()), float(E4.get())))

        if used_points[0].count(min_value_usagepoints) < 1:
            min_value_usagepoints += 1
        
        from_point_index = used_points[0].index(min_value_usagepoints)
        p_route_from_to[0] = points[from_point_index]
        used_points[0][from_point_index] += 1

        if used_points[1].count(0) > 1:
            to_point_index = used_points[1].index(0)
        else:
            to_point_index = random.randrange(len(points))
            while used_points[1][to_point_index] >= n_points - 1:
                to_point_index = random.randrange(len(points))

        p_route_from_to[1] = points[to_point_index]

        if len(routes) > 0:
            is_used_route = lambda a,b: [[a, b] in route['way'] for route in routes].count(True) > 0

            while p_route_from_to[1] == p_route_from_to[0] or is_used_route(p_route_from_to[0], p_route_from_to[1]):
                to_point_index = (to_point_index + 1) % len(points)
                p_route_from_to[1] = points[to_point_index]
        used_points[1][to_point_index] += 1

        new_route = {'way': [p_route_from_to[0], p_route_from_to[1]], 'speed': speed_newRoute}

        routes.append(new_route)
        
        canvas.create_line(new_route['way'][0]['X'], new_route['way'][0]['Y'], new_route['way'][1]['X'], new_route['way'][1]['Y'], arrow=LAST)

    print(len(points))
    print(len(routes))
    print(routes)
    print(used_points)

    canvas.pack(side = RIGHT)

def saveMap():
    FILE_DIR = os.getcwd()
    FILENAME = "new_graph.xml"

    #with open(FILENAME, "w", encoding="utf-8") as file:
     #   file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<map>\n<points>\n")
      #  for point_id in range(points):
       #     file.write("<point id=\""+str(point_id)+"\" x=\""+str(points[point_id]['X'])+"\" y=\""+str(points[point_id]['Y'])+"\"/>\n")
        #file.write("</points>\n<routes>\n")
        #for route in routes:
         #   file.write("<route from=\""+route[]"\"")

B1=Button(f_menu, text = "Map Generation", command = drawMap)
B1.pack()

B2=Button(f_menu, text = "Save map", command = saveMap)
B2.pack()

B3=Button(f_menu, text = "Delete map", command = delMap)
B3.pack()

top.mainloop()