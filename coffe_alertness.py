learning_rate = 0.15   ##coffee, alertness
weight = 0.0            #1 = yes, 0 = no
daily_experiences = [
    (1,1),
    (1,0),
    (0,1),
    (1,1),
    (0,0)
] 
print("Hebbian Learning : Coffee -> Alertness")
print("---------------------------------------------------")
print("Day | Coffee | Alert | Weight")
print("---------------------------------------------------")

for day, (coffee, alert) in enumerate(daily_experiences, start=1):
    delta_w = learning_rate * coffee * alert
    weight += delta_w
    print(f"{day:^3} | {coffee:^6} | {alert:^5} | {weight:.2f}")

print("---------------------------------------------------")
print(f"Final Learned Weight: {weight:.2f}")
print("---------------------------------------------------")

print("\nTesting New Input")
test_input = int(input("Did the person drink coffee? (1 = Yes, 0 = No): "))

predicted_output = weight * test_input

print(f"\nPredicted Alertness Value = {weight:.2f} * {test_input} = {predicted_output:.2f}")

if predicted_output > 0:
    print("Prediction: Higher chance of being alert.")
else:
    print("Prediction: Low chance of being alert.")