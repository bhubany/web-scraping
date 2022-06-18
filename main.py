import json
from textwrap import indent
import requests
import os


list2=[]
count = 0
page_no=1
def send_request(page=1, keyword="कोरोना"):
    global count, list2
    url ="https://bg.annapurnapost.com/api/search?title="+str(keyword)+"&page="+str(page)
    
    try:
        response = requests.get(url)
        if(response.status_code ==200):            
            res = response.json()
            v=res['data']['items']
            
            count += len(v)          
            for vals in v:       
                list2.append(vals)            
            list2.append({'page':page})
        else:
            print("Error Occurs with Status Code: ",response.status_code )
            return True     # true that res error occurs

    except Exception as error:
        print("Error occurs (Requests) : ", error)
    finally:
        pass    


query_str = input("Enter Query String: ")

# checking If not all 30 articles are fetched from the page
fileName = "jsonFile.json"
existance = os.path.exists(fileName)

if(existance):
    try:
        f= open('jsonFile.json', 'r', encoding="utf-8")
        data = json.load(f)
        previous_page=data[-1]['page']

        list2.extend(data) #storing previously fetched Data
        print("Up to page = "+str(previous_page)+" Has been fetched. Next will start From Page: "+str(int(previous_page)+1))
        count = previous_page*10   #since 10 article is shown per page
        page_no=previous_page+1
        print("Count Value== ",count)
    except Exception as err:
        print("Error Occurs (file exist): ",err)


# Calling for 3 times for 30 articles
while(count<30):
    res_err = send_request(page=page_no, keyword=query_str)
    if(res_err):
        break
    page_no+=1

if(len(list2) != 0):
    try:
        with open("jsonFile.json", "w", encoding="utf-8") as file:
            json.dump(list2, file, indent=2)

    except Exception as err:
        print("Error Occurs in (File) : ",err)
    finally:
        file.close()