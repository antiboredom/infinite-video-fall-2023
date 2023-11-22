import cv2


# create the background subtractor
mog = cv2.createBackgroundSubtractorMOG2()

# capture from the camera
cap = cv2.VideoCapture(0)

# loop forever
while True:
    # get the current frame
    ret, frame = cap.read()

    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # apply the background subtractor
    fgmask = mog.apply(gray)

    # erode and than dilate to remove small blobs
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    fgmask = cv2.dilate(fgmask, kernel, iterations=1)

    # find contours (continuous blobs of pixels)
    # these will only exist if there is motion!
    contours, hierarchy = cv2.findContours(
        fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # loop through the contours
    for contour in contours:
        # Ignore small contours
        if cv2.contourArea(contour) < 1000:
            continue

        # Draw bounding box around contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # show the current frame and motion contours
    cv2.imshow("Motion Detection", frame)

    # quit if user presses 'q' key
    if cv2.waitKey(1) == ord("q"):
        break

# cleanup
cap.release()
cv2.destroyAllWindows()
