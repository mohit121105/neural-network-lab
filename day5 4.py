target_volume = 80.0
current_volume = 60.0
learning_rate = 0.3
input_knob = 1.0
num_adjustments = 30
tolerance = 0.01
print("Adj | Volume   | Error  | ΔKnob   | Current Knob")
print("-" * 50)

for adj in range(1, num_adjustments + 1):
    
    volume = current_volume

    error = target_volume - volume
    delta_knob = learning_rate * error * input_knob
    current_volume += delta_knob

    if abs(error) <= tolerance:
        volume = target_volume

    print(f"{adj:^3} | {volume:^8.2f} | {error:^6.2f} | {delta_knob:^7.2f} | {current_volume:^12.2f}")

    if abs(error) <= tolerance:
        break