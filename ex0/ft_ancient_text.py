import sys
import typing


def main() -> None:
    """Read a file given on the command line and display it like cat."""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    file_name: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "r")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return
    try:
        content: str = file.read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error reading file '{file_name}': {error}")
        return
    finally:
        file.close()
    print("---\n")
    print(content)
    print("---")
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
