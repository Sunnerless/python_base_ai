import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# plt.style.use('ggplot')
# fig, ax = plt.subplots()
# # ax.plot(squares)  # 根据 squares 的索引作为横坐标（x 轴），squares 中的值作为纵坐标（y 轴）来绘制一条线
# # plt.show()
#
#
# # 修改标签文字和线条粗细
# ax.plot(input_values, squares, linewidth=3, color='blue')

# plt.show()

# 使用scatter()绘制散点图
# plt.style.use('ggplot')
# fig,ax = plt.subplots()
# ax.scatter(input_values, squares, s=100)  # s越大散点越大
# ax.set_title('Square Numbers', fontsize=24)
# ax.set_xlabel('Value', fontsize=14)
# ax.set_ylabel('Square of Value', fontsize=14)
#
# ax.tick_params(labelsize=14)  # 刻度标记的字号设置为14
#
#
# plt.show()

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)  # s越大散点越大
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('x_values', fontsize=14)
ax.set_ylabel('y_values', fontsize=14)
ax.axis([0, 1100, 0, 1100000])
ax.ticklabel_format(style='plain')


# 保存图片
plt.savefig('demo_1.png', bbox_inches='tight')  # 要保存这里要把plt.show()删除
