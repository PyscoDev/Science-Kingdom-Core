class servo:
    start_angle= 90

    def __init__(self,pin):
        self.pin= pin
        self.current_angle= start_angle

    def get_status(self):
        pass