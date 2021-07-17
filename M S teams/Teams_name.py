import Login as log
import User_data as UD
import time

def TeamsName():
    Email,Password = UD.User_data['Email'],UD.User_data['Password']
    message,driver = log.Login(Email,Password)

    if driver == None:
        print(message)

    else:
        print(message)

        time.sleep(8)
        teams = driver.find_elements_by_class_name("team-name-text")

        time.sleep(2)

        teams_name = []
        for team in teams:
            teams_name.append(team.text)
        
        print("\n")

    return driver,teams,teams_name
    
