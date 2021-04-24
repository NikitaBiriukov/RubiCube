from turtle import Turtle, Screen

class Cube3x3x3:

    def draw_cell(self, x1, y1, x2, y2, x3, y3, x4, y4, color_):
        self.t.penup()
        self.t.fillcolor(color_)
        self.t.begin_fill()
        self.t.goto(x1, y1)
        self.t.pendown()
        self.t.goto(x2, y2)
        self.t.goto(x3, y3)
        self.t.goto(x4, y4)
        self.t.goto(x1, y1)
        self.t.penup()
        self.t.end_fill()

    def draw_play_ground(self):
        self.t.clear()
        # Front side
        for i in range(0, 3):
            for j in range(0, 3):
                x0 = j * self.side - (3*self.side / 2)
                y0 = i * self.side - (3*self.side / 2)
                self.draw_cell(x0 + 1, y0 + 1, x0 + self.side - 1, y0 + 1, x0 + self.side - 1, y0 + self.side - 1, x0 + 1, y0 + self.side - 1, self.A[0][3*i + j])
        # Upper side
        cosA = 0.75 * 0.766 * self.side  # 0.866   0.5253
        sinA = 0.75 * 0.643 * self.side  # 0.5   0.851
        for i in range(3):
            for j in range(3):
                x0 = i * cosA + j * self.side - (3*self.side / 2)
                y0 = 3 * self.side + i * sinA - (3*self.side / 2)
                self.draw_cell(x0 + 1, y0 + 1, x0 + cosA + 1, y0 + sinA - 1, x0 + cosA + self.side - 1, y0 + sinA - 1, x0 + self.side - 1,  y0 + 1, self.A[2][3*i + j])
        # Right side
        for i in range(3):
            for j in range(3):
                x0 = 3 * self.side + j * cosA - (3*self.side / 2)
                y0 = i * self.side + j * sinA - (3*self.side / 2)
                self.draw_cell(x0 + 1, y0 + 1, x0 + 1, y0 + self.side - 1, x0 + cosA - 1, y0 + sinA + self.side - 2, x0 + cosA - 1, y0 + sinA + 1, self.A[1][3*i + j])

    def redraw_row(self, row):
        # Front side
        for j in range(0, 3):
            x0 = j * self.side - (3*self.side / 2)
            y0 = row * self.side - (3*self.side / 2)
            self.draw_cell(x0 + 1, y0 + 1, x0 + self.side - 1, y0 + 1, x0 + self.side - 1, y0 + self.side - 1, x0 + 1, y0 + self.side - 1, self.A[0][3*row + j])
        cosA = 0.75 * 0.766 * self.side  # 0.866   0.5253
        sinA = 0.75 * 0.643 * self.side  # 0.5   0.851
        # Right side
        for j in range(3):
            x0 = 3 * self.side + j * cosA - (3*self.side / 2)
            y0 = row * self.side + j * sinA - (3*self.side / 2)
            self.draw_cell(x0 + 1, y0 + 1, x0 + 1, y0 + self.side - 1, x0 + cosA - 1, y0 + sinA + self.side - 2, x0 + cosA - 1, y0 + sinA + 1, self.A[1][3*row + j])

    def redraw_column(self, column):
        # Front side
        for i in range(0, 3):
            x0 = column * self.side - (3*self.side / 2)
            y0 = i * self.side - (3*self.side / 2)       
            self.draw_cell(x0 + 1, y0 + 1, x0 + self.side - 1, y0 + 1, x0 + self.side - 1, y0 + self.side - 1, x0 + 1, y0 + self.side - 1, self.A[0][3*i + column])
        # Upper side
        cosA = 0.75 * 0.766 * self.side  # 0.866   0.5253
        sinA = 0.75 * 0.643 * self.side  # 0.5   0.851     
        for i in range(3):
            x0 = i * cosA + column * self.side - (3*self.side / 2)
            y0 = 3 * self.side + i * sinA - (3*self.side / 2)       
            self.draw_cell(x0 + 1, y0 + 1, x0 + cosA + 1, y0 + sinA - 1, x0 + cosA + self.side - 1, y0 + sinA - 1, x0 + self.side - 1,  y0 + 1, self.A[2][3*i + column])

    def oncontrolkeypress(self, screen_, event_handle_function, key):
        def eventfunction(event):
            event_handle_function()
        screen_.getcanvas().bind("<Control-KeyPress-%s>" % key, eventfunction)

    def onaltkeypress(self, screen_, event_handle_function, key):
        def eventfunction(event):
            event_handle_function()
        screen_.getcanvas().bind("<Alt-KeyPress-%s>" % key, eventfunction)

    def row_transform_matrix(self, row, sides, draw = False):
        temp = [0, 0, 0]
        for i in range(3):
            temp[i] = self.A[sides[0]][3*row + i]
        for k in range(3):
            for i in range(3):
                self.A[sides[k]][3*row + i] = self.A[sides[k + 1]][3*row + i]
        for i in range(3):
            self.A[sides[3]][3*row + i] = temp[i]
        if draw :
            self.redraw_row(row)

    def column_transform_matrix(self, column, sides, draw = False):
        temp = [0, 0, 0]
        for i in range(3):
            temp[i] = self.A[sides[0]][3*i + column]
        for k in range(3):
            for i in range(3):
                self.A[sides[k]][3*i + column] = self.A[sides[k + 1]][3*i + column]
        for i in range(3):
            self.A[sides[3]][3*i + column] = temp[i]
        if draw :
            self.redraw_column(column)

    # bottom row move clockwise
    def command_ctrl_d(self):
        self.row_transform_matrix(0, [0, 1, 4, 3], True)
    # bottom row move couter clockwise
    def command_D(self):
        self.row_transform_matrix(0, [3, 4, 1, 0], True)

    # top row move clockwise
    def command_ctrl_u(self):
        self.row_transform_matrix(2, [0, 1, 4, 3], True)
    # top row move couter clockwise
    def command_U(self):
        self.row_transform_matrix(2, [3, 4, 1, 0], True)

    # middle row move clockwise
    def command_ctrl_e(self):
        self.row_transform_matrix(1, [0, 1, 4, 3], True)
    # middle row move couter clockwise
    def command_E(self):
        self.row_transform_matrix(1, [3, 4, 1, 0], True)

    # top and middle row move clockwise
    def command_alt_u(self):
        self.row_transform_matrix(2, [0, 1, 4, 3])
        self.row_transform_matrix(1, [0, 1, 4, 3], True)
    # bottom and middle row move clockwise
    def command_alt_d(self):
        self.row_transform_matrix(1, [0, 1, 4, 3])
        self.row_transform_matrix(0, [0, 1, 4, 3], True)

    # left column moved
    def command_L(self):
        self.column_transform_matrix(0, [0, 2, 4, 5], True)
    # middle column moved
    def command_M(self):
        self.column_transform_matrix(1, [0, 2, 4, 5], True)
    # right column moved
    def command_R(self):
        self.column_transform_matrix(2, [0, 2, 4, 5], True)

    def onKeyHandler(self):
        # Handle key events
        #self.screen.onkey(self.UpMove, "Up")
        #self.screen.onkey(self.RightMove, "Right")
        #self.screen.onkey(self.DownMove, "Down")
        self.oncontrolkeypress(self.screen, self.command_ctrl_d, "d")
        self.screen.onkey(self.command_D, "D")
        self.oncontrolkeypress(self.screen, self.command_ctrl_u, "u")
        self.screen.onkey(self.command_U, "U")
        self.oncontrolkeypress(self.screen, self.command_ctrl_e, "e")
        self.screen.onkey(self.command_E, "E")
        self.onaltkeypress(self.screen, self.command_alt_d, "d")
        self.onaltkeypress(self.screen, self.command_alt_u, "u")
        self.screen.onkey(self.command_L, "L")
        self.screen.onkey(self.command_M, "M")
        self.screen.onkey(self.command_R, "R")
        self.screen.listen()

    def launch(self):
        self.draw_play_ground()
        self.onKeyHandler()
        self.screen.exitonclick()

    def __init__(self, side, title):
        self.side = side
        # Initialize turtle and screen
        self.screen = Screen()
        self.screen.setup(20 * side, 20 * side)
        self.screen.title(title)
        self.t = Turtle()
        self.t.speed(0)
        # Initialize playground values
        self.A = [[0 for j in range(0, 9)] for i in range(0, 6)]
        self.box_colors = {0: "#c5c8c1",  1: "#99cc33", 2: "#b43232", 3: "#b78ea3", 4: "#35516b", 5: "#bb7128"}
        for i in range(0, 6):
            for j in range(0, 9):
                self.A[i][j] = self.box_colors[i]

def main():
    g = Cube3x3x3(40, "Rubic Cube")
    g.launch()


if __name__ == "__main__":
    main()
