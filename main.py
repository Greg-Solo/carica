from modules import encode, recognize

from pathlib import Path

ENCODINGS_PATH = Path("encodings/encodings.pkl")
TRAIN_PATH = Path("data/train")
TEST_PATH = Path("data/test")

# encode("hog", ENCODINGS_PATH, TRAIN_PATH)

for filepath in TEST_PATH.glob("*"):
    _name, _bbox = recognize(filepath, "hog", ENCODINGS_PATH)
    print(_name, _bbox)
