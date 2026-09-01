"""演示 OpenCV 中彩色图像的 BGR 数组结构及三个颜色通道。"""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


IMAGE_PATH = Path(__file__).resolve().parent.parent / "images" / "Lenna.jpg"


def main():
    image_bgr = cv2.imread(str(IMAGE_PATH))
    if image_bgr is None:
        raise FileNotFoundError(f"无法读取图像：{IMAGE_PATH}")

    # OpenCV 读入的数组按 B、G、R 排列；Matplotlib 显示时需要 RGB。
    blue, green, red = cv2.split(image_bgr)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    zeros = np.zeros_like(red)

    red_only = np.dstack((red, zeros, zeros))
    green_only = np.dstack((zeros, green, zeros))
    blue_only = np.dstack((zeros, zeros, blue))

    height, width = image_bgr.shape[:2]
    x, y = width // 2, height // 2
    pixel_bgr = image_bgr[y, x]
    pixel_rgb = image_rgb[y, x]

    print(f"Python type: {type(image_bgr)}")
    print(f"OpenCV image shape: {image_bgr.shape}  # (height, width, channels)")
    print(f"OpenCV image dtype: {image_bgr.dtype}")
    print("\nOpenCV image array ([B, G, R] per pixel):")
    print(image_bgr)
    print(f"image_bgr[y, x] at ({x}, {y}): {pixel_bgr}  # [B, G, R]")
    print(f"image_rgb[y, x] at ({x}, {y}): {pixel_rgb}  # [R, G, B]")
    print(f"single channel shape: {red.shape}")
    print("注意：直接把 BGR 数组交给 Matplotlib，红色和蓝色会被交换。")

    fig, axes = plt.subplots(2, 2, figsize=(9, 9))
    panels = [
        (image_rgb, "RGB = R + G + B"),
        (red_only, "Red channel"),
        (green_only, "Green channel"),
        (blue_only, "Blue channel"),
    ]

    for axis, (panel, title) in zip(axes.flat, panels):
        axis.set_title(title)
        axis.axis("off")
        axis.imshow(panel)

    # 在彩色图上标出终端中单独打印的像素。
    axes[0, 0].plot(
        x,
        y,
        marker="o",
        markersize=8,
        markerfacecolor="none",
        markeredgecolor="yellow",
        markeredgewidth=2,
    )

    fig.suptitle("How OpenCV stores a color image")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
