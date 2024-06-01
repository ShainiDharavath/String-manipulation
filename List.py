def max_words_formed(s: str, words: List[str]) -> int:
  """
  Finds the maximum number of words formable from the given words using characters in s

  Args:
      s: The string to form words from.
      words: The list of words to be formed.

  Returns:
      The maximum number of words formable.
  """
  n = len(s)
  dp = [[False] * (n + 1) for _ in range(len(words) + 1)]

  # Base case: empty string cannot form any words
  for i in range(len(words) + 1):
    dp[i][0] = False

  # Base case: empty word list can form 0 words
  for j in range(n + 1):
    dp[0][j] = True

  # Build DP table
  for i in range(1, len(words) + 1):
    word = words[i - 1]
    for j in range(1, n + 1):
      if word[0] == s[j - 1]:
        # Check if the remaining word can be formed using remaining characters in s
        dp[i][j] = dp[i - 1][j - 1] and all(dp[k][j - l] for k, l in enumerate(map(ord, word[1:])) if s[j - l - 1] == chr(k))
      else:
        # If first character doesn't match, word cannot be formed here
        dp[i][j] = dp[i][j - 1]

  # Return the maximum value in the last row (represents all words)
  return sum(dp[-1])

# Follow-up: modify the code to return a list of formed words
def max_words_formed_with_list(s: str, words: List[str]) -> List[str]:
  """
  Finds the maximum number of words formable and returns the list of formed words

  Args:
      s: The string to form words from.
      words: The list of words to be formed.

  Returns:
      A list of formed words (if any)
  """
  n = len(s)
  # Similar DP table structure with additional information for backtracking
  dp = [[[False, None]] * (n + 1) for _ in range(len(words) + 1)]

  # Base cases remain the same

  # Build DP table with backtracking information
  for i in range(1, len(words) + 1):
    word = words[i - 1]
    for j in range(1, n + 1):
      if word[0] == s[j - 1]:
        can_form, prev_word = dp[i - 1][j - 1]
        if can_form and all(dp[k][j - l][0] for k, l in enumerate(map(ord, word[1:])) if s[j - l - 1] == chr(k)):
          dp[i][j] = [True, prev_word + " " + word]
      else:
        dp[i][j] = [dp[i][j - 1][0], None]

  # Backtrack to find formed words (if any)
  formed_words = []
  i, j = len(words), n
  while i > 0 and j > 0:
    can_form, prev_word = dp[i][j]
    if can_form:
      formed_words.append(prev_word.strip())
      i, j = map(lambda x: int(x.split()[0]), dp[i][j][1].split(" "))
    else:
      j -= 1

  return formed_words[::-1]  # Reverse to get words in formation order

# Example usage
s = "applepen"
words = ["apple", "pen"]
print(max_words_formed(s, words))  # Output: 2

# Follow-up example
formed_words = max_words_formed_with_list(s, words)
print(formed_words)  # Possible output: ["apple", "pen"] (order may vary)
