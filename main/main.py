from flask import Blueprint, render_template, request
import logging
from main.utils import tuple_posts_by_search
from config import POST_PATH
from exceptions import *

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprint.route("/")
def page_index():
    """Открытие главной страницы"""

    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    """Страница поиска, поиск по вхождению слова"""

    s = request.args.get("s")
    logging.info("Выполняется поиск")
    try:
        filtered_posts = tuple_posts_by_search(s, POST_PATH)
    except DataJsonError:
        return "Проблема с загрузкой json файла"
    return render_template("post_list.html", posts=filtered_posts, s=s)

