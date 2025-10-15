| Property ID | Constant Name                       | Description                                        |
| ----------- | ----------------------------------- | -------------------------------------------------- |
| `0`         | `cv2.CAP_PROP_POS_MSEC`             | Current position of the video file in milliseconds |
| `1`         | `cv2.CAP_PROP_POS_FRAMES`           | 0-based index of the next frame to be read         |
| `2`         | `cv2.CAP_PROP_POS_AVI_RATIO`        | Relative position of the video: 0=start, 1=end     |
| `3`         | `cv2.CAP_PROP_FRAME_WIDTH`          | Width of the frames in the video stream            |
| `4`         | `cv2.CAP_PROP_FRAME_HEIGHT`         | Height of the frames in the video stream           |
| `5`         | `cv2.CAP_PROP_FPS`                  | Frame rate (frames per second)                     |
| `6`         | `cv2.CAP_PROP_FOURCC`               | 4-character code of codec (e.g., MJPG)             |
| `7`         | `cv2.CAP_PROP_FRAME_COUNT`          | Total number of frames in the video file           |
| `8`         | `cv2.CAP_PROP_FORMAT`               | Format of the `Mat` object (like depth)            |
| `9`         | `cv2.CAP_PROP_MODE`                 | Backend-specific value (not usually used)          |
| `10`        | `cv2.CAP_PROP_BRIGHTNESS`           | Brightness of the image (only for cameras)         |
| `11`        | `cv2.CAP_PROP_CONTRAST`             | Contrast of the image                              |
| `12`        | `cv2.CAP_PROP_SATURATION`           | Saturation of the image                            |
| `13`        | `cv2.CAP_PROP_HUE`                  | Hue of the image                                   |
| `14`        | `cv2.CAP_PROP_GAIN`                 | Gain of the camera                                 |
| `15`        | `cv2.CAP_PROP_EXPOSURE`             | Exposure (usually in log base 2 seconds)           |
| `16`        | `cv2.CAP_PROP_CONVERT_RGB`          | Boolean: convert image to RGB or not               |
| `17`        | `cv2.CAP_PROP_WHITE_BALANCE_BLUE_U` | White balance (may vary by camera driver)          |
| `18`        | `cv2.CAP_PROP_RECTIFICATION`        | Used for stereo cameras (rectification flag)       |

