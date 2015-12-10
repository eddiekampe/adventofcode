def calc_look(start_string):

    counter = 1
    new_string = ""

    for index, value in enumerate(start_string):

        if index == 0:
            continue

        if start_string[index - 1] == value:
            counter += 1
        else:
            new_string += "{}{}".format(counter, start_string[index - 1])
            counter = 1

    return new_string + "{}{}".format(counter, start_string[-1])


if __name__ == "__main__":

    acc_start = open("input.txt", "r").readline()
    result = reduce(lambda acc, _: calc_look(acc), xrange(0, 50), acc_start)
    print len(result)
