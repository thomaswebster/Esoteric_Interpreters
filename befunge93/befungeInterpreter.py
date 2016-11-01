from random import choice

class Befunge93(object):
    DIRECTIONS = {"<":[-1,0], ">":[1,0], "^":[0,-1], "v":[0,1]}

    def run(self):
        self.output = ""
        self.iptr, self.direction = [0,0],[1,0]
        self.stack = [0]

        while True:
            instruction = self.grid[self.iptr[1]][self.iptr[0]]
            if instruction in "0123456789": self.stack.append(int(instruction))
            elif instruction in "<>v^?":
                if instruction == "?": instruction = choice("<>v^")
                self.direction = Befunge93.DIRECTIONS[instruction]
            elif instruction in "+-*/%": self.stack[-2:] = [eval(str(self.stack[-2]) + instruction + str(self.stack[-1]))]
            elif instruction == "!": self.stack[-1] = not self.stack[-1]
            elif instruction == "`": self.stack[-2:] = [self.stack[-2]>self.stack[-1]]
            elif instruction == ":": self.stack += [self.stack[-1]]
            elif instruction == ".": self.output += str(self.stack.pop())
            elif instruction == ",": self.output += chr(self.stack.pop())
            elif instruction == "_": self.direction = [(self.stack.pop()==0)*2-1,0]
            elif instruction == "|": self.direction = [0,(self.stack.pop()==0)*2-1]
            elif instruction == "\"":
                self.iptr = map(sum, zip(self.iptr, self.direction))
                while self.grid[self.iptr[1]][self.iptr[0]] != "\"":
                    self.stack.append(ord(self.grid[self.iptr[1]][self.iptr[0]]))
                    self.iptr = map(sum, zip(self.iptr, self.direction))
            elif instruction == "\\": self.stack[-2:] = self.stack[-2:][::-1]
            elif instruction == "$": self.stack.pop()
            elif instruction == "#": self.iptr = map(sum, zip(self.iptr, self.direction))
            elif instruction == "p":
                y,x,v = self.stack.pop(),self.stack.pop(),self.stack.pop()
                grid[y][x] = chr(v)
            elif instruction == "g":
                y,x = self.stack.pop(), self.stack.pop()
                stack.append(ord(grid[x][y]))
            elif instruction == "@": return self.output
            self.iptr = list(map(sum, zip(self.iptr, self.direction)))
        
    def __init__(self, code):
        self.grid = list(map(list,code.split("\n")))
