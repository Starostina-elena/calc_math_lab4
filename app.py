from flask import Flask, render_template, request
from forms import InputForm


app = Flask(__name__)
app.secret_key = 'fjJGKJGVkjgjkhvNBvJGGhbjhgb657g'


@app.route('/', methods=['GET', 'POST'])
def main():
    form = InputForm.InputForm()

    if form.validate_on_submit():
        if form.file.data:
            file_data = request.files.get('file').read().decode('utf-8').strip().split('\n')

            rows = []
            try:
                for line in file_data:
                    x, y = map(lambda el: float(el.replace(',', '.')), line.split())
                    rows.append({'x': x, 'y': y})
                if not (8 <= len(rows) <= 12):
                    raise ValueError("File must contain between 8 and 12 rows.")
            except Exception as e:
                return render_template('main.html', form=form, message=f'Invalid file format: {e}')

            for i, row in enumerate(rows):
                form.rows[i].x.data = row['x']
                form.rows[i].y.data = row['y']

        data = [{'x': row.x.data, 'y': row.y.data} for row in form.rows]
        x = []
        y = []
        for row in data:
            x.append(row['x'])
            y.append(row['y'])
        a, b, S, eps = lineal(x, y)
        return "Form submitted successfully!"
    elif request.method == 'POST':
        return render_template('main.html', form=form, message='Некорректные данные')

    return render_template('main.html', form=form)


if __name__ == '__main__':
    app.run()
