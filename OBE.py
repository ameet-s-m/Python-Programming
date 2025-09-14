variance_ratio = 25 / 36
mean_X = 55
b_yx = 4 / 3 
constant_term = -100 / 3 
mean_Y_verified = b_yx * mean_X + constant_term
Var_X = 1  
Var_Y = variance_ratio * Var_X  
b_yx_verified = (Var_Y / Var_X) ** 0.5
b_xy_verified = 1 / b_yx_verified  
r_squared_verified = b_yx_verified * b_xy_verified
r_verified = r_squared_verified ** 0.5
print("Mean marks in Statistics (Ȳ):", mean_Y_verified)
print("Coefficient of correlation (r):", r_verified)
