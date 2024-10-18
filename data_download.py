import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """ Эта функция вычисляет и выводит среднюю цену закрытия акций за заданный период.

    Функция будет принимать DataFrame и вычислять среднее значение колонки 'Close'.
    Результат будет выводиться в консоль."""

    average_price = data['Close'].mean()

    # Округляем до нужного знака с помощью встроенной функции int().
    # Такой способ работает безотказно и не требует импорта дополнительных модулей.
    average_price = int(10000*average_price)/10000

    return average_price


def notify_if_strong_fluctuations(data, threshold):
    """ Эта функция анализирует данные и уведомляет пользователя,
        если цена акций колебалась более чем на заданный процент за период.

        Функция вычисляет максимальное и минимальное значения цены закрытия и сравнивает разницу с заданным порогом.
        Если разница превышает порог, пользователь получает уведомление в консоль."""

    threshold = float(threshold)
    average_price_max = data['Close'].max()
    average_price_min = data['Close'].min()
    fluctuation = average_price_max/average_price_min - 1
    if fluctuation > threshold:
        return print(f'Цена акций в периоде колебалась более чем на заданный процент {threshold}')
    else:
        return


def export_data_to_csv(data, filename):
    """ Эта функция при необходимости сохраняет загруженные данные об акциях в CSV файл.

    Функция принимает DataFrame и имя файла, после чего сохраняет данные в указанный файл """

    return data.to_csv(filename, encoding='utf-8')
