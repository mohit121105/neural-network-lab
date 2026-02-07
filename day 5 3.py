target_volume = 250.0
hand_tilt = 10.0
learning_rate = 0.3
input_tilt = 1.0
num_pours = 30
tolerance = 0.1
print("Pour | Volume   | Error  | ΔTilt   | Hand Tilt")
print("-" * 45)

for pour in range(1, num_pours + 1):
    
    volume = hand_tilt * 0.8

    error = target_volume - volume
    delta_tilt = learning_rate * error * input_tilt
    hand_tilt += delta_tilt

    if abs(error) <= tolerance:
        volume = target_volume

    print(f"{pour:^4} | {volume:^8.2f} | {error:^6.2f} | {delta_tilt:^7.2f} | {hand_tilt:^9.2f}")

    if abs(error) <= tolerance:
        break