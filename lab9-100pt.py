############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.



# Additionally, ask if the user has recently travelled to West Africa.

# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# This tells the person they shuld go to the hospital
def ShuldGo():
    print "You shuld go tho the hospital"
    #asking how many more patients
    print "any more patients?"
    print "1 = yes, 0 = no"
    
patients = 1
while (patients == 1):
    #asking for temp
    print "what is your temperature?"
    temp = int(raw_input())
    #asking if sick in the last 24 hours
    print "have you been sick in the last 24 hours?"
    print "1 = yes, 0 = no"
    sick = int(raw_input())
    #asking if bean to west africa recently
    print "have you rescently travled to west africa?"
    print "1 = yes, 0 = no"
    westAfrica = int(raw_input())
# - A temperature of over 105F
    if temp > 105:
        ShuldGo()
        patients = int(raw_input())
# - A temperature of over 102F and they have been sick in the last 24 hours
    elif temp > 102 and sick == 1:
        ShuldGo()
        patients = int(raw_input())
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
    elif temp > 100 or sick == 1 and westAfrica == 1:
        ShuldGo()
        patients = int(raw_input())