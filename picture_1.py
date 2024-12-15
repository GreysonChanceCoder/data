import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter


data=pd.read_csv("picture_data.csv")
print(data)

topic_proportion=[]
for i in range(len(data)):
    topic_proportion.append(data.loc[i,'num']/sum(data['num']))

data['topic_proportion']=topic_proportion
data=data.sort_values('topic_proportion').reset_index()
print(data)


# 准备数据和标签
categories = data['topic'].astype(str)
values = data['topic_proportion']
labels = data['topic'].astype(str)

theme_words=[
"Changes in Sleep Patterns",
"Emotional Reactions and Physiological Effects",
"Insomnia and Emotional Management",
"Physical Symptoms and Sleep Quality",
"Emotional Fluctuations and Behavioral Responses",
"Memory Disorders and Cognitive Interference",
"Psychological Effects and Sleep Disorders",
"Emotional Fluctuations and Behavioral Abnormalities",
"Popular Science Knowledge and Misunderstandings",
"Comprehensive Symptom Responses"
]

#第二阶段
"""
theme_words=[
"Impact on Sleep and Self-Perception",
"Perceived Effects and Emotional Reactions",
"Prevalence of Insomnia and Self-Identification",
"Direct Impact of Geomagnetic Storms",
"Exploration of Causes and Actual Effects",
"Emotional Regulation and Physiological Changes",
"Sleep Difficulties and Individual Responses",
"Emotional Fluctuations and Self-Perception",
"Identification of Causes and Physiological Effects",
"Behavioral Responses and Emotional Regulation"
]
"""

fig, ax = plt.subplots()
# 设置条形的宽度
bar_width = 0.05

# 绘制水平条形图并设置宽度
plt.barh(categories, values, color='black',height=bar_width)

# 在每个条形后添加标签
for i in range(len(categories)):
    plt.text(values[i]+0.005, categories[i], 'Topic'+labels[i]+'  '+theme_words[i])

# 隐藏纵坐标轴
plt.gca().axes.get_yaxis().set_visible(False)

# 设置横坐标为百分数
def to_percent(temp, position):
    return '%1.0f%%' % (100 * temp)
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

# 添加标签
plt.xlabel('Values')
plt.title('Period 1')

#去除边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# 显示图形
plt.show()