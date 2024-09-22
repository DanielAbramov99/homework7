counter_jumps = 0
sum_jump = 0

best_jump: float = None
record_jump: str = None
record_jump_number: float = None
for j in range(7):
    name: str = str(input("enter contestant name:"))
    jump: float = float(input("enter contestant jump result:"))
    if jump < 5.80:
        continue
    else:
        if jump >= 5.80:
            counter_jumps += 1
            sum_jump += counter_jumps
        if best_jump is None or jump > best_jump:
            best_jump = jump

        if jump > 6.23:
            counter_jumps += 1
            sum_jump += counter_jumps
        if record_jump is None or jump > 6.23:
            record_jump = name

        j += 1
    if j == 7:
        print(f"the best jump is:{best_jump}")
        print(f"the record jump belongs to: {record_jump}")

avg_jump: float = sum_jump / counter_jumps
print(f"the average of all jumps is:{avg_jump}")
