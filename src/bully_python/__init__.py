import sys


class CustomException(Exception):
    pass

def recurse(depth=0):
    try:
        raise CustomException()
    except CustomException:
        recurse(depth + 1)


def main():
    recurse()

if __name__ == "__main__":
    main()