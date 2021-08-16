#!/usr/bin/env python3
import random

# Time window: 11 - 21
# Duration: 4 - 6
# No more than 20 hours between slots
# One slot per day

# 7 days

# Generate duration
# Generate start time

# Generate duration for next day
# Generate start time
# Check if starve time is longer than 20 hours
# Regenerate start time if so

#We're going to be creating an object for each day. Let's just make a class to make life easy
class dayObj:
    startTime = 0
    endTime = 0
    duration = 0
    name = ""

#Instatiate Monday as an object based on the day class
monday = dayObj()
#Generate the eating period for Monday (4 to 6 hours)
monday.duration = random.randint(4,6)
#The end time is then at most 21:00 minus whatever duration we just generated. 
# It could be less but it can never be more.
tmpMaxEndTime = 21 - monday.duration
#Generate the start time
monday.startTime = random.randint(11,tmpMaxEndTime)
#Log the end time to make some maths easier
monday.endTime = monday.startTime + monday.duration

#Instantiate the other days
tuesday = dayObj()
wednesday = dayObj()
thursday = dayObj()
friday = dayObj()
saturday = dayObj()
sunday = dayObj()

#Name them in a sloppy way
monday.name = "Monday"
tuesday.name = "Tuesday"
wednesday.name = "Wednesday"
thursday.name = "Thursday"
friday.name = "Friday"
saturday.name = "Saturday"
sunday.name = "Sunday"

#Load up a list
week = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

#We've already done Monday so the loop actually starts at 1 rather than 0
currentIndex = 1

#Iterate through them
for day in week:
    #I can't be fucked reworking this so if it's Monday we'll just skip it!
    if currentIndex < 2:
        currentIndex += 1
    else:
        #Generate the day's duration
        day.duration = random.randint(4,6)

        #A temporary start time and end time as something squirrely is happening
        #As in this should finish and then move to the next item but apparently not.
        #There's bound to be a sensible reason for this I can't be bothered finding it right now.
        day.startTime = random.randint(11,(21 - day.duration))
        day.endTime = day.startTime + day.duration

        #The lower bound for the days following Monday is a tad complicated. 
        #In total it needs to start less than 20 hours after the previous day
        previousDayStarveDuration = 24 - week[(currentIndex - 2)].endTime
        #The lower bound can then be up to 20 hours from that but no more.
        upperBound = 20 - previousDayStarveDuration
        #Debugging stuff. I have NO IDEA why it needs to be -2 not -1. Ugh.
        # print(str(week[(int(currentIndex) - 2)].name) + "\'s end time is " + str(week[(currentIndex - 2)].endTime))
        # print("Therefore the " + str(day.name) + " start time can be no later than " + str(((week[(currentIndex - 2)].endTime) + 20)-24))
        #The upper bound could still go over 21 though and that's bad.
        while previousDayStarveDuration + day.startTime > 20:
            day.startTime = random.randint(11,(21 - day.duration))
        # print("Start time generated is " + str(day.startTime) + "\n")
        day.endTime = day.startTime + day.duration

        currentIndex += 1

print("Schedule details:")
for day in week:
    print("###  " + day.name + "  ###")
    print("Start of slot: " + str(day.startTime) + ":00")
    print("End of slot: " + str(day.endTime) + ":00" + "\n")
    