"""
File: 
Name: Vanessa
-------------------------
Make the ball bouncing in the window when users click the mouse.
When the ball is out of the window, it will go back to the start place.
After the ball bounces three times, it will no longer bounce again.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
vy = GRAVITY
ct = 0
switch = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball)
    onmouseclicked(bounce)


def bounce(mouse):
    global ball, vy, switch, ct
    if not switch and ct != 3:
        # switch: the switch of the mouse
        switch = True
        # ct: bouncing times
        ct += 1
        while True:
            ball.move(VX, vy)
            if ball.y + SIZE >= window.height and vy > 0:
                vy = -REDUCE * vy
            pause(DELAY)
            vy += GRAVITY
            if ball.x >= window.width:
                window.remove(ball)
                switch = False
                break
        window.add(ball, x=START_X, y=START_Y)


if __name__ == "__main__":
    main()
