# 9. Sum of Marks (Maths, Physics, Chemistry)
# Question: Calculate the sum of marks in 3 subjects. 
# - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - 
# Output: - Total marks: 263
d={"Maths":85,"Physics":90,"Chemistry":88}
print(d)
totalsum=sum(value for key,value in d.items())
print(totalsum)
# 10. Average of Marks (Maths, Physics, Chemistry)
# Question: Calculate the average of marks in 3 subjects. -
# Input: - Maths = 85 - Physics = 90 - Chemistry = 88 -
# Output: - Average marks: 87.67
average=totalsum/len(d)
print(average)