target_distance = 3.0
throw_strength = 2.0
learning_rate = 0.2
input_strength = 1.0
num_throws = 30
for throw in range(1, num_throws + 1):
    error = target_distance - throw_strength
    delta_w = learning_rate * error * input_strength
    throw_strength += delta_w

   
    distance = throw_strength * 1.5

    if abs(target_distance - distance) < 0.01:
        distance = target_distance

    print(f"{throw:^4} | {distance:^9.2f} | {error:^6.2f} | {delta_w:^8.2f} | {throw_strength:^14.2f}")

    if distance == target_distance:
        break