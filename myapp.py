import requests
import json

URL = "http://127.0.0.1:8000/Studentapi/"

# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {'id':id}
#     json_data = json.dumps(data)
#     r = requests.get(url = URL, data = json_data)
#     data = r.json()
#     print(data)

# get_data()


# def delete_data():
#     data = {'id': 2}

#     json_data = json.dumps(data)
#     r = requests.delete(url = URL, data = json_data)
#     data = r.json()
#     print(data)
# delete_data()



def post_data():
    data = {
        'Name': 'mahad',
        'City': 'Karachi',
        'Age':19,
        'Roll_Number': 18965,
        'School_Name': 'The Smart School',
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)
post_data()



# def update_data():
#     data = {
#         'id': 4,
#         'Name': 'sameer',
#         'City': 'Rawalpindi',
#         'Age':25,
#         'Roll_Number': 18965,
#         'School_Name': 'The Smart School',
#     }
#     json_data = json.dumps(data)
#     r = requests.put(url = URL, data = json_data)
#     data = r.json()
#     print("data",data)


# update_data()   


