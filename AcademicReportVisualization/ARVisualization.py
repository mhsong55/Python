import matplotlib.pyplot as plt
import numpy as np

# 난이도 별 정오 nest pie graph
plt.rc('font', family='NanumGothic')
fig1=plt.figure(1)
ax1 = plt.subplot()

size = 0.3
#                 정  오
vals = np.array([[9, 3],
                 [2, 2],
                 [1, 3]])
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

ax1.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
        wedgeprops=dict(width=size, edgecolor='w'))
ax1.pie(vals.flatten(), radius=1-size, colors=inner_colors,
        wedgeprops=dict(width=size, edgecolor='w'))
ax1.set(aspect="equal")

plt.show()

# 단원 별 bar graph
fig2 = plt.figure(2)
ax2 = plt.subplot()

data = {'1. 100까지의 수': 100,
        '2. 덧셈과 뺄셈 (1)': 0,
        '3. 여러가지 모양': 66,
        '4. 덧셈과 뺄셈 (2)': 100,
        '5. 시계 보기와 규칙 찾기': 33,
        '6. 덧셈과 뺄셈 (3)': 33}
unit = list(data.keys())
y_pos = np.arange(len(unit))
x_ticks = list(np.linspace(0, 100, 11))
grade = list(data.values())
colors = ['purple','gray', 'orange', 'red', 'blue', 'green']
ax2.barh(y_pos, grade, align='center', color=colors, edgecolor='white', alpha=.7)
ax2.set_yticks(y_pos)
ax2.set_yticklabels(unit)
ax2.invert_yaxis() # labels read top-to-bottom
ax2.set_xlim([0, 100])

ax2.set_xticks(x_ticks)
ax2.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=1)

plt.show()
