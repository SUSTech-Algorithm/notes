"""对比平均、高斯、中值和锐化滤波的效果。"""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


IMAGE_PATH = Path(__file__).resolve().parent.parent / "images" / "Lenna.jpg"


def add_noise(image, seed=7):
    """加入少量高斯噪声和椒盐噪声，便于对比滤波效果。"""
    generator = np.random.default_rng(seed)
    noisy = image.astype(np.float32)
    noisy += generator.normal(0, 12, image.shape)
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)

    salt_and_pepper = generator.random(image.shape[:2])
    noisy[salt_and_pepper < 0.008] = 0
    noisy[salt_and_pepper > 0.992] = 255
    return noisy


def main():
    image_bgr = cv2.imread(str(IMAGE_PATH))
    if image_bgr is None:
        raise FileNotFoundError(f"无法读取图像：{IMAGE_PATH}")

    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    noisy = add_noise(image_rgb)

    mean_filtered = cv2.blur(noisy, (5, 5))
    gaussian_filtered = cv2.GaussianBlur(noisy, (5, 5), sigmaX=1.2)
    median_filtered = cv2.medianBlur(noisy, 5)

    sharpen_kernel = np.array(
        [[0, -1, 0], [-1, 5, -1], [0, -1, 0]],
        dtype=np.float32,
    )
    sharpened = cv2.filter2D(image_rgb, ddepth=-1, kernel=sharpen_kernel)

    panels = [
        (image_rgb, "Original"),
        (noisy, "Added noise"),
        (mean_filtered, "Mean filter 5x5"),
        (gaussian_filtered, "Gaussian filter 5x5"),
        (median_filtered, "Median filter 5x5"),
        (sharpened, "Sharpening"),
    ]

    figure, axes = plt.subplots(2, 3, figsize=(12, 8))
    for axis, (panel, title) in zip(axes.flat, panels):
        axis.imshow(panel)
        axis.set_title(title)
        axis.axis("off")

    figure.suptitle("Different filters preserve and remove different information")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
