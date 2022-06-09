"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    # ct: total died times
    ct = 0
    # num_brick: number of breaks in the window
    num_brick = graphics.brick_r * graphics.brick_c
    # Add the animation loop here!

    while True:
        if ct < NUM_LIVES:
            pause(FRAME_RATE)
            graphics.ball.move(graphics.dx, graphics.dy)
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                graphics.dx = -graphics.dx
            if graphics.ball.y <= 0:
                graphics.dy = -graphics.dy
            if graphics.ball.y + graphics.ball.height > graphics.window.height:
                graphics.dx = 0
                graphics.dy = 0
                graphics.ball.x = (graphics.window.width-graphics.ball.width)/2
                graphics.ball.y = (graphics.window.height-graphics.ball.height)/2
                ct += 1
            for i in range(2):
                for j in range(2):
                    x = graphics.window.get_object_at(graphics.ball.x + i*2*graphics.ball_r, graphics.ball.y
                                                      + j*2*graphics.ball_r)
                    if x is not None:
                        if x is graphics.paddle:
                            graphics.dy = -graphics.initial_y
                        elif x is graphics.score_board:
                            graphics.dx = graphics.dx
                            graphics.dy = graphics.dy
                        else:
                            graphics.dy = -graphics.dy
                            graphics.window.remove(x)
                            num_brick -= 1
                            graphics.score += 1
                            graphics.score_board.text = 'Score: ' + str(graphics.score)
                            if num_brick == 0:
                                break
        else:
            graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
            graphics.ball.y = (graphics.window.height - graphics.ball.height) / 2
            break


if __name__ == '__main__':
    main()
