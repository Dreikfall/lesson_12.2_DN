from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint
import logging
# from functions import ...

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.errorhandler(400)
def bad_request_error(error):
    """Вызов страницы ошибки"""

    logging.info(error)
    return render_template("error_400.html", error=error)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run(debug=True)

