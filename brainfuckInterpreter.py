class BrainFuck(object):
        def run(self, inp = ""):
            '''initialises system and runs the program, returning the output string'''
            self.memory, self.mptr, self.cptr, self.iptr = [0], 0, 0, 0
            self.output, self.inp = "", inp

            while self.cptr < len(self.code):
                if self.code[self.cptr] == "<":
                    if self.mptr: self.mptr -= 1
                elif self.code[self.cptr] == ">":
                    if self.mptr == len(self.memory)-1:
                        self.memory += [0]
                    self.mptr += 1
                elif self.code[self.cptr] == "+":
                    self.memory[self.mptr] += 1
                elif self.code[self.cptr] == "-":
                    self.memory[self.mptr] -= 1
                elif self.code[self.cptr] == ".":
                    self.output+=chr(self.memory[self.mptr])
                elif self.code[self.cptr] == ",":
                    self.memory[self.mptr] = ord(self.inp[self.iptr])
                    self.iptr += 1
                elif self.code[self.cptr] == "[":
                    if not self.memory[self.mptr]: self.cptr = self.brackets[self.cptr]
                elif self.code[self.cptr] == "]":
                    if self.memory[self.mptr]: self.cptr = self.brackets[self.cptr]

                self.cptr += 1
                self.memory[self.mptr] = self.memory[self.mptr]%256
            return self.output
        
        def makejumptable(self, code):
            '''returns a dictionary of indexes, each jumping to matching bracket'''
            temp, jumptable = [], {}
            for index, command in enumerate(code):
                if command == "[": temp.append(index)
                elif command == "]":
                    to = temp.pop()
                    jumptable[to], jumptable[index] = index, to
            return jumptable
        
        def __init__(self, code):
            '''strips code unwanted cahracters, creates bracket jumptable'''
            self.code = list(filter(lambda x: x in "<>.,+-[]", code))
            self.brackets = self.makejumptable(self.code)
