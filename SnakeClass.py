class Snake:

    def __init__(self):
        self.speed = 15
        # defining snake default position
        self.position = [100, 50]
        # defining first 4 blocks of snake body
        self.body = [[100, 50],
                      [90, 50],
                      [80, 50],
                      [70, 50]]
        # setting default snake direction towards right
        self.direction = 'RIGHT'

