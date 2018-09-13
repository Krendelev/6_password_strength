import string
import argparse


CHECK_WEIGHT = 2


def check_case(password, case):
    return not set(password).isdisjoint(set(case))


def check_letters(password):
    strings = {
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation,
    }
    return sum(
        CHECK_WEIGHT * check_case(password, string)
        for string in strings
        )


def check_length(password):
    min_length = 8
    return CHECK_WEIGHT * (len(password) >= min_length)


def check_repetitions(password):
    return len(password) > len(set(password))


def check_list(password, password_list):
    try:
        with open(password_list) as list_handler:
            return int(password in list_handler.read())
    except FileNotFoundError:
        print('Password list not found')


def get_password_strength(password, password_list=None):
    return (
        check_list(password, password_list) if password_list else None
        ) or (
        check_letters(password) +
        check_length(password) -
        check_repetitions(password)
        )


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('password')
    parser.add_argument('password_list', nargs='?')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    print('Your passwords strength is {} out of 10'.format(
        get_password_strength(args.password, args.password_list)
        ))
