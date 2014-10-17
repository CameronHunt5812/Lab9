############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:

# Ask user for Celcius temperature to convert
print "what tempurature do you want to convert"
# Accept user input 
num1 = int(raw_input())
# Calculate fahrenheit
ancer = ((num1 * 9) / 5) + 32
# Output answer
print "the equivilent fahrenheit temprature is" + str(ancer)