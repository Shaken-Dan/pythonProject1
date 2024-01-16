from flask import Flask, render_template, request
import flask_wtf
import wtforms


class SubscriptionForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name")
    email = wtforms.StringField("Email")
    submit = wtforms.SubmitField("Submit")


class IceCreamForm(flask_wtf.FlaskForm):
    tastes = wtforms.SelectField("Taste")
    toppings = wtforms.SelectMultipleField("Toppings")
    cup_size = wtforms.RadioField("Cup Size")
    submit = wtforms.SubmitField("Submit")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'aadd8565f55550006xcnmkjk154'


@app.route('/search')
def search_view():
    return render_template('search.html')


@app.route('/ice', methods=['GET', 'POST'])
def ice_view():
    form = IceCreamForm()
    if request.method == 'GET' and form.validate():
        return render_template('ice.html', form=form)
    return f'Thank you, {form.name.data}, for subscribing!'


@app.route('/getsearch')
def get_search_view():
    mail = request.args.get('mail')
    return f'Search page, parameter acquired by GET, searching for...  {mail}'


@app.route('/postsearch', methods=['POST'])
def post_search_view():
    mail = request.form.get('mail')
    return f'Search page, parameter acquired by POST, searching for...  {mail}'


if __name__ == '__main__':
    app.run(debug=True)
