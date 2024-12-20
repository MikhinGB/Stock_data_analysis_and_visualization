import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, period='1mo', start=None, end=None):
    """ Эта функция получает исторические данные об акциях для указанного тикера и временного периода.

    Возвращает DataFrame с данными."""

    stock = yf.Ticker(ticker)
    data = stock.history(period=period, start=start, end=end)
    return data


def add_moving_average(data, window_size=5):
    """ Эта функция добавляет в DataFrame колонку Moving_Average со скользящим средним, рассчитанным на основе
    цен закрытия(колонка Close)."""

    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """ Эта функция вычисляет и выводит среднюю цену закрытия акций за заданный период.

    Функция принимает DataFrame и вычисляет среднее значение колонки 'Close'.
    Результат выводится в консоль."""

    average_price = data['Close'].mean()

    # Округляем до нужного знака с помощью встроенной функции int().
    # Такой способ работает безотказно и не требует импорта дополнительных модулей.
    # average_price = int(10000*average_price)/10000    # одна из 10 основных ошибок начинающих Python-разработчиков -
    #  Написание своих велосипедов, вместо использования встроенных
    # функций
    average_price = round(average_price, 4)

    return average_price


def notify_if_strong_fluctuations(data, threshold):
    """ Эта функция анализирует данные и уведомляет пользователя,
        если цена акций колебалась более чем на заданный процент за период.

        Функция вычисляет максимальное и минимальное значения цены закрытия и сравнивает разницу с заданным порогом.
        Если разница превышает порог, пользователь получает уведомление в консоль."""

    threshold = float(threshold)
    average_price_max = data['Close'].max()
    average_price_min = data['Close'].min()
    fluctuation = average_price_max / average_price_min - 1
    if fluctuation > threshold:
        return print(f'Цена акций в периоде колебалась более чем на заданный процент {threshold}')
    else:
        return


def export_data_to_csv(data, filename):
    """ Эта функция при необходимости сохраняет загруженные данные об акциях в CSV файл.

    Функция принимает DataFrame и имя файла, после чего сохраняет данные в указанный файл """

    return data.to_csv(filename, encoding='utf-8')


def Elders_rays(data, period):
    """ Эта функция принимает:
             - period (по умолчанию 13) - Период расчета индикатора;
             - DataFrame.
    Эта функция добавляет в DataFrame колонки:
             -  p_EMA;
             - bull_power;
             - bear_power.
    Эта функция вычисляет:
             - multiplier - множитель, вычисляемый по формуле: multiplier = 2 / (period + 1). Для периода, равного 13
               multiplier равен 0.1429.
             - p-EMA (Exponential Moving Average), где p - значение периода. Вычисляется по формуле:
               p-EMA = {Close - EMA(previous day)} * multiplier  + EMA(previous day). Значение вставляется в
               соответствующую колонку DataFrame (колонку p_EMA);
             - силу "быков". Вычисляется по формуле:
                   Сила быков = Макс (High) - p-EMA
                   Значение вставляется в соответствующую колонку DataFrame (колонку bull_power);
             - силу "медведей". Вычисляется по формуле:
                   Сила медведей = Мин (Low) - p-EMA
                   Значение вставляется в соответствующую колонку DataFrame (колонку bear_power)

    """

    p_EMA = str(period) + '-EMA'  # предполагаем, что период EMA будет выбирать пользователь. Поэтому и вводим эту
    # переменную.

    data[p_EMA] = data['Close'].ewm(span=period, adjust=False).mean()

    data['Bull_power'] = data['High'] - data[p_EMA]
    data['Bear_power'] = data['Low'] - data[p_EMA]

    return data

def macd_and_derivatives(data):
    """ Эта функция принимает:
                 - DataFrame.
        Эта функция добавляет в DataFrame колонки:
                 -  12-EMA;
                 -  26-EMA;
                 - MACD;
                 - SIGNAL;
                 - MACD-hist.
        Эта функция вычисляет:
                 - 12_EMA - 12-дневное EMA по ценам закрытия. Значение вставляется в соответствующую колонку DataFrame
                  (колонку 12-EMA);
                 - 26_EMA - 26-дневное EMA по ценам закрытия. Значение вставляется в соответствующую колонку DataFrame
                  (колонку 26-EMA);
                 - macd - разность между 12_EMA и 26_EMA. Значение вставляется в соответствующую колонку DataFrame
                  (колонку MACD). На графике отображается сплошной линией;
                 - signal - 9-дневное EMA от MACD. Значение вставляется в соответствующую колонку DataFrame
                  (колонку SIGNAL). На графике отображается пунктирной линией.
                 - macd_hist - разность между MACD и signal. Значение вставляется в соответствующую колонку DataFrame
                  (колонку MACD-hist). На графике отображается в виде гистограммы.
        """

    data['12-EMA'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['26-EMA'] = data['Close'].ewm(span=26, adjust=False).mean()

    data['MACD'] = data['12-EMA'] - data['26-EMA']

    data['SIGNAL'] = data['MACD'].ewm(span=9, adjust=False).mean()

    data['MACD-hist'] = data['MACD'] - data['SIGNAL']

    return data
