""" / Abdullah Alazzani
This programe Calculates the areas
of Circles and Triangales
"""
print ("Starting the Calculator ...")

option = input("Enter C for Circle or T for Triangle: ").upper()

if option == 'C':
  radious = float(input("Enter radius: "))
  area = 3.14159 * radious ** 2  
  print ("The area of circle with radious %f is %f" % (radious, area))
elif option == 'T':
  base = float(input("Enter base: "))
  height = float(input("Enter height: "))
  area = 0.5 * base * height
  print ("The area of tringale with base %f and height %f is %f " % ( base, height, area))
else: 
  print ("Error! Invalid shape.")
  
print ("Exiting ...")
