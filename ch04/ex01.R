N = sum(HairEyeColor)

print('Hair / eye proportion')
hair_eye_prop = apply(HairEyeColor, c('Eye', 'Hair'), sum)/ N
print(round(hair_eye_prop, 2))

print('Hair proportion')
hair_prop = apply(HairEyeColor, c('Hair'), sum)/ N
print(round(hair_prop, 2))

print('Eye proportion')
eye_prop= apply(HairEyeColor, c('Eye'), sum) / N
print(round(eye_prop, 2))

print('P(eye | hair=Brown)')
eye_g_brown = hair_eye_prop[,'Brown'] / hair_prop['Brown']
print(round(eye_g_brown, 2))

print('P(hair | eye=Brown)')
hair_g_brown = hair_eye_prop['Brown',] / eye_prop['Brown']
print(round(hair_g_brown, 2))
