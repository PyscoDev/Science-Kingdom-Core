class Robot:
    def __init__(self,name):
        self.name= name
        self.battery= 50
    def greet(self):
        print(f"Hello,I am {self.name}.System online.")
    def charge(self):
        print("Charging....")
        while self.battery<100:
            self.battery+=1
            print(self.battery)
        print(f"{self.name} is now fully charged!")
    

my_first_robot= Robot("Unit-01")
my_second_robot= Robot("Alpha-7")

my_first_robot.greet()
my_second_robot.greet()

print(f"Battery of {my_second_robot.name} is currently {my_second_robot.battery}. Preparing to charge....")
my_second_robot.charge()