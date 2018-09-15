import string
import argparse
import getpass


def check_case(password, case):
    return not set(password).isdisjoint(set(case))


def check_length(password):
    min_length = 8
    return len(password) >= min_length


def check_repetitions(password):
    return len(password) > len(set(password))


def get_password_strength(password):
    weight_factor = 2
    strings = {
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.punctuation,
        string.digits,
    }
    case_count = sum(check_case(password, string) for string in strings)
    return (
        case_count * weight_factor +
        check_length(password) * weight_factor -
        check_repetitions(password)
        )


def load_blacklist(path):
    with open(path) as file_handler:
        return file_handler.read().splitlines()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('blacklist', nargs='?')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    password = getpass.getpass('Enter your password: ')
    evaluated_password = False
    if args.blacklist:
        try:
            evaluated_password = password in load_blacklist(args.blacklist)
        except FileNotFoundError:
            print('Blacklist not found')
    if not evaluated_password:
        evaluated_password = get_password_strength(password)
    print('Passwords strength is {:d} out of 10'.format(evaluated_password))
