import re
from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def create_link():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    original = data.get('url')
    short = data.get('custom_id')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if short is None or short == '':
        short = URLMap.generate_short_url()
    if URLMap.query.filter_by(short=short).first() is not None:
        raise InvalidAPIUsage(f'Имя "{short}" уже занято.', 400)
    if len(short) > 16 or not re.match(r"^[a-zA-Z0-9]*$", short):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    link = URLMap(
        original=original,
        short=short,
    )
    db.session.add(link)
    db.session.commit()
    return jsonify(link.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_link(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if not url:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url.original}), 200
