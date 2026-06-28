import json
import uuid
import re

class BirthdayManager:
    def __init__(self,filename="birthdays.json"):
        self.filename=filename
        self.data=self.load_data()

    def load_data(self):
        try:
            with open(self.filename,'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.filename,'w') as file:
            json.dump(self.data,file,indent=4)
    
    def add_birthday(self,name,date,month,year):
        uid= str(uuid.uuid4())
        self.data[uid] ={"name":name,"date":date,"month":month,"year":year}
        self.save_data()
    def view_birthday(self):
        for i in self.data:
            individual_data=[i,self.data[i]]
            yield individual_data
    def chk_month(self,month):
        for i,info in self.data.items():
            if info["month"]==month:
                yield i,info
    def chk_name(self,name):
        for i,info in self.data.items():
            if re.sub(r'[^a-zA-Z0-9]', '', info['name']).lower()==re.sub(r'[^a-zA-Z0-9]', '', name).lower():
                yield i,info
    def deletion(self,ID):
        if ID in self.data:
            del self.data[ID]
            self.save_data()
            return "Data deleted successfully!"
        else:
            return "No matching ID found!"