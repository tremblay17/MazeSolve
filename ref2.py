import numpy as np

w = 1.0
class Node:
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        self.f=0
        self.fp=0
        self.g=0
        self.h=0

def findCost(nodePos, endPoint): #h
    x, y = nodePos
    xEnd, yEnd = endPoint
    cost = ((xEnd - x) ** 2 + (yEnd - y) ** 2)
    return cost
def findCost2(currNode): #g
    cost2 = currNode.g +1
    return cost2
def findCost34(currNode): #f
    cost3 = currNode.g + currNode.h
    cost4 = currNode.g + w*currNode.h
    return cost3, cost4


def in_bounds(nodePos, maze_dimension):
    (maxX, maxY) = maze_dimension
    (x, y) = nodePos
    x_in = (x <= maxX) & (x >= 0)
    y_in = (y <= maxY) & (y >= 0)
    return bool(x_in * y_in)


def remove_route(node, route):
    nodePos = node.position
    new_route = []
    for cell in route:
        if cell.position != nodePos:
            new_route.append(cell)
    return new_route


def pickNextRoute(atNode, maze, prev):
    movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    x0, y0 = atNode.position
    maze_dimension = (len(maze) - 1, len(maze[0]) - 1)

    nextRoute = []
    for movement in movements:
        x, y = (movement[0], movement[1])
        nextPos = (x0 + x, y0 + y)
        okay = in_bounds(nextPos, maze_dimension)
        if okay:
            try1 = maze[nextPos[0], nextPos[1]] != 0
            try2 = nextPos not in [item.position for item in prev]
            if bool(try1 * try2):
                cost = findCost(nextPos, maze_dimension)
                cost2 = findCost2(atNode)
                cost3 = cost + cost2
                cost4 = cost + w*cost2
                new_node = Node(atNode, nextPos)
                new_node.fp = cost4
                new_node.f = cost3
                new_node.g = cost2
                new_node.h = cost
                nextRoute.append(new_node)
    return nextRoute


def nodePicker(nodes):
    if len(nodes) == 1:
        atNode = nodes[0]
        return atNode
    atNode = Node(None, (0, 0))
    for node in nodes:
        if node.fp < atNode.fp:
            atNode = node
    return atNode


def mover(maze, route, prev, atNode):
    prev.append(atNode)
    route = remove_route(atNode, route)
    nextRoute = pickNextRoute(atNode, maze, prev)
    for each in nextRoute:
        route.append(each)
    atNode = nodePicker(nextRoute)
    x, y = atNode.position
    maze[x, y] = 4
    return maze, route, prev, atNode