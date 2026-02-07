memory = {
    90: "A",
    75: "B",
    60: "C"
}
new_marks = 55
closest_marks = None
minimum_distance = float('inf')
for marks in memory:
    distance = abs(new_marks - marks)
    if distance < minimum_distance:
        minimum_distance = distance
        closest_marks = marks
predicted_grade = memory[closest_marks]
print("Memory-Based Learning Example")
print("-------------------------------")
print("Stored Data:", memory)
print("New Marks:", new_marks)
print("Closest Stored Marks:", closest_marks)
print("Predicted Grade:", predicted_grade)