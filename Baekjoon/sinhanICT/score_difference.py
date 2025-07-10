estimate_info = [
    [1, 1, 100],
    [2, 3, 30],
    [3, 2, 100],
    [4, 5, 450],
    [5, 4, 2000]
]

real_scores = {
    1: 350,
    2: 30,
    3: 20,
    4: 100,
    5: 1500
}

k = 3

def score_difference(k, estimate_info, real_scores):
  sorted_by_priority = sorted(estimate_info, key=lambda x: x[1])
  top_k_priority = sorted_by_priority[:k]

  # 방법 1 - 우선순위 기준
  est_sum1 = 0
  real_sum1 = 0
  for x in top_k_priority:
    est_sum1 += x[2]
    real_sum1 += real_scores[x[0]]
  
  answer1 = abs(est_sum1 - real_sum1)

  # 방법 2 - 예상점수 기준, 점수 같으면 우선순위 높은 순
  est_sum2 = 0
  real_sum2 = 0
  sorted_by_estimate = sorted(estimate_info, key=lambda x: (-x[2], x[1]))
  top_k_estimate = sorted_by_estimate[:k]

  for x in top_k_estimate:
    est_sum2 += x[2]
    real_sum2 += real_scores[x[0]]

  answer2 = abs(est_sum2 - real_sum2)

  return [answer1, answer2]

print(score_difference(k, estimate_info, real_scores))



