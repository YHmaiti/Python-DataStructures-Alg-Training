import stack

string = " ok so test this and see how the reverse message becomes "
reversed_string = ""
s = stack.stack()

for i in string:
    s.push(i)


while(s.is_empty() == False):
    reversed_string += (s.pop())


print(reversed_string)