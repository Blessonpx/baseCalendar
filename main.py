from models.eventModel import Event
import json
import uuid
import shutil


def createEvent(eventName,startDay,startMonth,startYear,startHour,startMinute,endDay,endMonth,endYear,endHour,endMinute,location):
    event1 = Event(eventName,startDay,startMonth,startYear,startHour,startMinute,endDay,endMonth,endYear,endHour,endMinute,location)
    id=uuid.uuid1()
    aDict = {"id":str(id), "Name":event1.get_name(), "StartDate":str(event1.get_startDate()),"EndDate":str(event1.get_endDate()),"Location":event1.get_location(),"State":event1.get_state()}
    with open('data/events.json', 'r+') as file:
        file_data=json.load(file)
        file_data["Events"].append(aDict)
        file.seek(0)
        json.dump(file_data,file,indent=4)

def findById(id):
    with open('data/events.json', 'r') as file:
        file_data=json.load(file)
        output_dict = [x for x in file_data['Events'] if x['id']==id ]
        output_json = json.dumps(output_dict)
        print(output_json)

def findByName(Name):
    with open('data/events.json', 'r') as file:
        file_data=json.load(file)
        output_dict = [x for x in file_data['Events'] if x['Name']==Name ]
        output_json = json.dumps(output_dict)
        print(output_json)


def updateById(id,jsonList):
    with open('data/events.json', 'r+') as file:
        file_data=json.load(file)
        otherevents=[x for x in file_data['Events'] if x['id']!=id ]
        event=[]
        event=[x for x in file_data['Events'] if x['id']==id ]
        if len(event)== 0:
            return 
    if jsonList[0]['Name']:
        event[0]['Name']=jsonList[0]['Name']
    if jsonList[0]['StartDate']:
        event[0]['StartDate']=jsonList[0]['StartDate']
    if jsonList[0]['EndDate']:
        event[0]['EndDate']=jsonList[0]['EndDate']
    if jsonList[0]['Location']:
        event[0]['Location']=jsonList[0]['Location']
    if jsonList[0]['State']:
        event[0]['State']=jsonList[0]['State']
    aDict = {"id":id, "Name":event[0]['Name'], "StartDate":event[0]['StartDate'],"EndDate":event[0]['EndDate'],"Location":event[0]['Location'],"State":event[0]['State']}
    with open('data/events.json', 'r+') as file:
        file_data=json.load(file)
        file_data["Events"]=[x for x in file_data['Events'] if x['id']!=id ]
        file_data["Events"].append(aDict)
        file.seek(0)
        json.dump(file_data,file,indent=4)
    
def deleteById(id):    
    shutil.copyfile('data/events_base.json','data/events_new.json')
    with open('data/events.json', 'r+') as file:
        file_data=json.load(file)
        event=[x for x in file_data['Events'] if x['id']==id ]
        if len(event)==0:
            return
        for idx,obj in enumerate(file_data['Events']):
            if obj['id']==id:
                file_data['Events'].pop(idx)
                new_file_data=file_data
    with open('data/events_new.json', 'r+') as file:
        file.seek(0)
        json.dump(new_file_data,file,indent=4)
    shutil.copyfile('data/events_new.json','data/events.json')
    shutil.copyfile('data/events_base.json','data/events_new.json')

findById('fd94ed40-0676-11ed-810c-1dc13fa2a8bd')
findByName('Event2')
jsonList=[
    {
            "Name": "Event14",
            "StartDate": "2022-01-01 13:01:00",
            "EndDate": "2022-01-02 14:10:00",
            "Location": "Bengaluru",
            "State": "neutral"
    }]
updateById('21ab1e3d-0677-11ed-810c-1dc13fa2a8bd',jsonList)
deleteById('21ab1e3d-0677-11ed-810c-1dc13fa2a8bd')


# createEvent('Event1',1,1,2022,13,1,2,1,2022,14,10,'Bengaluru',)
# createEvent('Event2',1,1,2022,13,1,2,1,2022,14,10,'Bengaluru',)
# createEvent('Event3',1,1,2022,13,1,2,1,2022,14,10,'Bengaluru',)
# createEvent('Event4',1,1,2022,13,1,2,1,2022,14,10,'Bengaluru',)




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

