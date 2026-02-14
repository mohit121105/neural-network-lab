learning_rate = 0.2
weight = 0.0

daily_data = [
    (1,1),
    (0,1),
    (1,0),
    (1,1),
    (0,0),
    (1,1),
    (0,1)
]

print("Hebbian Learning : Exercise -> Energetic")
print("---------------------------------------------------")
print("Day | Exercise | Energetic | Weight")
print("---------------------------------------------------")

for day, (exercise, energetic) in enumerate(daily_data, start=1):
    delta_w = learning_rate * exercise * energetic
    weight += delta_w
    print(f"{day:^3} | {exercise:^8} | {energetic:^9} | {weight:.2f}")

print("---------------------------------------------------")
print(f"Final Learned Weight: {weight:.2f}")
print("---------------------------------------------------")

print("\nTesting New Input")
test_input = int(input("Did the person exercise? (1 = Yes, 0 = No): "))

predicted_output = weight * test_input

print(f"\nPredicted Energy Value = {weight:.2f} * {test_input} = {predicted_output:.2f}")

if predicted_output > 0:
    print("Prediction: Higher chance of feeling energetic.")
else:
    print("Prediction: Low chance of feeling energetic.")
