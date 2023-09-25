def distribute_mangoes(bags, students):
    # Sort the bags in ascending order
    bags.sort()

    # Initialize variables to keep track of minimum difference and bag assignments
    min_difference = float('inf')
    max_difference = float('inf')
    assignments = [[] for _ in range(students)]

    # Distribute bags to students in a round-robin fashion
    for i in range(len(bags)):
        student_index = i % students
        assignments[student_index].append(bags[i])

    # Calculate the difference between the bag with max and min mangoes for each student
    for assignment in assignments:
        max_mangoes = max(assignment)
        min_mangoes = min(assignment)
        difference = max_mangoes - min_mangoes
        min_difference = min(min_difference, difference)
        max_difference = max(min_difference, difference)

    return min_difference, max_difference, assignments

# Example usage:
bags = [5, 9, 2, 15, 7, 3, 5, 7, 8, 10]
students = 5
min_diff, max_diff, assignments = distribute_mangoes(bags, students)
print("Minimum Difference:", min_diff)
print("Maximum Difference:", max_diff)

print(assignments)
