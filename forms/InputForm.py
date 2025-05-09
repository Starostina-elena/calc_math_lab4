from flask_wtf import FlaskForm
from wtforms import FileField, FieldList, FormField, FloatField, SubmitField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileAllowed




class RowForm(FlaskForm):
    class Meta:
        csrf = False
    x = FloatField('X')
    y = FloatField('Y')


class InputForm(FlaskForm):
    rows = FieldList(FormField(RowForm), min_entries=8, max_entries=12)
    file = FileField('Или загрузите файл', validators=[FileAllowed(['txt'], 'txt files only')])
    submit = SubmitField('Готово')

    def validate(self, *args, **kwargs):
        if self.file.data:
            return True
        else:
            for row in self.rows:
                if not row.x or not row.y:
                    return False
        return super().validate(*args, **kwargs)
