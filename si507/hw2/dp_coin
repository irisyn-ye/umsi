# [8] method 3 dp
def change(amount, coins):
  dp = [float('inf') for inf in range(amount+1)]
  dp[0] = 0

  for i in range(len(dp)):
    for c in coins:
      if i-c >= 0:
        dp[i] = min(dp[i], dp[i-c]+1)
  return dp[-1] if dp[-1] == float('inf') else dp[-1]
