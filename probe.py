import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('nornikel.xlsx')

period = 13
p_EMA = str(period) + '-EMA'

df[p_EMA] = df['close'].ewm(span=period, adjust=False).mean()
df['bull_power'] = df['max'] - df[p_EMA]
df['bear_power'] = df['min'] - df[p_EMA]

# print(df)

# Настройка размеров подложки
plt.figure(figsize=(17, 10))

# Вывод графиков

plt.subplot(3, 1, 1)
plt.plot(df['date'], df[p_EMA], label=p_EMA)
plt.title(f"{p_EMA} тенденция")
plt.subplot(3, 1, 2)
plt.bar(df['date'], df['bull_power'], label='bull_power')
plt.title("Сила быков")
plt.subplot(3, 1, 3)
plt.bar(df['date'], df['bear_power'], label='bear_power')
plt.title("Сила медведей")

# plt.title(f"{ticker} Цена акций с течением времени")
# plt.xlabel("Дата")
# plt.ylabel("Цена")
# plt.legend()
#
# if filename is None:
#     filename = f"{ticker}_{period}_stock_price_chart.png"

plt.savefig('elders_rays1.png')

