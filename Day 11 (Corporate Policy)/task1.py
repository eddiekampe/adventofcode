import string
import itertools

start_value = open("input.txt", "r").readline()
alphabet = string.ascii_lowercase
banned = "iol"


def has_sequence(password):
    for index in xrange(0, len(password) - 2):
        if password[index:index + 3] in alphabet:
            return True
    return False


def has_pairs(password):
    groups = itertools.groupby(password)
    return len([_ for _, v in groups if len(list(v)) > 1]) > 1


def has_no_banned(password):
    return not any(c in banned for c in password)


def increment(password):

    characters_as_int = [ord(c) for c in password]
    a_as_int, z_as_int = ord("a"), ord("z")

    index = -1

    while True:
        characters_as_int[index] += 1
        if characters_as_int[index] <= z_as_int:
            break
        else:
            characters_as_int[index] = a_as_int
            index -= 1

    return "".join(chr(n) for n in characters_as_int)


def password_generator(password):

    while not password[0] == "z":

        password = increment(password)
        if has_sequence(password) and has_no_banned(password) and has_pairs(password):
            yield password

generator = password_generator(start_value)

print next(generator)
