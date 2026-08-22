"""演示图像的 NumPy 数组结构、坐标顺序和像素值。"""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt


IMAGE_PATH = Path(__file__).resolve().parent.parent / "images" / "Lenna.jpg"


def main():
    image_bgr = cv2.imread(str(IMAGE_PATH))
    if image_bgr is None:
        raise FileNotFoundError(f"无法读取图像：{IMAGE_PATH}")

    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    height, width, channels = image_rgb.shape
    x, y = width // 2, height // 2
    pixel = image_rgb[y, x]

    print(f"shape: {image_rgb.shape}  # (height, width, channels)")
    print(f"dtype: {image_rgb.dtype}")
    print(f"value range: [{image_rgb.min()}, {image_rgb.max()}]")
    print(f"pixel coordinate (x, y): ({x}, {y})")
    print(f"image[y, x]: {pixel}  # [R, G, B]")

    radius = 6
    crop = image_rgb[y - radius : y + radius, x - radius : x + radius]

    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    axes[0].imshow(image_rgb)
    axes[0].scatter(x, y, c="yellow", marker="x", s=100, linewidths=2)
    axes[0].set_title(f"Image: H={height}, W={width}, C={channels}")
    axes[0].axis("off")

    axes[1].imshow(crop, interpolation="nearest")
    axes[1].set_title("12 x 12 pixel crop")
    axes[1].set_xticks([position - 0.5 for position in range(crop.shape[1] + 1)], minor=True)
    axes[1].set_yticks([position - 0.5 for position in range(crop.shape[0] + 1)], minor=True)
    axes[1].grid(which="minor", color="white", linewidth=0.7)
    axes[1].tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)

    fig.suptitle(f"Selected RGB pixel = {pixel.tolist()}")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
