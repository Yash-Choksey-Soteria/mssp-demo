import limacharlie
import requests
import json
import sys


#This is the API key for the Yash's organization of LimaCharlie.
YASH_API_KEY='0b1a506c-95d3-4be4-9cf6-08692c78e2c2'
OID='ffc59d08-4169-4498-a181-a2b42dded7b0'




#Get the JWT from the API Key and the OID
url = "https://jwt.limacharlie.io"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "oid": OID,           
    "secret": YASH_API_KEY  
}

response = requests.post(url, headers=headers, data=data, timeout=20)

if response.status_code == 200:
    JWT=response.json().get("jwt")
else:
    print("Failed to get JWT:", response.status_code, response.text)
    exit(-1)


request=input("Enter the request you want to send to the LimaCharlie API (enter exit to exit): ")
#This is the URL for the LimaCharlie API.
request=request.upper()

url="https://api.limacharlie.io/v1/"

while (request!='EXIT'):
    if (request==''):
        print("Not implimented")

    if (request=="API KEY"):
        response=requests.get(url+"orgs/"+OID+"/keys", headers={'Authorization': 'Bearer ' + JWT},timeout=20)

        if response.status_code == 200:
            print("Request successful")
            data=response.json()

            json_string = json.dumps(data, indent=4)
            print(json_string)
        else:
            print(f"Request failed with status code {response.status_code}")
            exit(-1)

    if (request=="HIVE GET"):
        #List oppurations related to the configuration hive

        response=requests.get(url+"/hive/secret/"+OID, headers={'Authorization': 'Bearer ' + JWT},timeout=20)

        if response.status_code == 200:
            print("Request successful")
            data=response.json()

            json_string = json.dumps(data, indent=4)
            print(json_string)
        else:
            print(f"Request failed with status code {response.status_code}")
            exit(-1)

        response=requests.get(url+"/hive/dr-general/"+OID, headers={'Authorization': 'Bearer ' + JWT},timeout=20)

        if response.status_code == 200:
            print("Request successful")
            data=response.json()

            json_string = json.dumps(data, indent=4)
            print(json_string)
        else:
            print(f"Request failed with status code {response.status_code}")
            exit(-1)
    
    if (request=="HIVE POST DR"):

        #First get the yaml file that will be the D/R rule


        #Then convert the yaml file to the associated 2 json bodys required
            # The first is the body, formatted in the form dictated by exampledr.yml
            # The second is the metadata of that rule, Going to test out what format that can be in.








        print("Not implemented")

    if (request=="HIVE EXTENSION GET"):

        response=requests.get(url+"/orgs/"+OID+"/subscriptions", headers={'Authorization': 'Bearer ' + JWT},timeout=20)

        if response.status_code == 200:
            print("Request successful")
            data=response.json()

            json_string = json.dumps(data, indent=4)
            print(json_string)
        else:
            print(f"Request failed with status code {response.status_code}")
            exit(-1)


    



    request=input("Enter the request you want to send to the LimaCharlie API (enter exit to exit): ").upper()

print("Exited sucessfully")
sys.exit(0)


# How the hive works

# hive_name refers to the category of config: secret, cloud_sensor, 



# YARA_SIG = 'https://raw.githubusercontent.com/Yara-Rules/rules/master/Malicious_Documents/Maldoc_PDF.yar'

# # Create an instance of the SDK.
# man = limacharlie.Manager()
 
# # Get a list of all the sensors in the current Organization.
# all_sensors = man.sensors()

# # Select the first sensor in the list.
# sensor = all_sensors[ 0 ]

# # Tag this sensor with a tag for 10 minutes.
# sensor.tag( 'suspicious', ttl = 60 * 10 )

# # Send a task to the sensor (unidirectionally, not expecting a response).
# sensor.task( 'os_processes' )

# # Send a yara scan to that sensor for processes "evil.exe".
# sensor.task( 'yara_scan -e *evil.exe ' + YARA_SIG )
