# 要在⽂本⽂件中存储数据，最简单的⽅式是将数据组织为⼀系列以逗号分隔的值（comma-separated values， CSV）并写⼊⽂件。这样的⽂件称为CSV ⽂件
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.express as px

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
# print(lines)
reader = csv.reader(lines)

header_row = next(reader)

print(header_row)
for index, column_header in enumerate(header_row):  # 获取索引和值
    print(index, column_header)

# 提取最高温度和日期
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

print(highs)

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

ax.set_title('High Temperature', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature(F)', fontsize=16)
ax.tick_params(labelsize=16)
plt.show()

