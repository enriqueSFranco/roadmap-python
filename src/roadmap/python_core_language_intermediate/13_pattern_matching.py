import re
import sys
import traceback


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm teapot"
        case _:
            return "Something's wrong with the internet"


def factorial(n: int):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * factorial(n - 1)


match match := re.match(r"([^@]+)@.*", "alice@email.com").group(1):
    case "alice":
        print("Welcome, Alice!")
    case "bob":
        print("Welcome, Bob!")
    case _:
        print("Welcome, stranger!")


PROMPT = "\N{SNAKE}"
COMMANDS = ("help", "exit", "quit")


def main():
    print('Type "help" for more information, "exit" or "quit" to finish.')
    while True:
        try:
            match input(PROMPT):
                case command if command.lower() in COMMANDS:
                    match command.lower():
                        case "help":
                            print(f"Python {sys.version}")
                        case "exit" | "quit":
                            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    main()
