import cv2

# Load pre-trained models for face, eyes, and smiles
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Load the image
image_path = r'C:\Users\Dell\PycharmProjects\Image Processing\Face image.jpg'  # Replace with your image path
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle for face
    roi_gray = gray_image[y:y + h, x:x + w]
    roi_color = image[y:y + h, x:x + w]

    # Detect eyes within the detected face
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20))
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  # Green rectangle for eyes

    # Restrict the region of interest for smile detection to the lower half of the face
    roi_gray_lower = roi_gray[h // 2:, :]  # Lower half of the face
    roi_color_lower = roi_color[h // 2:, :]

    # Detect smiles within the lower half of the face
    smiles = smile_cascade.detectMultiScale(
        roi_gray_lower,
        scaleFactor=1.8,  # Adjusted for better accuracy
        minNeighbors=30,  # Higher value to reduce false positives
        minSize=(25, 25)  # Minimum size of the detected smile
    )
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color_lower, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)  # Red rectangle for smiles

# Show the result
cv2.imshow('Face, Eye and Smile Detection', image)
cv2.imwrite('face_eye_smile_detected.jpg', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
