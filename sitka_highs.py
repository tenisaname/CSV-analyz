import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = "data/1.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Чтение дат и максимальных температур из файла
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        try:
            high = int(row[2])
            low = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # Нанесение данных на диаграмму
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red", alpha=0.5)
    ax.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)



    # Форматирование диаграммы
    title = "Температура за выбранный период"
    plt.title(title, fontsize = 20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both',which='major', labelsize=16)

    plt.show()