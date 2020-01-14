import statistics
sum_multiply_first_val = 1+2+3*3
print(sum_multiply_first_val)
# 1+2+3*3 = 1+2+9 = 12
sum_first_multiply_val = (1 + 2 + 3) * 3
print(sum_first_multiply_val)
# (1+2+3)*3 = 6*3 = 18
power_val = 3 ** 2
print(power_val)
# POWER => 3^2 = 9
xor_val = 10^2
print(xor_val)
# XOR => 10 ^ 2 = 000110(2) ^ 000010(2) = 000100(2) = 8
modulo_val = 9 % 2
print(modulo_val)
# 9/2 = 4 rest => 1
integer_division_val = 7 // 2
print(integer_division_val)
# 7 / 2 = (int) 3.5 = 3

# QUIZ
# 1
bill_1 = 23
bill_2 = 32
bill_3 = 64
average_bills = (bill_1 + bill_2 + bill_3)/3
print(average_bills)
average_bills_mean_func = statistics.mean([bill_1, bill_2, bill_3])
print(average_bills_mean_func)

# 2
tiles_in_package = 6
part_1_tiles_wide = 9
part_1_tiles_long = 7
part_2_tiles_wide = 5
part_2_tiles_long = 7
all_tiles = (part_1_tiles_wide * part_1_tiles_long) + (part_2_tiles_wide * part_2_tiles_long)
packages = (all_tiles + tiles_in_package // 2) // tiles_in_package
print(packages)

bought_tiles = 17 * tiles_in_package
left_tiles = bought_tiles - all_tiles
print(left_tiles)
# 3

# 4