import sys

def bf_interpreter():
    
    bf_string = ""
    bf_list = [0] * 50000
    data_pointer = 0
    bracket_stack = []
    bracket_pair = {}
    i = 0

    while True:
        line = input()
    
        if line.strip() == "STOP":
            break
        bf_string += line

    for index, character in enumerate(bf_string):
        if character == "[":
            bracket_stack.append(index)
        elif character == "]":
            if bracket_stack:
                begin = bracket_stack.pop()
                bracket_pair[begin] = index
                bracket_pair[index] = begin

    while i < len(bf_string):
        character = bf_string[i]

        if character == ">":
            data_pointer += 1
            if data_pointer >= len(bf_string):
                data_pointer = 0

        elif character == "<":
            data_pointer -= 1
            if data_pointer < 0:
                data_pointer = len(bf_string) - 1

        elif character == "+":
            bf_list[data_pointer] = bf_list[data_pointer] + 1

        elif character == "-":
            bf_list[data_pointer] = bf_list[data_pointer] - 1

        elif character == ".":
            print(chr(bf_list[data_pointer]), end="")

        elif character == ",":
            input_char = sys.stdin.read(1)
            number_value = ord(input_char)
            bf_list[data_pointer] = number_value

        elif character == "[":
            if bf_list[data_pointer] == 0:
                i = bracket_pair[i]

        elif character == "]":
            if bf_list[data_pointer] != 0:
                i = bracket_pair[i]

        i += 1

bf_interpreter()