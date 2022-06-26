import json
import requests

list2=[]

def send_request(page=1, keyword="कोरोना", list2=[]):
    while(page <= 3):
        url ="https://bg.annapurnapost.com/api/search?title="+str(keyword)+"&page="+str(page)    

        response = requests.get(url)
        if(response.status_code == 200):         
            res = response.json()
            res_data=res['data']['items']                      
            list2.append(res_data)
            page+=1
        else:
            print("Error Occurs with Status Code: ",response.status_code )

    if(len(list2) != 0):
        try:
            with open("jsonFile.json", "w", encoding="utf-8") as file:
                json.dump({'current_page':(page), 'articles':list2}, file, indent=2)
        except Exception as err:
            print("Error Occurs creating Json File : ",err)
        finally:
            file.close()

query_str = input("Enter Query String: ") # Taking Keywords
try:
    file= open('jsonFile.json', 'r', encoding="utf-8")
    data = json.load(file)
    print("Up to page = {} Has been fetched (limit is set to 3).".format(data['current_page']-1))
    send_request(page=data['current_page'],keyword=query_str, list2=data['articles'])
except:
    send_request()
