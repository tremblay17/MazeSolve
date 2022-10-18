import numpy as np


class Node:
    def __init__(self, parent, cost, position):
        self.parent = parent
        self.cost = cost
        self.position = position


def findCost(nodePos, endPoint):
    x, y = nodePos
    xEnd, yEnd = endPoint
    cost = np.sqrt((xEnd - x) ** 2 + (yEnd - y) ** 2)
    return cost


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
                new_node = Node(atNode, cost, nextPos)
                nextRoute.append(new_node)
    return nextRoute


def nodePicker(nodes):
    if len(nodes) == 1:
        atNode = nodes[0]
        return atNode
    atNode = Node(None, np.inf, (0, 0))
    for node in nodes:
        if node.cost < atNode.cost:
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
