"""演示固定阈值与 Otsu 自动阈值二值化。"""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


IMAGE_PATH = Path(__file__).resolve().parent.parent / "images" / "Lenna.jpg"


def main():
    image_bgr = cv2.imread(str(IMAGE_PATH))
    if image_bgr is None:
        raise FileNotFoundError(f"无法读取图像：{IMAGE_PATH}")

    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    thresholds = [70, 120, 170]
    fixed_results = [cv2.threshold(gray, value, 255, cv2.THRESH_BINARY)[1] for value in thresholds]
    otsu_threshold, binary_otsu = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    print(f"fixed thresholds: {thresholds}")
    print(f"Otsu threshold: {otsu_threshold:.0f}")
    print(f"binary values: {np.unique(binary_otsu)}")

    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes[0, 0].imshow(gray, cmap="gray", vmin=0, vmax=255)
    axes[0, 0].set_title("Grayscale")

    axes[0, 1].hist(gray.ravel(), bins=256, range=(0, 256), color="black")
    axes[0, 1].axvline(otsu_threshold, color="red", label=f"Otsu T={otsu_threshold:.0f}")
    axes[0, 1].set_title("Grayscale histogram")
    axes[0, 1].legend()

    axes[0, 2].imshow(binary_otsu, cmap="gray", vmin=0, vmax=255)
    axes[0, 2].set_title("Otsu binary image")

    for axis, threshold, binary in zip(axes[1], thresholds, fixed_results):
        axis.imshow(binary, cmap="gray", vmin=0, vmax=255)
        axis.set_title(f"Fixed threshold = {threshold}")

    for axis in axes.flat:
        if axis is not axes[0, 1]:
            axis.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
