from modules import encode, recognize

from pathlib import Path

ENCODINGS_PATH = Path("encodings/encodings.pkl")
TRAIN_PATH = Path("data/train")

encode("hog", ENCODINGS_PATH, TRAIN_PATH)

# for filepath in Path("modules/face_rec/test").glob("*"):
#     recognize(filepath, "hog", Path("modules/face_rec/output/encodings.pkl"))
