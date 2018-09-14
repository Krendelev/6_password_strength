import string
import argparse
import getpass


def check_case(password, case):
    return not set(password).isdisjoint(set(case))


def assess_letters(password):
    strings = {
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation,
    }
    return sum(check_case(password, string) for string in strings)


def check_length(password):
    min_length = 8
    return len(password) >= min_length


def check_repetitions(password):
    return len(password) > len(set(password))


def is_in_blacklist(password, blacklist):
    return password in blacklist


def get_password_strength(password):
    weight_factor = 2
    return (
        assess_letters(password) * weight_factor +
        check_length(password) * weight_factor -
        check_repetitions(password)
        )


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
            with open(args.blacklist) as fh:
                evaluated_password = is_in_blacklist(password, fh.read().split())
        except FileNotFoundError:
            print('Blacklist not found')
    if not evaluated_password:
        evaluated_password = get_password_strength(password)
    print('Passwords strength is {:d} out of 10'.format(evaluated_password))
