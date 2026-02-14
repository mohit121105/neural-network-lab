learning_rate = 0.1
weight= 0.0
data = [
    (1,1),
    (1,0),
    (0,1),
    (1,1),
    (0,0)
]
print("hebbian Learning : Study -> Good Marks")
print("---------------------------------------------------")
print("Day| Studied | Good Marks| Weight")
print("---------------------------------------------------")

for day, (studied, good_marks) in enumerate(data, start =1):
    delta_w = learning_rate * studied * good_marks
    weight += delta_w
    print(f"{day:^3} | {studied: ^7} | {good_marks:^10} | {weight:.2f}")
print("---------------------------------------------------")
print(f"Final Learned Weight: {weight:.2f}")
print("---------------------------------------------------")
print("\nTesting New Input")
test_input = int(input("Did the student study? (1 = Yes, 0 = No): "))
predicted_output = weight * test_input
print(f"\nPredicted Good Marks Value = {weight:.2f} * {test_input} = {predicted_output:.2f}" )
if predicted_output > 0:
    print("Prediction: Higher chance of getting good marks.")
else:
    print("Prediction: Low chance of getting good marks.")