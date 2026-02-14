learning_rate = 0.15
weight = 0.0

experiences = [
    (1,1),
    (1,0),
    (0,1),
    (1,1),
    (0,0),
    (1,1)
]
print("Hebbian Learning : Song -> Happiness")
print("---------------------------------------------------")
print("Day | Song | Happiness | Weight")
print("---------------------------------------------------")

for day, (song, happiness) in enumerate(experiences, start=1):
    delta_w = learning_rate * song * happiness
    weight += delta_w
    print(f"{day:^3} | {song:^6} | {happiness:^9} | {weight:.2f}")

print("---------------------------------------------------")
print(f"Final Learned Weight: {weight:.2f}")
print("---------------------------------------------------")

print("\nTesting New Input")
test_input = int(input("Did the person listen to the song? (1 = Yes, 0 = No): "))

predicted_output = weight * test_input

print(f"\nPredicted Happiness Value = {weight:.2f} * {test_input} = {predicted_output:.2f}")

if predicted_output > 0:
    print("Prediction: Higher chance of feeling happy.")
else:
    print("Prediction: Low chance of feeling happy.")