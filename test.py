data = [
    ([1, 1, 0], 1),
    ([1, 0, 0], 1),
    ([0, 1, 0], 1),

    ([0, 0, 1], 0),
    ([0, 0, 0], 0),

    ([1, 0, 1], 0),
    ([0, 1, 1], 0),
    ([1, 1, 1], 0),
    ([0, 1, 0], 0),
]

weights = [0.0, 0.0, 0.0]
bias = 0.0
learning_rate = 0.1
epochs = 15

# -------- TRAINING ----------
for epoch in range(epochs):
    for inputs, target in data:
        # weighted sum + bias (bias only once)
        output = 0.0
        for i in range(3):
            output += weights[i] * inputs[i]
        output += bias

        prediction = 1 if output >= 0 else 0
        error = target - prediction

        # update weights
        for i in range(3):
            weights[i] += learning_rate * error * inputs[i]

        # update bias
        bias += learning_rate * error

print("Final Weights:", weights)
print("Final Bias:", bias)

# -------- PREDICTIONS + METRICS ----------
TP = FP = TN = FN = 0
print("\nTraining Data Predictions:\n")

for inputs, target in data:
    output = 0.0
    for i in range(3):
        output += weights[i] * inputs[i]
    output += bias

    prediction = 1 if output >= 0 else 0
    print(f"Input: {inputs}  Target: {target}  Pred: {prediction}")

    # confusion matrix update
    if prediction == 1 and target == 1:
        TP += 1
    elif prediction == 1 and target == 0:
        FP += 1
    elif prediction == 0 and target == 0:
        TN += 1
    elif prediction == 0 and target == 1:
        FN += 1

print("\nConfusion Matrix:")
print("TP =", TP, "FP =", FP)
print("TN =", TN, "FN =", FN)

total = TP + TN + FP + FN

accuracy = (TP + TN) / total if total != 0 else 0
precision = TP / (TP + FP) if (TP + FP) != 0 else 0
recall = TP / (TP + FN) if (TP + FN) != 0 else 0
f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

print("\nMetrics:")
print("Accuracy =", accuracy)
print("Precision =", precision)
print("Recall =", recall)
print("F1 Score =", f1)  