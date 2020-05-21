from flask import Flask, render_template
from data import title, subtitle, description, departures, tours

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('index.html',
                           title_step=title,
                           departures=departures,
                           description=description,
                           subtitle=subtitle,
                           tours=tours)


@app.route('/departure/<departure>')
def show_daparture(departure):
    from_town = departures.get(departure)
    # this will be a dict with tours for this departure
    tours_dict = dict()
    for key, value in tours.items():
        if value.get('departure') == departure:
            tours_dict[key] = value
    # count of tours for this departure
    counter = len(tours_dict)
    # correct typo for 'тур/ов/а'
    if counter == 1:
        counter_line = 'Найден 1 тур'
    elif counter == 11:
        counter_line = f'Найдено {counter} туров'
    elif 4 >= counter % 10 >= 1:
        counter_line = f'Найдено {counter} тура'
    else:
        counter_line = f'Найдено {counter} туров'
    return render_template('departure.html',
                           departure=departure,
                           departures=departures,
                           from_town=from_town,
                           title='Туры ' + from_town,
                           tours=tours_dict,
                           counter_line=counter_line)


@app.route('/tour/<int:id_tour>')
def show_tour(id_tour):
    tour = tours.get(id_tour)
    tour_departure = tour.get("departure")
    from_town = departures.get(tour_departure)
    # correct typo for 'ночь/и/ей'
    nights = tour.get('nights')
    if nights == 1:
        nights_line = '1 ночь'
    elif nights == 11:
        nights_line = f'{nights} ночей'
    elif 4 >= nights % 10 >= 1:
        nights_line = f'{nights} ночи'
    else:
        nights_line = f'{nights} ночей'
    return render_template('tour.html',
                           title=tour.get('title'),
                           tour=tour,
                           from_town=from_town,
                           nights=nights_line,
                           departures=departures)


@app.route('/about/')
def render_about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
