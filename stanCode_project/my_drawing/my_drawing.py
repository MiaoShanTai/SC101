"""
File: 
Name: Vanessa
----------------------
Create my drawing by GObject
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Moon(饅頭人)
    Always smile as happy as Moon!!!
    """
    window = GWindow(width=600, height=600, title='Moon')
    face = GOval(350, 350, x=125, y=50)
    window.add(face)
    eye1 = GLine(220, 170, 290, 170)
    window.add(eye1)
    eye2 =GLine(230, 130, 290, 170)
    window.add(eye2)
    eye3 = GLine(245, 200, 290, 170)
    window.add(eye3)
    eye4 = GLine(350, 160, 415, 145)
    window.add(eye4)
    eye5 = GLine(350, 160, 390, 110)
    window.add(eye5)
    eye6 = GLine(350, 160, 410, 185)
    window.add(eye6)
    nose = GArc(50, 80, 5, 190)
    window.add(nose, x=295, y=180)
    rouge = GOval(80, 80)
    rouge.filled = True
    rouge.fill_color = 'lightpink'
    rouge.color = 'lightpink'
    window.add(rouge, x=150, y=180)
    rouge1 = GOval(75, 75)
    rouge1.filled = True
    rouge1.fill_color = 'lightpink'
    rouge1.color = 'lightpink'
    window.add(rouge1, x=397, y=165)
    mouth = GArc(345, 185, 225, 125)
    window.add(mouth, x=150, y=160)
    arc1 = GArc(850, 1100, 18, 50)
    window.add(arc1, x=295, y=35)
    line1 = GLine(490, 110, 540, 75)
    window.add(line1)
    line2 = GLine(500, 140, 555, 110)
    window.add(line2)
    line3 = GLine(465, 85, 510, 40)
    window.add(line3)
    l_hand = GArc(80, 80, 100, 275)
    window.add(l_hand, x=170, y=460)
    l_arm1 = GLine(215, 375, 203, 460)
    window.add(l_arm1)
    l_arm2 = GLine(250, 488, 275, 430)
    window.add(l_arm2)
    l_body = GLine(235, 530, 233, 560)
    window.add(l_body)
    r_body = GLine(405, 405, 425, 540)
    window.add(r_body)
    r_hand = GArc(80, 80, 260, 165)
    window.add(r_hand, x=400, y=430)
    r_arm = GLine(415, 360, 433, 437)
    window.add(r_arm)


if __name__ == '__main__':
    main()
