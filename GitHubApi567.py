import json
import requests

def pull_info(username):
    request = requests.get('https://api.github.com/users/'+username+'/repos')
    json = request.json()
    try:
        for i in range(0, len(json)):
            commit_num = 0
            print("Project Number:", i+1)
            print("Project Name:", json[i]['name'])
            print("Project URL:", json[i]['svn_url'])
            request2 = requests.get('https://api.github.com/repos/'+username+'/'+json[i]['name']+'/commits')
            json2 = request2.json()
            for i in range(0, len(json2)):
                commit_num += 1
            print("Number of Commits:", commit_num, "\n")
    except:
        return 'Please enter a valid username'
    return 'Successful'

username = input("Enter the github username:")
print(pull_info(username))
