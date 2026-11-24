scores = []

for i in range(5):
    scores.append(int(input(f"Enter quiz {i + 1} score:")))

print("Quiz Scores:" , scores)
print("Number of quizzes:" , len(scores))

total = sum(scores)
print("Total Score:" , total)

average = total / len(scores)
print("Average Score:" , average)

print("Highest Score:" , max(scores))

print("Lowest Score:" , min(scores))

scores.sort()
print("Ascending:" , scores)

scores.reverse()
print("Descending:" , scores)

print("Original Scores:" , scores)
