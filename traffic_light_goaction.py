learning_rate = 0.1
weight = 0.0
trials = [        #5 trials of experiences (green light, pressed the accelerator)
    (1,1),        # 1 = yes, 0 = no
    (1,0),
    (0,1),
    (1,1),
    (0,0)
]
print("Hebbian Learning : Green Light -> Press Accelerator")
print("---------------------------------------------------")
print("Trial | Green Light | Pressed Accelerator | Weight")
print("---------------------------------------------------")

for trial_num, (green_light, accelerator) in enumerate(trials, start=1):
    delta_w = learning_rate * green_light * accelerator
    weight += delta_w
    print(f"{trial_num:^5} | {green_light:^11} | {accelerator:^19} | {weight:.2f}")

print("---------------------------------------------------")
print(f"Final Learned Weight: {weight:.2f}")
print("---------------------------------------------------")

print("\nTesting New Input")
test_input = int(input("Green light? (1 = Yes, 0 = No): "))

predicted_output = weight * test_input

print(f"\nPredicted Response Value = {weight:.2f} * {test_input} = {predicted_output:.2f}")

if predicted_output > 0:
    print("Prediction: Likely to press accelerator.")
else:
    print("Prediction: Unlikely to press accelerator.")