import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, display_period, style_number, filename=None):
    style_sheets = ['Solarize_Light2', 'dark_background']
    plt.style.use(style_sheets[style_number])
    plt.figure(figsize=(17, 10))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.subplot(3, 1, 1)
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.title(f"{ticker} Цена акций с течением времени")
            plt.ylabel("Цена")
            plt.legend()
            plt.subplot(3, 1, 2)
            plt.plot(dates, data['MACD'].values, '-', color='green', label='MACD')
            plt.plot(dates, data['SIGNAL'].values, '--', color='red', label='SIGNAL')
            plt.ylabel("MACD и Сигнал")
            plt.legend()
            plt.subplot(3, 1, 3)
            plt.bar(dates, data['MACD-hist'].values, color='grey', label='MACD-hist')
            plt.xlabel("Дата")
            plt.ylabel("MACD-гистограмма")
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.subplot(3, 1, 1)
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.title(f"{ticker} Цена акций с течением времени")
        plt.ylabel("Цена")
        plt.legend()
        plt.subplot(3, 1, 2)
        plt.plot(data['Date'], data['MACD'].values, '-', color='green', label='MACD')
        plt.plot(data['Date'], data['SIGNAL'].values, '--', color='red', label='SIGNAL')
        plt.ylabel("MACD и Сигнал")
        plt.legend()
        plt.subplot(3, 1, 3)
        plt.bar(data['Date'], data['MACD-hist'].values, color='grey', label='MACD-hist')
        plt.xlabel("Дата")
        plt.ylabel("MACD-гистограмма")

    if filename is None:
        filename = f"{ticker}_{display_period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")

def create_and_save_plot_rays(data, ticker, display_period, period_EMA, filename=None):
    plt.figure(figsize=(17, 10))
    p_EMA = str(period_EMA) + '-EMA'

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.subplot(3, 1, 1)
            plt.plot(dates, data[p_EMA], label=p_EMA)
            plt.title(f"{p_EMA} тенденция")
            plt.subplot(3, 1, 2)
            plt.bar(dates, data['Bull_power'], label='Bull_power')
            plt.title("Сила быков")
            plt.subplot(3, 1, 3)
            plt.bar(dates, data['Bear_power'], label='Bear_power')
            plt.title("Сила медведей")

        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.subplot(3, 1, 1)
        plt.plot(data['Date'], data[p_EMA], label=p_EMA)
        plt.title(f"{p_EMA} тенденция")
        plt.subplot(3, 1, 2)
        plt.bar(data['Date'], data['Bull_power'], label='Bull_power')
        plt.title("Сила быков")
        plt.subplot(3, 1, 3)
        plt.bar(data['Date'], data['Bear_power'], label='Bear_power')
        plt.title("Сила медведей")

    if filename is None:
        filename = f"{ticker}_{display_period}_elders_rays.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
