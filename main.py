import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = input("Введите пороговое значение колебания цены акции в периоде (например, '0.05' ): ")
    export = input("Экспортировать данные в CSV формате? (Y/N):» ")
    elder_rays = input("Выводить инструмент ЛУЧИ ЭЛДЕРА? (Y/N):» ")


    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)
    # column_names = stock_data.columns.tolist()
    # print(column_names)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    average_price_period = dd.calculate_and_display_average_price(stock_data)
    print(f'Cредняя цена закрытия акций {ticker} за заданный период {period}: {average_price_period}')

    dd.notify_if_strong_fluctuations(stock_data, threshold)

    if export == "Y":
        file_name = input("Введите название выходного файла (по умолчанию - 'out_file_csv'):» ")
        if file_name == "":
            file_name = 'out_file_csv.csv'

        dd.export_data_to_csv(stock_data, file_name)


    if elder_rays == 'Y':
        period_EMA = input("Введите период EMA (по умолчанию - 13):» ")
        if period_EMA == "":
            period_EMA = 13
        else:
            period_EMA = int(period_EMA)

        dd.Elders_rays(stock_data, period_EMA)
        dplt.create_and_save_plot_rays(stock_data, ticker, period, period_EMA)

if __name__ == "__main__":
    main()
