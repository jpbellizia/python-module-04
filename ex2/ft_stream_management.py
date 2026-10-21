import sys
import typing


def print_error(message: str) -> None:
    """Send an error message to the error stream (stderr)."""
    sys.stdout.flush()
    print(f"[STDERR] {message}", file=sys.stderr)


def read_archive(file_name: str) -> str | None:
    """Open, read and close a file. Return its content or None on error."""
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "r")
    except OSError as error:
        print_error(f"Error opening file '{file_name}': {error}")
        return None
    try:
        content: str = file.read()
    except (OSError, UnicodeDecodeError) as error:
        print_error(f"Error reading file '{file_name}': {error}")
        return None
    finally:
        file.close()
    print("---\n")
    print(content)
    print("---")
    print(f"File '{file_name}' closed.")
    return content


def transform(content: str) -> str:
    """Add the archive character '#' at the end of each line."""
    result: str = ""
    for line in content.splitlines():
        result += line + "#\n"
    return result


def save_archive(file_name: str, content: str) -> None:
    """Create (or replace) a file and write the content in it."""
    print(f"Saving data to '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "w")
    except OSError as error:
        print_error(f"Error opening file '{file_name}': {error}")
        print("Data not saved.")
        return
    try:
        file.write(content)
    except OSError as error:
        print_error(f"Error writing file '{file_name}': {error}")
        print("Data not saved.")
        return
    finally:
        file.close()
    print(f"Data saved in file '{file_name}'.")


def read_user_input(prompt: str) -> str:
    """Read one line from stdin without using input()."""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    line: str = sys.stdin.readline()
    return line.rstrip("\n")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content: str | None = read_archive(sys.argv[1])
    if content is None:
        return
    new_content: str = transform(content)
    print("\nTransform data:")
    print("---\n")
    print(new_content)
    print("---")
    new_name: str = read_user_input("Enter new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
        return
    save_archive(new_name, new_content)


if __name__ == "__main__":
    main()
