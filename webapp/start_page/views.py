from flask import render_template
from flask import Blueprint
from webapp import config

blueprint = Blueprint('start', __name__)


@blueprint.route('/', methods=['GET','POST'])
def index():
    page_title = config.WEB_TITTLE
    message = config.WEB_TITTLE
    return render_template('start_page/main.html',
                        page_title=page_title,
                        message=message)