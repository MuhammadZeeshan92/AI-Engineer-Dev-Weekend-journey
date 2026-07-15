# ==========================================
# File Processing Functions
# ==========================================

from utils import count_lines, count_words, count_characters


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def process_text(text):
    processed_text = text.upper()

    statistics = {
        "lines": count_lines(text),
        "words": count_words(text),
        "characters": count_characters(text)
    }

    return processed_text, statistics


def write_file(file_path, processed_text, statistics):
    with open(file_path, "w") as file:
        file.write(processed_text)
        file.write("\n\nStatistics\n")
        file.write("-" * 20 + "\n")
        file.write(f"Lines: {statistics['lines']}\n")
        file.write(f"Words: {statistics['words']}\n")
        file.write(f"Characters: {statistics['characters']}\n")