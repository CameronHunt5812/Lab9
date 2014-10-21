############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
print "what is your temperature?"
temp = int(raw_input())
print "have you been sick in the last 24 hours?"
print "1 = yes 0 = no"
sick = int(raw_input())
# Additionally, ask if the user has recently travelled to West Africa.
print "have you rescently travled to west africa?"
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
