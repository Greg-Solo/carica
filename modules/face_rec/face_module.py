from pathlib import Path

import face_recognition
import pickle
from collections import Counter


def encode(
    model: str,
    encodings_location: Path,
    train_location: Path,
) -> None:
    names = []
    encodings = []
    for filepath in train_location.glob("*/*"):
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)

        face_locations = face_recognition.face_locations(image, model=model)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)

    Path("encodings").mkdir(exist_ok=True)
    name_encodings = {"names": names, "encodings": encodings}
    with encodings_location.open(mode="wb") as f:
        pickle.dump(name_encodings, f)


def recognize(
    image_location: str,
    model: str,
    encodings_location: Path,
) -> None:
    name = []
    bbox = []

    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)

    input_face_locations = face_recognition.face_locations(input_image, model=model)

    if input_face_locations:
        input_face_encodings = face_recognition.face_encodings(
            input_image, input_face_locations
        )

        for bounding_box, unknown_encoding in zip(
            input_face_locations, input_face_encodings
        ):
            _name = _recognize_face(unknown_encoding, loaded_encodings)
            if not _name:
                _name = "Unknown"
            name.append(_name)
            bbox.append(bounding_box)
    else:
        name.append("Undetected")
        bbox.append(())

    return name, bbox


def _recognize_face(
    unknown_encoding,
    loaded_encodings,
):
    boolean_matches = face_recognition.compare_faces(
        loaded_encodings["encodings"], unknown_encoding
    )
    votes = Counter(
        name for match, name in zip(boolean_matches, loaded_encodings["names"]) if match
    )
    if votes:
        return votes.most_common(1)[0][0]
    else:
        return None
