import datetime


class Event:
    def __init__(self,eventName,startDay,startMonth,startYear,startHour,startMinute,endDay,endMonth,endYear,endHour,endMinute,location):
        self.eventName=eventName
        self.startDate=datetime.datetime(startYear,startMonth,startDay,startHour,startMinute)
        self.endDate=datetime.datetime(endYear,endMonth,endDay,endHour,endMinute)
        self.location=location
        self.state='neutral'
    
    def get_state(self):
        return self.state
    
    def get_startDate(self):
        return self.startDate
    
    def get_endDate(self):
        return self.endDate
    
    def get_location(self):
        return self.location
    
    def get_name(self):
        return self.eventName
    
    def set_state(self,state):
        self.state=state
        return
    
    def set_startDate(self,startDate):
        self.startDate = startDate
        return
    
    def set_endDate(self,endDate):
        self.endDate=endDate
        return 
    
    def set_location(self,location):
        self.location=location
        return

