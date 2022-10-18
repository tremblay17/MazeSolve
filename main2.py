#SOLVER MAIN
from time import sleep
import csv
import numpy as np
import pygame
import time
from ref2 import mover, nodePicker, Node

if __name__ == "__main__":
    solve = True
    start_t0 = time.time()
    #maze_file = "maze_(71x71)(1738)"
    maze_file = input("Enter file name without .csv: ")
    address = f"mazes/{maze_file}.csv"
    maze = np.genfromtxt(address, delimiter=',', dtype=int)

    rows = len(maze)
    columns = len(maze[0])
    endPoint = (rows - 1, columns - 1)
    start = (0, 0)
    start_node = Node(None, start)
    prev = []
    route = [start_node]

    if solve:

        red = (255, 0, 0)
        blue = (155, 255, 255)
        purple = (102, 51, 153)
        green = (0, 128, 0)
        white = (255, 255, 255)
        black = (0, 0, 0)
        background = (255, 255, 255)
        cursor = (211, 211, 211)
        height = 7
        width = 7
        pygame.init()
        screenSize = [rows*height, columns * width]
        screen = pygame.display.set_mode(screenSize)
        pygame.display.set_caption("Maze Solver A*")
        clock = pygame.time.Clock()
        colors = [black, white, purple, green, cursor, red]
        stop = False
        run = False
        finished = False
        finalPass = False

        while not stop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = True
                        start_t0 = time.time()
            screen.fill(background)
            for row in range(rows):
                for column in range(columns):
                    color = colors[maze[row,column]]
                    pygame.draw.rect(screen, color, [width * column, height * row, width, height])
            #clock.tick(1200)
            pygame.display.flip()
            if finalPass:
                stop = True
                run = False
            elif run:
                atNode = nodePicker(route)
                maze, route, prev, atNode = mover(maze, route, prev, atNode)

                if atNode.position == endPoint:
                    finalPass = True
                    while atNode.parent is not None:
                        x, y = atNode.position
                        maze[x, y] = 5
                        atNode = atNode.parent

                #sleep(0.001)
        print(f"{time.time() - start_t0:.4f} s")
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.KEYDOWN:
                    finished = True
        pygame.quit()

    with open(f"mazes/{maze_file}_solved", "w", newline="") as c:
        writer = csv.writer(c)
        writer.writerows(maze)

    exit(0)