# Stock_data_analysis_and_visualization
Общий обзор

Этот проект предназначен для загрузки исторических данных об акциях и их визуализации. Он использует библиотеку yfinance для получения данных и matplotlib для создания графиков. Пользователи могут выбирать различные тикеры и временные периоды для анализа, а также просматривать движение цен и скользящие средние на графике.



Структура и модули проекта

1. data_download.py:

Отвечает за загрузку данных об акциях и обработку загруженных данных с учетом пожеланий пользователя.

Содержит функции, предназначенные:
- для извлечения данных об акциях из интернета;
- для расчёта скользящего среднего;
- для анализа данных и уведомления пользователя, если цена акций колебалась более чем на заданный пользователем процент за период;
- 



2. main.py:

- Является точкой входа в программу.

- Запрашивает у пользователя:
  - тикер акции и временной период,
  - пороговое значение колебания цены акции в периоде, 
  - необходимость выгрузки загруженные данные об акциях в CSV файл.
  - в случае подтверждения запрашивает название файла  CSV. По умолчанию присваивается имя 'out_file_csv.csv' и создает файл в текущем директории.
  - загружает данные, обрабатывает их и выводит результаты в виде графика.



3. data_plotting.py:

Отвечает за визуализацию данных.

- Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.
 ![Семейство графиков](https://github.com/MikhinGB/Stock_data_analysis_and_visualization/blob/main/AAPL_1y_stock_price_chart.png) 
 
  
   - предоставляет пользователю возможность выбирать стиль графиков из предложенного списка.
