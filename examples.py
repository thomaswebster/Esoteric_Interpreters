import brainfuckInterpreter as bf

#prints hello world!
helloworld = bf.BrainFuck("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.")
print(helloworld.run())

#multiplys two integers together
multiplyints = bf.BrainFuck(",>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.")
print(ord(multiplyints.run(chr(5) + chr(7))))

#echos given input
echo1 = bf.BrainFuck(",[.[-],]")
print(echo1.run("echo echo echo" + chr(0)))

#another way of echoing given input
echo2 = bf.BrainFuck(",+[-.,+]")
print(echo2.run("echo again!" + chr(255)))
