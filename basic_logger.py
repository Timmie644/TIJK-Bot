import os

os.system("color")


def info(msg: str, name: str):
    print(f"\u001b[34m[INFO]\u001b[0m {msg} ({os.path.basename(name)})")


def debug(msg: str, name: str):
    print(f"\u001b[33m[DEBUG]\u001b[0m {msg} ({os.path.basename(name)})")


def warning(msg: str, name: str):
    print(f"\u001b[31;1m[WARNING]\u001b[0m {msg} ({os.path.basename(name)})")


def error(msg: str, name: str):
    print(f"\u001b[31m[ERROR]\u001b[0m {msg} ({os.path.basename(name)})")


def critical(msg: str, name: str):
    print(f"\u001b[35m[CRITICAL]\u001b[0m {msg} ({os.path.basename(name)})")


if __name__ == "__main__":
    info("This is the main file", __file__)
    debug("This is the main file", __file__)
    warning("This is the main file", __file__)
    error("This is the main file", __file__)
    critical("This is the main file", __file__)
