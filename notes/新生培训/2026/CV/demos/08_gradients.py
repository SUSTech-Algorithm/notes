"""对比 Sobel 水平/垂直梯度、梯度幅值与 Canny 边缘。"""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


IMAGE_PATH = Path(__file__).resolve().parent.parent / "images" / "Lenna.jpg"


def normalize_for_display(image):
    """将浮点结果线性归一化到 0~255，仅用于显示。"""
    return cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)


def main():
    image_bgr = cv2.imread(str(IMAGE_PATH))
    if image_bgr is None:
        raise FileNotFoundError(f"无法读取图像：{IMAGE_PATH}")

    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    smoothed = cv2.GaussianBlur(gray, (5, 5), sigmaX=1.2)

    gradient_x = cv2.Sobel(smoothed, cv2.CV_32F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(smoothed, cv2.CV_32F, 0, 1, ksize=3)
    magnitude = cv2.magnitude(gradient_x, gradient_y)
    canny = cv2.Canny(smoothed, threshold1=60, threshold2=140)

    panels = [
        (image_rgb, "Original", None),
        (gray, "Grayscale", "gray"),
        (np.abs(gradient_x), "|Sobel Gx|: vertical edges", "gray"),
        (np.abs(gradient_y), "|Sobel Gy|: horizontal edges", "gray"),
        (normalize_for_display(magnitude), "Gradient magnitude", "gray"),
        (canny, "Canny edges", "gray"),
    ]

    figure, axes = plt.subplots(2, 3, figsize=(12, 8))
    for axis, (panel, title, color_map) in zip(axes.flat, panels):
        axis.imshow(panel, cmap=color_map)
        axis.set_title(title)
        axis.axis("off")

    print(f"Gx range: [{gradient_x.min():.1f}, {gradient_x.max():.1f}]")
    print(f"Gy range: [{gradient_y.min():.1f}, {gradient_y.max():.1f}]")
    print("注意：梯度有正负方向，显示时取了绝对值。")

    figure.suptitle("From image gradients to edges")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
