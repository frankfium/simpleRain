#Copyright (c) <2020>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "simpleRain"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from graphics import *
import random as r
def main():
    WIDTH = 800
    HEIGHT = 800
    r.seed()

    win = GraphWin("Random Squares", WIDTH, HEIGHT, autoflush=False)

    rects = []
    colorList = [
    color_rgb(255, 170, 204),
    color_rgb(255, 187, 204),
    color_rgb(255, 204, 204),
    color_rgb(255, 221, 204),
    color_rgb(255, 238, 204)
    ]
    win.setBackground(color_rgb(72,61,139))

    for _ in range(3000):
        for rect in list(rects):  # iterate over a shallow copy
            rect.move(0, r.randint(10, 100))

            if rect.getP1().getY() > HEIGHT:
                rect.undraw()
                rects.remove(rect)

        x1 = r.randint(0, WIDTH - 5)
        y1 = r.randint(0, 10)

        rect = Rectangle(Point(x1, y1), Point(x1 + 5, y1 + 20))
        rect.setFill(r.choice(colorList))
        rect.draw(win)

        update(50)

        rects.append(rect)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
