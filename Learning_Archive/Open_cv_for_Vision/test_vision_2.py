import cv2

while True:
    choice=input("Would you like to continue[Y/N]:")
    if choice.upper() not in ('Y','N'):
        print("Invalid Input!Are you dumb?Are you blind for not seeing the option to choose from?")
        continue
    else:
        if choice.upper() == 'N':
            break
        else:
            mycam= cv2.VideoCapture(0)

            for i in range(10):
                mycam.read()
            
            validity,pic=mycam.read()
            mycam.release()

            image_name = input("Enter image name:")
            img_name = image_name + ".jpeg"
            cv2.imwrite(img_name,pic)
            
            print("Done.")

#learning complete --- moving to stage 2, recored video and live cam for true vision