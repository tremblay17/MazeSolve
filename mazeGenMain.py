from datetime import datetime

import pygame
import csv, time
import numpy as np
from time import sleep
from numpy.random import randint

pygame.init()
output = pygame.display.set_mode((440, 330))

pygame.display.set_caption('Maze Generator')


def in_bounds(position, maze_dimension):
    (maxX, maxY) = maze_dimension
    (x, y) = position

    inputX = (x <= maxX) & (x >= 0)
    inputY = (y <= maxY) & (y >= 0)
    return bool(inputX * inputY)


def movements(maze_dimension, prev):
    xpos, ypos = prev

    move = []
    move1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    move2 = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    moveCount = len(move1)

    for i in range(moveCount):
        moveX1, moveY1 = move1[i]
        moveX2, moveY2 = move2[i]

        if (in_bounds((xpos + moveX1, ypos + moveY1), maze_dimension)) and (
                in_bounds((xpos + moveX2, ypos + moveY2), maze_dimension)):
            move.append([(xpos + moveX1, ypos + moveY1), (xpos + moveX2, ypos + moveY2)])
    return move


def mover(maze, prev, history, back):
    (x, y) = prev
    maze[x, y] = 1
    maze_dimension = (len(maze), len(maze[0]))
    move = movements(maze_dimension, prev)
    moves = []

    for aMove in move:
        (x1, y1) = aMove[0]
        (x2, y2) = aMove[1]
        not_path = (maze[x1, y1] != 1) & (maze[x2, y2] != 1)
        not_start = (maze[x1, y1] != 2) & (maze[x2, y2] != 2)
        if bool(not_path * not_start):
            moves.append(aMove)
    if len(moves) == 0:
        prev = history[-2 - back]
        if prev == (0, 0):
            finished = True
            print("Finished maze generation. Press an arrow key to save the maze to CSV.")
            return maze, prev, back, finished
        back += 1
        finished = False
        # print("len(moves)==0")
        return maze, prev, back, finished
    else:
        back = 0
        # print("else1")
        if len(moves) == 1:
            # print("if1")
            prev = moves[0]
            (x1, y1) = prev[0]
            (x2, y2) = prev[1]
            maze[x1, y1] = 1
            maze[x2, y2] = 4
            prev = prev[1]
            finished = False
            return maze, prev, back, finished
        else:
            # print("else2")
            random = randint(0, len(moves))
            prev = moves[random]
            (x1, y1) = prev[0]
            (x2, y2) = prev[1]
            maze[x1, y1] = 1
            maze[x2, y2] = 4
            prev = prev[1]
            finished = False
            return maze, prev, back, finished


if __name__ == "__main__":
    num_mazes = 1
    start_t0 = time.time()

    purple = (102, 51, 153)
    green = (0, 128, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)
    background = (255, 255, 255)
    cursor = (102, 51, 153)

    blockHeight = 6
    blockWidth = blockHeight

    for iter_maze in range(num_mazes):
        start_t = time.time()
        rows = 99
        cols = 99
        maze = np.zeros((rows, cols))

        pygame.init()
        screenSize = [cols * blockHeight, rows * blockWidth]
        screen = pygame.display.set_mode(screenSize)
        pygame.display.set_caption("Maze Generator")
        finished = False
        run = False
        speed = pygame.time.Clock()
        colors = [black, white, purple, green, cursor]
        prev = (0, 0)
        history = [prev]
        back = 0

        maze[0, 0] = 2
        maze[-1, -1] = 3

        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    print("Exiting...")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = True
            screen.fill(background)
            for mazeRow in range(rows):
                for mazeColumn in range(cols):
                    color = colors[int(maze[mazeRow, mazeColumn])]
                    pygame.draw.rect(screen, color,
                                     [blockWidth * mazeColumn,
                                      blockHeight * mazeRow,
                                      blockWidth, blockHeight])
            speed.tick(120)
            pygame.display.flip()
            if run:
                maze, prev, back, finished = mover(maze, prev, history, back)
                if prev not in history:
                    history.append(prev)
                sleep(0.005)
        print(f"{time.time() - start_t:.3f} s")
        cont = True
        while cont:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cont = False
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                cont = False
                pygame.quit()
        timeInfo = datetime.now()
        #           replace below with desired file save location
        with open(f"E:\Automotive\Design\maze7/mazes/maze_({rows}x{cols})({timeInfo.hour}{timeInfo.minute}).csv", "w",
                  newline="") as c:
            writer = csv.writer(c)
            writer.writerows(maze)

    exit(0)