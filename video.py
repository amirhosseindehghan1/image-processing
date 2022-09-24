import  cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # if set gray, the video will be black & white
    # if set frame, the video will be colory
    cv2.imshow('my video', frame)

# if press Q on your keyboard, the window wii be close
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()