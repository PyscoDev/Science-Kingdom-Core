import ollama
import cv2
import time #for time control of action

#to analyse
def image_analyse(the_image):
        
    print("Analysing.......")
    response = ollama.chat(model='moondream',messages=[{'role':'user','content':"What do you see?",'images':[the_image]}])
    
    print(response['message']['content'])
    #learning
    


#to get image
def get_image():
    my_cam=cv2.VideoCapture(0)
    
    name=input("Enter the name of the image")
    image_name=name+'.jpeg'

    for i in range(10):
        my_cam.read()

    chk,frame=my_cam.read()
    cv2.imwrite(image_name,frame)
    print("Successfully captured.Sending to analyse....")
    my_cam.release()
    image_analyse(image_name)


#to analyse many of them
def main_stream():
    user_choice=input("Do you want to continue?[Y/N]")
    if user_choice.upper() in ('Y','N'):
        if user_choice.upper() == 'N':
            print("Thank you for thinking me as useful. See you")
            time.sleep(2)
            exit()
        else:
            get_image()
            main_stream()
    else:
        print("Are you unable to see the choice dummy???? Only y or n. Retry... All have potential!!")
        main_stream()

#start of the program
main_stream()