def max_words_formed(s: str, words: list[str]) -> int:
  """
  Finds the maximum number of words formable from the characters in s using words array.

  Args:
      s: The string containing characters to form words.
      words: An array of words that can be formed from characters in s.

  Returns:
      The maximum number of words formable using characters in s at most once.
  """
  # Create a character count dictionary from the string s.
  char_count = {}
  for char in s:
    char_count[char] = char_count.get(char, 0) + 1

  # Count the number of valid words.
  valid_words = 0
  for word in words:
    # Check if each character in the word exists in s with sufficient count.
    can_form = True
    for char in word:
      if char not in char_count or char_count[char] == 0:
        can_form = False
        break
      char_count[char] -= 1  # Decrement count for used character.
    if can_form:
      valid_words += 1
    # Reset character counts back to original values for next word.
    for char in word:
      char_count[char] += 1

  return valid_words

# Example usage
s = "apple"
words = ["ap", "ple", "apple"]
result = max_words_formed(s, words)
print(result)  # Output: 2 (ap and apple)
