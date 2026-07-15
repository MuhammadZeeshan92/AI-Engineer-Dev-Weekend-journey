# ==========================================
# Main CLI Script
# ==========================================

from file_processor import read_file, process_text, write_file


def main():
    input_file = "input.txt"
    output_file = "output.txt"

    try:
        text = read_file(input_file)

        processed_text, statistics = process_text(text)

        write_file(output_file, processed_text, statistics)

        print("File processed successfully!")
        print(f"Output written to '{output_file}'")

    except FileNotFoundError:
        print("Error: Input file not found.")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except Exception as error:
        print(f"Unexpected Error: {error}")

    finally:
        print("Program execution completed.")


if __name__ == "__main__":
    main()