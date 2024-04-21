def count_mismatches(word, s):
    mismatch_count = sum(1 for c in word if c != s)
    return mismatch_count


assert count_mismatches("hello", "l") == 3
assert count_mismatches("world", "o") == 4


word = "hello"
s = "l"
mismatch = count_mismatches(word, s)
print(f"Не співпадінь: {mismatch}")