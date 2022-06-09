"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 12        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create score board
        self.score = 0
        self.score_board = GLabel(f'Scores: {self.score}', x=0, y=window_height)
        self.score_board.font = '-30'
        self.window.add(self.score_board)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height - paddle_offset - self.paddle.height)

        # Center a filled ball in the graphical window
        self.ball_r = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.initial_y = INITIAL_Y_SPEED
        # Initialize our mouse listeners
        self.switch = False
        onmouseclicked(self.ball_move)

        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        onmousemoved(self.move_paddle)
        # Draw bricks
        self.brick_r = brick_rows
        self.brick_c = brick_cols
        self.brick_o = brick_offset
        self.brick_w = brick_width
        self.brick_s = brick_spacing
        self.brick_h = brick_height
        position_y = brick_offset
        # ct: number of rows
        ct = 0
        color = 'red'
        for j in range(brick_rows):
            position_x = 0
            for i in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color
                self.brick.color = color
                self.window.add(self.brick, x=position_x, y=position_y)
                position_x += brick_width + brick_spacing
            position_y += brick_height + brick_spacing
            ct += 1
            if ct % 10 == 0 or ct % 10 == 1:
                color = 'red'
            elif ct % 10 == 2 or ct % 10 == 3:
                color = 'orange'
            elif ct % 10 == 4 or ct % 10 == 5:
                color = 'yellow'
            elif ct % 10 == 6 or ct % 10 == 7:
                color = 'green'
            elif ct % 10 == 8 or ct % 10 == 9:
                color = 'blue'

    @property
    def dx(self):
        return self.__dx

    @dx.setter
    def dx(self, new_velocity):
        self.__dx = new_velocity
        # return self.__dx

    @property
    def dy(self):
        return self.__dy

    @dy.setter
    def dy(self, new_velocity):
        self.__dy = new_velocity
        # return self.__dy

    def ball_move(self, mouse):
        self.switch = True
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            self.switch = False
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def move_paddle(self, mouse):
        self.window.remove(self.paddle)
        self.paddle = GRect(self.paddle_width, self.paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.y = self.window.height - self.paddle_offset - self.paddle.height
        if self.paddle.width/2 <= mouse.x <= self.window.width - self.paddle.width/2:
            self.paddle.x = mouse.x - self.paddle.width / 2
        elif mouse.x > self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = 0
        self.window.add(self.paddle)
