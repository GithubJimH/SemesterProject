# Allowing the user to enter their stats with specific instructions
input_string = input('Enter your Bench,Squat,Deadlift separated by a space:')
print("\n")
lst = input_string.split()
# Showing users stats or a sort of refresher
print('Your Bench,Squat,Deadlift: ', lst)
# converting to an integer for the functions math
for i in range(len(lst)):
# Converting typed info into int
    lst[i] = int(lst[i])
# Establishing the lists for each of the comparisons
MarkHenry:list[int] = [585,1006,925] # Mark total lift
Kazmaier:list[int] =[661, 925,837] # Kaz total lift
Magnusson:list[int] = [485, 937,1016] # Mag total lift
percentages: list[int] = []
# printing the list comparisons with compact math
print('Your lifts compared to Mark Henry: ', *map(lambda x, y: x/y, lst, MarkHenry))
print('Your lifts compared to Kazmaier', *map(lambda x, y: x/y, lst, Kazmaier))
print('Your lifts compared to Magnusson', *map(lambda x, y: x/y, lst, Magnusson))
