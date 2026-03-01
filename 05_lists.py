# 05_lists.py
# lists and score_tracker

score_tracker = []

for i in range(5):
    score = float(input("Enter your score: "))
    score_tracker.append(score)

average = sum(score_tracker) / len(score_tracker)

print("Highest score: ", max(score_tracker))
print("Lowest score: ", min(score_tracker))
print("Average: ", round(average, 2))
