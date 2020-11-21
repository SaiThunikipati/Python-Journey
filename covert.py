# write a program to convert kilometrs into miles
kilometers = float(input("Enter value in kilometers: "))
conv_fac = 0.62137125
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))