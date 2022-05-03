from flask import Blueprint, render_template, request, abort
import logging
from loader.utils import *
from config import *

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="logger.log", level=logging.INFO)


@loader_blueprint.route("/post")
def adding_new_post_page():
    """Страница добавления постов"""

    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def adding_new_post_by_user():
    """Добавление нового поста, сохранение картинки,
    страница подтверждения добавления поста"""

    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены, отсутствует часть данных.")
        return "Отсутствует часть данных"
    posts = load_json(POST_PATH)
    try:
        new_post = {"pic": save_picture(picture), "content": content}
    except WrongImgType:
        abort(400)
    add_post(posts, new_post)
    return render_template("post_uploaded.html", new_post=new_post)