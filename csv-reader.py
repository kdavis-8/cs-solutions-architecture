import csv
import urllib.parse
import urllib.request
import urllib.error
import urllib.response
import json

headers = {"Content-Type": "application/json", "Authorization": "csAPIkey "}

def fileReader():
    filename = 'PUT-FILE-NAME-HERE.csv'
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            username = row["username"]
            fullName = row["fullName"]
            role = row["role"]
            
    
            
            createUser(username,fullName,role)

    print("Total number of users added: %d"% (reader.line_num-1))
    f.close    

def createUser(username,fullName,role):  # Need to work with Thomas or David to see what we will use for API Calls 
    url="https://api.chaossearch.com/v1/users"
   
    data = json.dumps({
    "username": username,
    "fullName": fullName,
    "role": {"name":role}
    }).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        the_page = response.read()
    
    except IOError as e:
        print (e)

def main():
    fileReader()

if __name__== "__main__":
    main()

#need to understand what the response would be if they exceed license
#add conflict, 409 response.
