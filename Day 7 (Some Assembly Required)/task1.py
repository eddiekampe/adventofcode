commands = [line.rstrip("\n") for line in open("input.txt", "r")]
gates = dict()


def get_signal(wire):

    if isinstance(wire, int) or wire.isdigit():
        return int(wire)

    operators = wire.split(" ")

    if len(operators) == 1:  # Assignment
        gates[wire] = get_signal(gates[operators[0]])
        return gates[wire]

    elif len(operators) == 2:  # NOT
        return ~get_signal(operators[1])

    elif len(operators) == 3:

        left, operator, right = operators

        if operator == "AND":
            return get_signal(left) & get_signal(right)
        elif operator == "OR":
            return get_signal(left) | get_signal(right)
        elif operator == "RSHIFT":
            return get_signal(left) >> get_signal(right)
        elif operator == "LSHIFT":
            return get_signal(left) << get_signal(right)


if __name__ == "__main__":

    for command in commands:
        _input, gate = command.split(" -> ")
        gates[gate] = _input

    print get_signal("a")
