import pprint, random
# def class Maze

class Maze():

# def attributes
    def __init__(self, name):
        self.name = name
        # start position in the maze
        self.pos_x = 4
        self.pos_y = 4
        maze[self.pos_x][self.pos_y] = "P"

    def move(self, maze):
        #End postion in the maze
        if maze[self.pos_x][self.pos_y] == maze[0][0]:
            print('You Won!')
        else:
            while maze[self.pos_x][self.pos_y] != maze[0][0]:
                pprint.pprint(maze)
                dir = input("What direction do you want to go?")
                #up
                if dir == "up":
                    #remove player old position in the maze
                    maze[self.pos_x][self.pos_y] = ' '
                    # Check if empty
                    if maze[self.pos_x - 1][self.pos_y] == "x":
                        print('not possible')
                    else:
                    # change pos_x
                        self.pos_x = self.pos_x - 1
                        maze[self.pos_x][self.pos_y] = 'P'
                        pprint.pprint(maze)
                        return self.move(maze)

                #down
                elif dir == "down":
                    maze[self.pos_x][self.pos_y] = ' '
                    if maze[self.pos_x + 1][self.pos_y] == "x":
                        print('not possible')
                    else:
                        self.pos_x = self.pos_x + 1
                        maze[self.pos_x][self.pos_y] = 'P'
                        pprint.pprint(maze)
                        return self.move(maze)
                #left
                elif dir == "left":
                    maze[self.pos_x][self.pos_y] = ' '
                    if maze[self.pos_x][self.pos_y-1] == "x":
                        print('not possible')
                    else:
                        self.pos_y = self.pos_y - 1
                        maze[self.pos_x][self.pos_y] = 'P'
                        pprint.pprint(maze)
                        return self.move(maze)
                #right
                elif dir == "right":
                    maze[self.pos_x][self.pos_y] = ' '
                    if maze[self.pos_x][self.pos_y + 1] == "x":
                        print('not possible')
                    else:
                        self.pos_y = self.pos_y + 1
                        maze[self.pos_x][self.pos_y] = 'P'
                        pprint.pprint(maze)
                        return self.move(maze)

# make maze for player
def maze_maker():
    matrix = [[random.randint(0,2) for col in range(5)] for row in range(5)]
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] % 2 == 0:
                matrix[row][col] = ' '
            else:
                matrix[row][col] = 'x'
    # end postion
    matrix[0][0] = " "
    # start position
    matrix[4][4] = " "
    return matrix


# position in the maze
maze = maze_maker()

# obejects
player = Maze("player")
player.move(maze)
