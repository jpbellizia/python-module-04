def secure_archive(file_name: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    """Safely read or write a file using the with statement.

    action: "read" (default) or "write".
    Return (True, file content or success message) or (False, error).
    """
    try:
        if action == "read":
            with open(file_name, "r") as file:
                return (True, file.read())
        if action == "write":
            with open(file_name, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        return (False, f"Invalid action '{action}' (use 'read' or 'write')")
    except (OSError, UnicodeDecodeError) as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive("ancient_fragment.txt")
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_archive.txt", "write", result[1]))
    else:
        print((False, "Nothing to write: previous read failed"))


if __name__ == "__main__":
    main()
