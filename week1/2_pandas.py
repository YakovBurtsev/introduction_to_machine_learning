import pandas as pd

df = pd.read_csv('titanic.csv', index_col='PassengerId')  # DataFrame

with open('answers/1.txt', 'w') as wf:
    sex_value_counts = df['Sex'].value_counts()  # Series
    wf.write(str(sex_value_counts['male']))
    wf.write(' ')
    wf.write(str(sex_value_counts['female']))

with open('answers/2.txt', 'w') as wf:
    survived_value_counts = df['Survived'].value_counts()
    survived_counts = survived_value_counts[1]
    total_count = survived_value_counts[0] + survived_counts
    survived_percentage = round(survived_counts / total_count * 100, 2)
    wf.write(str(survived_percentage))

with open('answers/3.txt', 'w') as wf:
    class_value_counts = df['Pclass'].value_counts()
    first_class_count = class_value_counts[1]
    first_class_percentage = round(first_class_count / total_count * 100, 2)
    wf.write(str(first_class_percentage))

with open('answers/4.txt', 'w') as wf:
    wf.write(str(df['Age'].mean()))
    wf.write(' ')
    wf.write(str(df['Age'].median()))

with open('answers/5.txt', 'w') as wf:
    corr = df['SibSp'].corr(df['Parch'])
    wf.write(str(round(corr, 2)))

