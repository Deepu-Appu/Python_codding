def life_in_weeks(age):
    # if we live upto 90 the years we have is 90 - current age
    years = 90 - age
    # one year has 52 weeks, then total week left is: the number of year left x week in one year
    total_weeks_left = 52 * years
    outcome = print (f"You have {total_weeks_left} weeks left.")
    
# calling the function
life_in_weeks(12)