"""
rescale.py
----------------
Helpers to rescale images and video frames. Exposes a small API-style
function `rescaleFrame` which works for both static images and video frames.

The module also contains an example video loop showing the original and
rescaled frames side-by-side.
"""

import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    """
    Rescale an image or video frame by a given scale factor.

    Args:
        frame (numpy.ndarray): source image or frame (HxWxC)
        scale (float): scaling factor, e.g. 0.5 for half size

    Returns:
        numpy.ndarray: resized frame

    Notes:
        This function does not check the type of `frame`. Callers should
        ensure `frame` is not None (e.g., after reading from a VideoCapture).
    """
    if frame is None:
        return None

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dsize=dimensions, interpolation=cv.INTER_AREA)


if __name__ == "__main__":
    # simple image example
    img = cv.imread("../photos/astinMartin.jpeg")
    if img is not None:
        rescaled_img = rescaleFrame(img, 0.2)
        cv.imshow("Astin Martin", rescaled_img)
        cv.imwrite("../photos/car_rescaled.jpeg", rescaled_img)
        cv.waitKey(0)

    # Video example
    def changeRes(capture, width, height):
        """
        Change resolution of a live/captured video stream (backend dependent).
        """
        capture.set(3, width)
        capture.set(4, height)

    capture = cv.VideoCapture("../videos/car.mp4")

    while True:
        isTrue, frame = capture.read()
        if not isTrue or frame is None:
            break

        rescaled_frame = rescaleFrame(frame)

        cv.imshow("Video", frame)
        if rescaled_frame is not None:
            cv.imshow("Video Resized", rescaled_frame)

        if cv.waitKey(20) & 0xFF == ord("q"):
            break

    capture.release()
    cv.destroyAllWindows()
