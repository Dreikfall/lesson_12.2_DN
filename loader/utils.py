import json
from exceptions import *
from config import *


def load_json(path):
    try:
        with open(path, "r", encoding="UTF-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def save_picture(picture):
    allowed_type = ["jpg", "png", "gif", "jpeg"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in allowed_type:
        raise WrongImgType(f'Неверный формат файла! Допустимы только {", ".join(allowed_type)}!')
    picture_path = f'{UPLOAD_FOLDER}/{picture.filename}'
    picture.save(picture_path)
    return picture_path


def add_post(post_list, post):
    post_list.append(post)
    with open(POST_PATH, "w", encoding="UTF-8") as f:
        json.dump(post_list, f, indent=2, ensure_ascii=False)
