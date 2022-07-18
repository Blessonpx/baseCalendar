from models.eventModel import Event
import json


event = Event('Event1',1,1,2022,13,1,2,1,2022,14,10,'Bengaluru',)
print(event.get_name())
print(event.get_startDate())
print(event.get_endDate())
print(event.get_location())
print(event.get_state())


# aDict = {"Name":event.get_name(), "StartDate":event.get_startDate(),"EndDate":event.get_endDate(),"Location":event.get_location(),"State":event.get_state()}
# jsonString = json.dumps(aDict, sort_keys=True, default=str)
# with open("data/events.json", 'a') as file:
#             json.dump(jsonString, file, indent=1)

# jsonFile = open("data/events.json", "w")
# jsonFile.write(jsonString)
# jsonFile.close()

event1 = Event('Event1',1,1,2022,13,1,2,1,2022,14,10,'Bengaluru',)
aDict = {"Name":event1.get_name(), "StartDate":str(event1.get_startDate()),"EndDate":str(event1.get_endDate()),"Location":event1.get_location(),"State":event1.get_state()}
with open('data/events.json', 'r+') as file:
        file_data=json.load(file)
        file_data["Events"].append(aDict)
        file.seek(0)
        json.dump(file_data,file,indent=4)


event1 = Event('Event2',1,1,2022,13,1,2,1,2022,14,10,'Bengaluru',)
aDict = {"Name":event1.get_name(), "StartDate":str(event1.get_startDate()),"EndDate":str(event1.get_endDate()),"Location":event1.get_location(),"State":event1.get_state()}
with open('data/events.json', 'r+') as file:
        file_data=json.load(file)
        file_data["Events"].append(aDict)
        file.seek(0)
        json.dump(file_data,file,indent=4)

event1 = Event('Event3',1,1,2022,13,1,2,1,2022,14,10,'Bengaluru',)
aDict = {"Name":event1.get_name(), "StartDate":str(event1.get_startDate()),"EndDate":str(event1.get_endDate()),"Location":event1.get_location(),"State":event1.get_state()}
with open('data/events.json', 'r+') as file:
        file_data=json.load(file)
        file_data["Events"].append(aDict)
        file.seek(0)
        json.dump(file_data,file,indent=4)

event1 = Event('Event4',1,1,2022,13,1,2,1,2022,14,10,'Bengaluru',)
aDict = {"Name":event1.get_name(), "StartDate":str(event1.get_startDate()),"EndDate":str(event1.get_endDate()),"Location":event1.get_location(),"State":event1.get_state()}
with open('data/events.json', 'r+') as file:
        file_data=json.load(file)
        file_data["Events"].append(aDict)
        file.seek(0)
        json.dump(file_data,file,indent=4)

# function to add to JSON
# def write_json(new_data, filename='data/data.json'):
#     with open(filename,'r+') as file:
#           # First we load existing data into a dict.
#         file_data = json.load(file)
#         # Join new_data with file_data inside emp_details
#         file_data["emp_details"].append(new_data)
#         # Sets file's current position at offset.
#         file.seek(0)
#         # convert back to json.
#         json.dump(file_data, file, indent = 4)
 
#     # python object to be appended
# y = {"emp_name":"Nikhil",
#      "email": "nikhil@geeksforgeeks.org",
#      "job_profile": "Full Time"
#     }
     
# write_json(y)



# import json
# from http.server import BaseHTTPRequestHandler, HTTPServer


# def make_handler(myvariable):

#     class GetHandler(BaseHTTPRequestHandler):
#         def _set_headers(self):
#             self.send_response(200)
#             self.send_header('Content-type', 'text/plain')
#             self.end_headers()

#         def do_GET(self):
#             self._set_headers()
#             self.wfile.write(myvariable.encode('utf8'))
#             return

#     return GetHandler

# server = HTTPServer(('127.0.0.1', 5000), make_handler('my_str'))
# print ('Starting server, use <Ctrl-C> to stop')
# server.serve_forever()

# import http.server
# import socketserver

# PORT = 8000

# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("",PORT),Handler) as httpd:
#     print("serving at Port ",PORT)
#     httpd.serve_forever()