from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


CATEGORIES = [('0', 'Без категории'), ('1', 'Сериалы, фильмы, спектакли'),
                                                 ('2', 'Рецепты'), ('3', 'Рассказы из жизни'), ('4', 'Хобби'),
                                                 ('5', 'Книги'), ('6', 'Новости'), ('7', 'Путешествия'),
                                                 ('8', 'Лайфхаки'), ('9', 'Мемы'), ('10', 'Домашние животные'),
                                                 ('11', 'Дача, садоводство'), ('12', 'Мода и стиль'),
                                                 ('13', 'Творчество'), ('14', 'Личные рекорды'),
                                                 ('15', 'Здоровый образ жизни')]


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    category = SelectField('Категория', choices=CATEGORIES)
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')
