from machine import Pin, PWM

class Servo_180:

    def __init__(self,servo_pin,frequency,in_min,in_max,out_min,out_max):
        
        self.in_min=in_min
        self.in_max=in_max
        self.out_min=out_min
        self.out_max=out_max

        self.the_servo=PWM(Pin(servo_pin))
        self.the_servo.freq(frequency)


    def value_mapper(self,angle):
        return int((angle-self.in_min)/(self.in_max-self.in_min)*(self.out_max-self.out_min)+self.out_min)

    def set_angle(self,current_angle):
        wtd= self.value_mapper(current_angle)
        self.the_servo.duty_u16(wtd)

if __name__=="__main__":
    sample_servo= Servo_180(15,50,0,180,1800,8200)
    sample_servo.set_angle(0)
    sample_servo.set_angle(90)
    sample_servo.set_angle(180)
    sample_servo.set_angle(0)