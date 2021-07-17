import Teams_name as Tname
import time
driver,teams,teams_name = Tname.TeamsName()

print("Present teams in the account are : \n")
for team in teams_name:
    print(team)

print("\n\nWhich team would you like to click on ?\n")
team = input('Enter the team name  ::  ')

if team in teams_name:
    for t in teams:
        if team == t.text:
            t.click()
            break
else:
    print("\nOOPS!! selected team is not present!")