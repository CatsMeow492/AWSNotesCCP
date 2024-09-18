import json
import matplotlib.pyplot as plt

## load tally.json
with open('questionShuffler/tally.json', 'r') as file:
    data = json.load(file)

questions = list(data.keys())
correct = [data[q]['correct'] for q in questions]
incorrect = [data[q]['incorrect'] for q in questions]
total_correct = sum(correct)
total_incorrect = sum(incorrect)
total_attempts = total_correct + total_incorrect

## Create a bar chart
x = range(len(questions))
plt.figure(figsize=(20, 10))
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot = bar chart
plt.bar(x, correct, width=0.4, label='Correct', color='b', align='center')
plt.bar(x, incorrect, width=0.4, label='Incorrect', color='r', bottom=correct, align='center')
plt.xlabel('Questions')
plt.ylabel('Counts')
plt.xticks(x, questions, rotation=90)
plt.legend()

# Calculating totals for pie chart
total_correct = sum(correct)
total_incorrect = sum(incorrect)
totals = [total_correct, total_incorrect]
labels = ['Correct', 'Incorrect']
colors = ['blue', 'red']

# Create a pie chart
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot = pie chart
plt.pie(totals, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.text(-1.2, -1.0, 'Total correct: ' + str(total_correct), fontsize=12)
plt.text(-1.2, -1.05, 'Total incorrect: ' + str(total_incorrect), fontsize=12)
plt.text(-1.2, -1.1, 'Total attempts: ' + str(total_attempts), fontsize=12)

# Count the number of unique questions attempted
unique_questions_attempted = sum(1 for q in questions if data[q]['correct'] > 0 or data[q]['incorrect'] > 0)

# Add the statistic to the pie chart
plt.text(-1.2, -1.15, 'Unique questions attempted: ' + str(unique_questions_attempted), fontsize=12)


plt.tight_layout()
plt.show()
