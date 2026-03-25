# grades.py
def calculate_average(scores):
    """Return the average of a list of scores."""
    return sum(scores) / len(scores)

def sayHi():
    print('Steve says Hi')
 
if __name__ == '__main__':
    scores = [88, 92, 75, 100, 63]
    print(f"Average: {calculate_average(scores)}")

def high_low(scores):
    """Return the highest and lowest scores."""
    return max(scores), min(scores)
def letter_grade(score):
 """Convert a numeric score to a letter grade."""
 if score >= 90:
    return "A"
 elif score >= 80:
    return "B"
 elif score >= 70:
    return "C"
 elif score >= 60:
    return "D"
 else:
    return "F"
def sayHi():
    print('Steve says hi!')
