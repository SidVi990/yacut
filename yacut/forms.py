from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import (
    URL,
    DataRequired,
    Length,
    Regexp,
)

from .constants import SHORT_MAX_LENGTH


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Оригинальная ссылка',
        validators=(
            DataRequired(message='Поле должно быть заполнено'),
            URL(message='Некорректный адрес URL'),
        ),
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=(
            Length(
                max=SHORT_MAX_LENGTH,
                message='Короткая ссылка не должна превышать 16 символов',
            ),
            Regexp(
                r"^[a-zA-Z0-9]*$",
                message=('Допускаются только латинские буквы и цифры'),
            ),
        ),
    )
    submit = SubmitField('Сократить')