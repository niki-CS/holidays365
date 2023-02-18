from imp import reload
from flask import Flask, render_template, request
import json
import requests
# from datetime import date

app = Flask(__name__)
# api_key = '45a49a731ce9d7cc0e72294530e4da7647fea981'

@app.route('/')
def index():
#    today = str(date.today())
#    country_data = request.form['country']
#    response = requests.get(f'https://calendarific.com/api/v2/holidays?&api_key=45a49a731ce9d7cc0e72294530e4da7647fea981&country={country_data}&year={today}')
#    data = response.json
    return render_template('index.html')


@app.route('/test', methods=["post"])
def prince():
    # today = str(date.today())
    country_data = request.form['country']
    print(country_data)
    response = requests.get(f'https://date.nager.at/api/v3/NextPublicHolidays/{country_data}')
    data = response.json()
    print(data)

    # for localName in data:
    #     for name in data:
    #         for date in data:
    #             print(localName, name, date)
    return render_template('index2.html', data = data)


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')