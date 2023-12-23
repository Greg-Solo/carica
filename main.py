from face_rec import encode, recognize

from pathlib import Path

DEFAULT_ENCODINGS_PATH = Path("face_rec/output/encodings.pkl")

encode("hog", DEFAULT_ENCODINGS_PATH)

# for filepath in Path("face_rec/test").glob("*"):
#     recognize(filepath, "hog", Path("face_rec/output/encodings.pkl"))
