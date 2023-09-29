import cv2 as cv

# Open the video file
cap = cv.VideoCapture('test.mp4')
if not cap.isOpened():
    print("Error : Video can not opened!!")
    exit()

# Initialize variables
w = 0  # Width counter
obje = 1  # Object counter
new_object = True  # Flag to track the start of a new object
collect_x = True  # Unused, can be removed
obj_values = set()  # Unused, can be removed
pr = set()  # Set to keep track of processed objects
i_arr = []  # List to store detected object positions (pixel indices)
left_max = {}  # Dictionary to store left maximum values for objects
right_min = {}  # Dictionary to store right minimum values for objects
left = []  # List to store leftmost positions of objects
right = []  # List to store rightmost positions of objects

while True:
    ret,frame = cap.read()
    if not ret:
        break
    # Taking 1px slice of the frame
    cut = frame[310:311,0:640]
    # Color gray
    gray = cv.cvtColor(cut,cv.COLOR_BGR2GRAY)
    # Threshold
    _,binary = cv.threshold(gray,175,255,cv.THRESH_BINARY)
    # Finding contours
    contours,_ = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(cut,contours,-1,(0,0,255),1)
    
    # Get materials location and i values
    for i in range(640):
        if binary[0,i] == 255:
            w += 1
            i_arr.append(i)

    # Object counting
    if new_object:
        if w == 0:
            obje += 1
            new_object = False
        else:
            new_object = True
    else:
        if w!= 0:
            new_object = True
            
                    
    
    if i_arr:
            i_arr.sort()
            if i_arr[0] <= 50: x_sol = i_arr[0]
            if i_arr[-1] >=250: sag_x = i_arr[-1]
                

    if left==[]:left.append(x_sol)
    else:
        if x_sol >= left[0]:
            left[0] = x_sol
        else:continue
    if right==[]:right.append(sag_x)
    else:
        if sag_x <= right[0]:
            right[0] = sag_x
        else:continue
    
    for i in range(1,obje+1):
        if i not in pr:    
            left_max[i] = left[0]
            right_min[i] = right[0]
            print(f"Nesne : {i}\nSol max : {left_max[i]}  --  Sağ min : {right_min[i]}")
            pr.add(i)
    right = []
    left = []
    i_arr = []        
    



    

    w = 0

    cv.imshow("Display",frame)
    if cv.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv.destroyAllWindows()
