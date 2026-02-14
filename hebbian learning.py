learning_rate = 0.1
weight= 0.5
training_data = [
    (1,1),
    (1,1),
    (1,0),
    (0,1),
    (1,1)
]
print("Hebbian Learning")
print("---------------------------")
print("Initial Weight:", weight)
print()
for i, (x,y) in enumerate(training_data, start = 1):
    delta_w = learning_rate * x * y
    weight += delta_w
    print(f"Step {i}")
    print(f"Input (x) = {x}, Output (y) = {y}")
    print(f"∆w = {learning_rate} * {x} * {y} = {delta_w}")
    print(f"Updated Weight = {weight}")
    print("---------------------------")
print("Final Weight after Hebbian Learning:", weight)
print("---------------------------")
test_x = int(input("Enter test input * (0 or 1): "))
test_y = weight * test_x
print(f"Predicted output y = weight * x = {weight} * {test_x} = {test_y}")