import cv2

mycam= cv2.VideoCapture(0)
Codec=cv2.VideoWriter_fourcc(*'XVID')
name=input("Enter the file name:")
filename=name+".avi"
output=cv2.VideoWriter(filename,Codec,20.0,(640,480))

print("Recording.............. press 'q' to exit")

while True:
    
    Validity,frame=mycam.read()
    
    if Validity:
        output.write(frame)
        cv2.imshow("First Try",frame)

    # If the 'q' key is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

mycam.release()
output.release()
cv2.destroyAllWindows()

#ovservation: after 2 tries video capture is okay but lacks sound so need to work on it.