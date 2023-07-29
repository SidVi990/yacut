from flask import redirect, flash, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap


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
            short = URLMap.generate_short_url()
        url = URLMap(
            original=original,
            short=short
        )
        db.session.add(url)
        db.session.commit()
        return (render_template(
            'index.html',
            form=form,
            short_url=URLMap.get_full_link(short)
        ), 200)
    return render_template("index.html", form=form)


@app.route('/<string:short>')
def link_redirect(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original, 302
    )
