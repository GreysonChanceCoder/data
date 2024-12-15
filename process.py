import pandas as pd


data=pd.read_csv("data.csv",encoding='utf-8')
print(data.head())

data['comment_time'] = pd.to_datetime(data['comment_time'])
print(len(data))

before_may_10 = data[data['comment_time'] < '2024-05-10']
after_may_10 = data[data['comment_time'] >= '2024-05-10']
print(len(before_may_10))
print(len(after_may_10))

print("Data before May 10th:")
print(before_may_10)

print("\nData after May 10th:")
print(after_may_10)

comments = before_may_10['comment'].astype(str)
with open('period1.txt', 'w', encoding='utf-8') as file:
    for comment in comments:
        file.write(comment + '\n')
citys = before_may_10['site'].astype(str)
with open('period1_city.txt', 'w', encoding='utf-8') as file:
    for city in citys:
        file.write(city + '\n')


comments = after_may_10['comment'].astype(str)
with open('period2.txt', 'w', encoding='utf-8') as file:
    for comment in comments:
        file.write(comment + '\n')
citys = after_may_10['site'].astype(str)
with open('period2_city.txt', 'w', encoding='utf-8') as file:
    for city in citys:
        file.write(city + '\n')