"""演示 RGB 图像的平均灰度化、加权灰度化和 OpenCV 灰度化。"""

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

    gray_average = np.mean(image_rgb, axis=2).astype(np.uint8)
    gray_weighted = np.rint(0.299 * red + 0.587 * green + 0.114 * blue).astype(np.uint8)
    gray_opencv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

    difference = cv2.absdiff(gray_weighted, gray_opencv)
    print(f"RGB shape: {image_rgb.shape}")
    print(f"grayscale shape: {gray_opencv.shape}")
    print(f"maximum difference between formula and OpenCV: {difference.max()}")

    fig, axes = plt.subplots(1, 4, figsize=(15, 4))
    panels = [
        (image_rgb, "RGB image", None),
        (gray_average, "Simple average", "gray"),
        (gray_weighted, "Weighted: 0.299R + 0.587G + 0.114B", "gray"),
        (gray_opencv, "OpenCV grayscale", "gray"),
    ]

    for axis, (panel, title, color_map) in zip(axes, panels):
        axis.imshow(panel, cmap=color_map, vmin=0 if color_map else None, vmax=255 if color_map else None)
        axis.set_title(title)
        axis.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
