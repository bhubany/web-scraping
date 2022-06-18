import json
from textwrap import indent
import requests



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
    except Exception as error:
        print("Error occurs : ", error)
    finally:
        pass    


query_str = input("Enter Query String: ")
while(count<30):
    send_request(page=page_no, keyword=query_str)
    i+=1

