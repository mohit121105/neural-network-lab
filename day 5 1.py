target_temp = 22.0
room_temp = 20.0
heater_setting=5.0
learning_rate = 0.2
x=1
max_iterations = 20
print("Step|Room Temp|Error|∆Heater|New Heater Setting")
print("-"*50)
for step in range(1, max_iterations+1):
    error=target_temp-room_temp
    delta_w = learning_rate * error * x
    heater_setting += delta_w
    room_temp += delta_w * 5
    if abs(target_temp - room_temp) < 0.01:
        room_temp = target_temp
    print(f"{step^4} | {room_temp:^9.2f} | {error:^5.2f} | {delta_w:^7.2f} | {heater_setting:^16.2f}")
    if room_temp == target_temp:
        break