from flask import flash, jsonify, app, Flask
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)


zodiac_signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']


@app.route('/horoscope/<string:zodiac_sign>')
def getHoroscope(zodiac_sign):
    if zodiac_sign in zodiac_signs:
        url = f'https://horo.mail.ru/prediction/{zodiac_sign}/today/'
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        horoscope = soup.find('div', {'class': 'article__item article__item_alignment_left article__item_html'})
        prediction = horoscope.find('p').text.strip()

        data = {
            'zodiac_sign': zodiac_sign,
            'prediction': prediction,
        }

        return jsonify(data)
    else:
        return jsonify({'error': 'Неверный знак зодиака'})

@app.route('/allHoros')
def getAllHoros():
    all_horoscopes = {}
    for zodiac_sign in zodiac_signs:
        url = f'https://horo.mail.ru/prediction/{zodiac_sign}/today/'
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        horoscope = soup.find('div', {'class': 'article__item article__item_alignment_left article__item_html'})
        prediction = horoscope.find('p').text.strip()

        data = {
            'zodiac_sign': zodiac_sign,
            'prediction': prediction,
        }

        all_horoscopes[zodiac_sign] = data

    return jsonify(all_horoscopes)


if __name__ == '__main__':
    app.run(debug=True)
