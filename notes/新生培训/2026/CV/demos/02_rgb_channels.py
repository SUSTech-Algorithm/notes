"""演示 RGB 彩色图像的三个通道。"""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


IMAGE_PATH = Path(__file__).resolve().parent.parent / "images" / "Lenna.jpg"


def main():
    image_bgr = cv2.imread(str(IMAGE_PATH))
    if image_bgr is None:
        raise FileNotFoundError(f"无法读取图像：{IMAGE_PATH}")

    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    red, green, blue = cv2.split(image_rgb)
    zeros = np.zeros_like(red)

    red_only = np.dstack((red, zeros, zeros))
    green_only = np.dstack((zeros, green, zeros))
    blue_only = np.dstack((zeros, zeros, blue))

    print(f"RGB image shape: {image_rgb.shape}")
    print(f"single channel shape: {red.shape}")
    print("OpenCV imread order is BGR; the image was converted to RGB for Matplotlib.")

    fig, axes = plt.subplots(2, 2, figsize=(9, 9))
    panels = [
        (image_rgb, "RGB = R + G + B"),
        (red_only, "Red channel"),
        (green_only, "Green channel"),
        (blue_only, "Blue channel"),
    ]

    for axis, (panel, title) in zip(axes.flat, panels):
        axis.imshow(panel)
        axis.set_title(title)
        axis.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
