from random import randint
import plotly.express as px

class Die:
    """表⽰⼀个骰⼦的类"""
    def __init__(self, num_sides=6):
        """骰⼦默认为6 ⾯的"""
        self.num_sides = num_sides

    def roll(self):
        """"返回⼀个介于1 和骰⼦⾯数之间的随机值"""
        return randint(1, self.num_sides)


# die = Die()
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
# #  分析结果
# frequencies = []
# poss_results = range(1, die.num_sides + 1)
# for i in poss_results:
#     frequency = results.count(i)
#     frequencies.append(frequency)
#
# print(frequencies)
# # 绘制直方图
# title = "Results of Rolling One D6 1,000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
#
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)  # scatter()散点图, line()折线图, bar()直方图
# fig.show()

# 整两个骰子
die_1 = Die()
die_2 = Die()
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for i in poss_results:
    frequency = results.count(i)
    frequencies.append(frequency)
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)  # scatter()散点图, line()折线图, bar()直方图
# 进⼀步定制图形
fig.update_layout(xaxis_dtick=1)
fig.write_html('dice_visual_d6d10.html')