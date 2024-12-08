from flask import Flask, render_template, request

from interface import APIInterface
from consts import api_key

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def main_page_post():
    try:
        form = request.form
        start, end = form['start_point'], form['end_point']
    except Exception as e:
        print(e)
        return render_template('error_page.html', error_message='Ошибка получения данных от формы')
    try:
        api = APIInterface(api_key=api_key)
        start_weather = api.weather(start)
        end_weather = api.weather(end)

    except IndexError:
        return render_template('error_page.html', error_message='Точка не найдена')
    except Exception:
        return render_template('error_page.html', error_message='Нет доступа к API')
    return render_template('index2.html', start=start_weather, end=end_weather)


if __name__ == '__main__':
    app.run()
