import os

TEXT = "I'm afraid for the calendar. Its days are numbered."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    assert 1 <= len(TEXT) <= 200, "entry must be 1 to 200 code points"
    assert TEXT.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
