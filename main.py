import json
from textwrap import indent
import requests
import os



list1=[]
count = 0
page_no=1
def send_request(page=1, keyword="कोरोना"):
    global count
    url ="https://bg.annapurnapost.com/api/search?title="+str(keyword)+"&page="+str(page)
    try:
        response = requests.get(url)
        print('Response HTTP Status Code: ', response.status_code)
        print('Response HTTP Response Body: ', type(response))
        
        res = response.json()
        v=res['data']['items']

        for val in v[0]:
            list1.append(val)
        
        count += len(v)
        print(count)
        
        for vals in v:
            temp1 = {}
            for key in list1:
                temp1[key] = vals[key]
                
            try:
                with open("jsonFile.json", "a", encoding="utf-8") as file:
                    json.dump(temp1, file, indent=2)

                # Just For checking Language
                with open("jsonFile.txt", "a", encoding="utf-8") as f:
                    f.write(str(temp1))

            except Exception as err:
                print("Error Occurs in FIle : ",err)
            finally:
                file.close()
                f.close()
        try:
            pg={
                'page':page
            }
            with open("jsonFile.json", "a", encoding="utf-8") as file:
                    json.dump(pg, file, indent=2)
            with open("jsonFile.txt", "a", encoding="utf-8") as f:
                    f.write("\npage:"+str(page))
        except Exception as er:
            print("Error Occurs as : ",er)
    except Exception as error:
        print("Error occurs : ", error)
    finally:
        pass    


query_str = input("Enter Query String: ")

# checking If file already Exist
fileName = "jsonFile.json"
existance = os.path.exists(fileName)
# print(existance)

if(existance):
    try:
        with open('jsonFile.json', 'r', encoding="utf-8") as f:
            last_line = f.readlines()[-2]
            previous_page=last_line.split(':')[-1]
            print("Up to page = "+previous_page+"Has been fetched. Next will start From Page: "+str(int(previous_page)+1))
            count = int(previous_page)*10   #since 10 article is shown per page
            page_no=int(previous_page)+1
            print("Count Value== ",count)
    except Exception as err:
        print("Error Occurs: ",err)


# Calling for 3times for 30 articles
while(count<30):
    send_request(page=page_no, keyword=query_str)
    page_no+=1

