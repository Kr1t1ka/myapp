import sys

from db import db
from cases import Cases


def error(text):
    print(f'ERROR: {text}')


def selector(params):
    case = Cases(db=db)
    if params[1] == '1':
        case.create_db()
    elif params[1] == '2':
        if len(params) < 5:
            error('Invalid parameter')
        else:
            case.create_user(params=params)
    elif params[1] == '3':
        case.print_user()
    elif params[1] == '4':
        case.insert_user()
    elif params[1] == '5':
        case.print_f_user()
    else:
        error('Invalid parameter')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        selector(sys.argv)
    else:
        error('You must pass the parameters')
