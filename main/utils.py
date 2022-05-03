import json
from exceptions import *


def load_json(path):
    try:
        with open(path, "r", encoding="UTF-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def tuple_posts_by_search(substring, path):
    posts = load_json(path)
    tuple_posts = ()
    for post in posts:
        if substring.lower() in post["content"].lower():
            tuple_posts += (post,)
    return tuple_posts
