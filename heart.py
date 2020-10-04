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
