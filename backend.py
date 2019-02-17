import json

"""Usernames"""
def usernameDB(uid, username):

    #Formatting pythonic dictionary to githubData.json format
    dataToAppend = [{
        "uid" : uid,
        "username" : username
    }]

    #Capturing old data
    with open("static/userData.json") as dataViewer:
        oldData = json.load(dataViewer)


    #Checking if data is already present for repo
    for n in oldData:
        #remove old info and bump updated info to top
        if dataToAppend[0]['uid'] == n['uid']:

            filteredData = [d for d in oldData if d['uid'] != n['uid']]
            newData = dataToAppend + filteredData

            with open("static/userData.json", "w") as writeToFile:
                json.dump(newData, writeToFile)

            break

    #add new repo to top
        else:
            newData = dataToAppend + oldData

            with open("static/userData.json", "w") as writeToFile:
                json.dump(newData, writeToFile)

"""Usernames"""
def projectDB(userID, identifier, name, desc, imgurl):

    #Formatting pythonic dictionary to githubData.json format
    dataToAppend = [{
        "uid" : userID,
        "identifier": identifier,
        "name": name,
        "desc": desc,
        "imgurl": imgurl
    }]

    #Capturing old data
    with open("static/projectData.json") as dataViewer:
        oldData = json.load(dataViewer)



    newData = dataToAppend + oldData

    with open("static/projectData.json", "w") as writeToFile:
        json.dump(newData, writeToFile)
