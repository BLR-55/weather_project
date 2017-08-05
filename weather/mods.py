
def degree(deg_val):

    val = float(deg_val)

    if val >= 11.25 and val <= 33.75:
        deg_name = 'Северо-Северо-Восток'
    elif val > 33.75 and val < 56.25:
        deg_name = 'Северо-Восток'
    elif val >= 56.25 and val <= 78.75:
        deg_name = 'Восток-Северо-Восток'
    elif val > 78.75 and val < 101.25:
        deg_name = 'Восток'
    elif val >= 101.25 and val <= 123.75:
        deg_name = 'Восток-Юго-Восток'
    elif val > 123.75 and val < 146.25:
        deg_name = 'Юго-Восток'
    elif val >= 146.25 and val < 168.75:
        deg_name = 'Юго-Юго-Восток'
    elif val >= 168.75 and val <= 191.25:
        deg_name = 'ЮГ'
    elif val > 191.25 and val < 213.75:
        deg_name = 'Юго-Юго-Запад'
    elif val >= 213.75 and val <= 236.25:
        deg_name = 'Юго-Запад'
    elif val > 236.25 and val < 258.75:
        deg_name = 'Запад-Юго-Запад'
    elif val >= 258.75 and val <= 281.25:
        deg_name = 'Запад'
    elif val > 281.25 and val < 303.75:
        deg_name = 'Запад-Северо-Запад'
    elif val >= 303.75 and val <= 326.25:
        deg_name = 'Северо-Запад'
    elif val > 326.25 and val < 348.75:
        deg_name = 'Северо-Северо-Запад'
    else:
        deg_name = 'Север'

    return deg_name

def weather_status(status):

    val = str(status).lower()
    print(status)
    print(val)

    if val == 'rain':
        val_name = 'Дождь'
    elif val == 'clouds':
        val_name = 'Облачно'
    elif val == 'clear':
        val_name = 'Ясно'
    elif val == 'few clouds':
        val_name = 'Малооблачно'
    elif val == 'broken clouds':
        val_name = 'Рваное небо'
    elif val == 'shower rain':
        val_name = 'Ливень'
    elif val == 'thunderstorm':
        val_name = 'Гроза'
    elif val == 'show':
        val_name = 'Снег'
    elif val == 'mist':
        val_name = 'Легкий туман'
    elif val == 'scattered clouds':
        val_name = 'Рассеянные облака'
    elif val == 'haze':
        val_name = 'Туман'
    else:
        val_name = val
    return val_name





