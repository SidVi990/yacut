from flask import redirect, flash, render_template
from http import HTTPStatus

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import generate_short_url


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        original = form.original_link.data
        short = form.custom_id.data
        if URLMap.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!')
            return render_template('index.html', form=form)
        if not short:
            short = generate_short_url()
        url = URLMap(
            original=original,
            short=short
        )
        db.session.add(url)
        db.session.commit()
        return (render_template(
            'index.html',
            form=form,
            short_url='http://localhost/' + short
        ), HTTPStatus.OK)
    return render_template("index.html", form=form)


@app.route('/<string:short>')
def link_redirect(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original, HTTPStatus.FOUND
    )
