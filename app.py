import io

from flask import Flask, render_template, request, send_file
from forms import InputForm

from utils import lineal, polinom2, polinom3, exponential, logarithmic, poweric

app = Flask(__name__)
app.secret_key = 'fjJGKJGVkjgjkhvNBvJGGhbjhgb657g'


@app.route('/download_report', methods=['POST'])
def download_report():
    report_text = request.form['report_text']
    report = io.StringIO(report_text)
    return send_file(io.BytesIO(report.getvalue().encode('utf-8')),
                     mimetype='text/plain',
                     as_attachment=True,
                     download_name='report.txt')


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
        try:
            lineal_a, lineal_b, lineal_r, lineal_R2, lineal_s, lineal_f, lineal_eps = lineal.lineal(x, y)
            pol2_a, pol2_b, pol2_c, pol2_R2, pol2_s, pol2_f, pol2_eps = polinom2.polinom2(x, y)
            pol3_a, pol3_b, pol3_c, pol3_d, pol3_R2, pol3_s, pol3_f, pol3_eps = polinom3.polinom3(x, y)
            try:
                exp_a, exp_b, exp_R2, exp_s, exp_f, exp_eps = exponential.exponential(x, y)
                exp_error = False
            except ValueError:
                exp_error = True
                exp_a, exp_b, exp_R2, exp_s, exp_f, exp_eps = None, None, None, None, None, None
            try:
                log_a, log_b, log_R2, log_s, log_f, log_eps = logarithmic.logarithmic(x, y)
                log_error = False
            except ValueError:
                log_error = True
                log_a, log_b, log_R2, log_s, log_f, log_eps = None, None, None, None, None, None
            try:
                pow_a, pow_b, pow_R2, pow_s, pow_f, pow_eps = poweric.poweric(x, y)
                pow_error = False
            except ValueError:
                pow_error = True
                pow_a, pow_b, pow_R2, pow_s, pow_f, pow_eps = None, None, None, None, None, None
            best_approximation = ''
            s_values = [lineal_s, pol2_s, pol3_s]
            if exp_s is not None:
                s_values.append(exp_s)
            if log_s is not None:
                s_values.append(log_s)
            if pow_s is not None:
                s_values.append(pow_s)
            min_s = min(s_values)
            if min_s == lineal_s:
                best_approximation = 'Линейная'
            elif min_s == pol2_s:
                best_approximation = 'Полином 2 степени'
            elif min_s == pol3_s:
                best_approximation = 'Полином 3 степени'
            elif min_s == exp_s:
                best_approximation = 'Экспоненциальная'
            elif min_s == log_s:
                best_approximation = 'Логарифмическая'
            elif min_s == pow_s:
                best_approximation = 'Степенная'
            center_x = (max(x) + min(x)) / 2
            center_y = (max(y) + min(y)) / 2
            proportion = max(max(y) - min(y), max(x) - min(x))
            return render_template('result.html', x=x, y=y, lineal_a=lineal_a, lineal_b=lineal_b,
                                   lineal_r=lineal_r, lineal_R2=lineal_R2,
                                   lineal_s=lineal_s, lineal_f=lineal_f, lineal_eps=lineal_eps,
                                   pol2_a=pol2_a, pol2_b=pol2_b, pol2_c=pol2_c, pol2_s=pol2_s,
                                   pol2_f=pol2_f, pol2_eps=pol2_eps, pol2_R2=pol2_R2,
                                   pol3_a=pol3_a, pol3_b=pol3_b, pol3_c=pol3_c, pol3_d=pol3_d,
                                   pol3_R2=pol3_R2, pol3_s=pol3_s, pol3_f=pol3_f, pol3_eps=pol3_eps,
                                   exp_a=exp_a, exp_b=exp_b, exp_s=exp_s, exp_f=exp_f,
                                   exp_eps=exp_eps, exp_R2=exp_R2, exp_error=exp_error,
                                   log_a=log_a, log_b=log_b, log_s=log_s, log_f=log_f,
                                   log_eps=log_eps, log_R2=log_R2, log_error=log_error,
                                   pow_a=pow_a, pow_b=pow_b, pow_s=pow_s, pow_f=pow_f,
                                   pow_eps=pow_eps, pow_R2=pow_R2, pow_error=pow_error,
                                   desmos_left_view = center_x - proportion,
                                   desmos_right_view = center_x + proportion,
                                   desmos_up_view = center_y + proportion,
                                   desmos_down_view = center_y - proportion,
                                   best_approximation=best_approximation)
        except ValueError as e:
            return render_template('main.html', form=form, message=f'Ошибка: {e}')
    elif request.method == 'POST':
        return render_template('main.html', form=form, message='Некорректные данные')

    return render_template('main.html', form=form)


if __name__ == '__main__':
    app.run()
