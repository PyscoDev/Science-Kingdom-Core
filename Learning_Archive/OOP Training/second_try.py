class Robot:
    def __init__(self,name):
        self.name= name
        self.battery=50
    def greet(self):
        print(f"Hi. I am {self.name}. Nice to meet you.")

class MedicRobot(Robot):
    def greet(self):
        print(f"Hi. I am {self.name}. I heal units and my kind heal eachother too.")
    def heal(self,target_robot):
        print(f"Healing {target_robot.name}...")
        while target_robot.battery<100:
            target_robot.battery+=1
            print(target_robot.battery)
        print(f"{target_robot.name} is now fully charged!")


my_first_robot= Robot("Unit-01")
healer1= MedicRobot("Elder Elf")
healer1.greet()
healer1.heal(my_first_robot)
