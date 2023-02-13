scores = 0
for _ in range(10):
    score = int(input())
    pre_scores = scores
    scores += score
    if scores >= 100:
        if abs(100-scores) > abs(100-pre_scores):
            scores = pre_scores
        break
print(scores)