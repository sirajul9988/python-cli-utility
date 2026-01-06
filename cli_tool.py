import argparse
import sys

def greet(name):
    print(f"Hello, {name}! Welcome to the CLI Utility.")

def main():
    parser = argparse.ArgumentParser(
        description="Simple Python CLI Utility"
    )
    parser.add_argument(
        "--name",
        type=str,
        required=True,
        help="Name of the user"
    )

    args = parser.parse_args()
    greet(args.name)

if __name__ == "__main__":
    main()
