# grades.py
def calculate_average(scores):
    """Return the average of a list of scores."""
    return sum(scores) / len(scores)

def sayHi():
    print('Steve says Hi')
 
if __name__ == '__main__':
    scores = [88, 92, 75, 100, 63]
    print(f"Average: {calculate_average(scores)}")

