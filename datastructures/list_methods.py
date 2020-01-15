scores = ["B", "A", "A", "C", "B", "A"]
grades = scores
print(f"scores {scores}")
print(f"grades {grades}")
scores[3] = "E"
print(f"scores {scores}")
print(f"grades {grades}")

grades = scores.copy()
print(f"scores {scores}")
print(f"grades {grades}")
scores[3] = "F"
print(f"scores {scores}")
print(f"grades {grades}")

print(min(scores))
print(max(scores))

print(sorted(grades))

print('\n'.join(grades))
print('--'.join(scores))

grades.append("F")
print(grades)
