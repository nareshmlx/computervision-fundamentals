import cv2 as cv
import os

# ---------------------------
# 1. Setup
# ---------------------------
folder_path = "../../photos/faces/train/Madonna"
supported_formats = (".jpg", ".jpeg", ".png")

# List and numerically sort images
images = [file for file in os.listdir(folder_path) if file.lower().endswith(supported_formats)]
images.sort(key=lambda x: int(os.path.splitext(x)[0]))

print(images, f"\n\nNo of Images: {len(images)}")

# ---------------------------
# 2. Initialize index and window
# ---------------------------
index = 0
window_name = "Gallery"

cv.namedWindow(window_name, cv.WINDOW_NORMAL)  # allow resizing

# ---------------------------
# 3. Main loop
# ---------------------------
while True:
    img_path = os.path.join(folder_path, images[index])
    img = cv.imread(img_path)
    
    if img is None:
        print(f"Failed to load {img_path}")
        index = (index + 1) % len(images)
        continue

    # Resize to fit window
    img = cv.resize(img, (800, 600))

    # Display filename on image
    cv.putText(img, images[index], (20, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show image in the single window
    cv.imshow(window_name, img)

    # Wait for key press
    key = cv.waitKey(0) & 0xFF

    if key == ord('q'):
        break  # quit
    elif key == ord('d') or key == 83:
        index = (index + 1) % len(images)  # next image
    elif key == ord('a') or key == 81:
        index = (index - 1) % len(images)  # previous image

# ---------------------------
# 4. Cleanup
# ---------------------------
cv.destroyAllWindows()
