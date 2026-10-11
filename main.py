# mlb trade calculator project
print("--- MLB All-Stadium Trade Simulator ---")
print("")

# get player info from user
name = input("Enter player name: ")
hr = int(input("Enter home runs hit: "))

print("")
print("Select CURRENT stadium number:")
print("1: Arizona | 2: Atlanta | 3: Baltimore | 4: Boston | 5: Cubs")
print("6: White Sox | 7: Cincinnati | 8: Cleveland | 9: Colorado | 10: Detroit")
print("11: Houston | 12: Kansas City | 13: Angels | 14: Dodgers | 15: Miami")
print("16: Milwaukee | 17: Minnesota | 18: Mets | 19: Yankees | 20: Oakland")
print("21: Phillies | 22: Pittsburgh | 23: Padres | 24: Giants | 25: Mariners")
print("26: Cardinals | 27: Rays | 28: Rangers | 29: Blue Jays | 30: Nationals")
stadium1 = int(input("Enter number (1-30): "))

# find current park factor value
if stadium1 == 9:
    pf1 = 112  # Colorado altitude
elif stadium1 == 4 or stadium1 == 7 or stadium1 == 19 or stadium1 == 21 or stadium1 == 29:
    pf1 = 105  # hitter parks (boston, cincy, yankees, philly, toronto)
elif stadium1 == 10 or stadium1 == 12 or stadium1 == 18 or stadium1 == 23 or stadium1 == 24 or stadium1 == 25:
    pf1 = 93   # pitcher parks (detroit, kc, mets, padres, giants, mariners)
else:
    pf1 = 100  # neutral parks (everyone else)

print("")
print("Select DESTINATION stadium number:")
stadium2 = int(input("Enter number (1-30): "))

# find target park factor value and type
if stadium2 == 9:
    dest_name = "Coors Field (Altitude Boost)"
    pf2 = 112
elif stadium2 == 4 or stadium2 == 7 or stadium2 == 19 or stadium2 == 21 or stadium2 == 29:
    dest_name = "Hitter-Friendly Stadium"
    pf2 = 105
elif stadium2 == 10 or stadium2 == 12 or stadium2 == 18 or stadium2 == 23 or stadium2 == 24 or stadium2 == 25:
    dest_name = "Pitcher-Friendly Stadium"
    pf2 = 93
else:
    dest_name = "Neutral Stadium"
    pf2 = 100

# basic algebra steps to calculate changes
neutral_hr = hr / (pf1 / 100)
projected_hr = round(neutral_hr * (pf2 / 100))

# display final outputs
print("")
print("--- SIMULATION RESULTS ---")
print("Player Name:", name)
print("Moving to:", dest_name)
print("Old Home Runs:", hr)
print("Predicted New Home Runs:", projected_hr)
print("--------------------------")

# output message logic
if projected_hr > hr:
    diff = projected_hr - hr
    print("Result: HRs increase by +" + str(diff) + " due to stadium sizes.")
elif projected_hr < hr:
    diff = hr - projected_hr
    print("Result: HRs drop by -" + str(diff) + " due to stadium sizes.")
else:
    print("Result: Environment is identical. No changes.")
