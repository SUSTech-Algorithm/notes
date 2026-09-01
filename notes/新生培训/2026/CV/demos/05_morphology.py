"""交互比较二值图像的腐蚀、膨胀、开运算与闭运算。"""

import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np


def create_noisy_mask():
    """生成同时包含噪点、小孔、裂缝和细小结构的二值图。"""
    mask = np.zeros((260, 420), dtype=np.uint8)

    cv2.rectangle(mask, (55, 55), (180, 205), 255, thickness=-1)
    cv2.circle(mask, (300, 130), 75, 255, thickness=-1)

    # 在前景中制造小孔和裂缝。
    cv2.circle(mask, (105, 105), 3, 0, thickness=-1)
    cv2.circle(mask, (315, 145), 4, 0, thickness=-1)
    cv2.line(mask, (180, 130), (225, 130), 255, thickness=5)
    cv2.line(mask, (294, 55), (294, 88), 0, thickness=4)

    # 添加孤立白色噪点。
    noise_points = [(24, 35), (40, 225), (205, 40), (230, 220), (380, 35), (395, 230)]
    for x, y in noise_points:
        cv2.circle(mask, (x, y), 2, 255, thickness=-1)

    return mask


def apply_operations(mask, kernel_size, iterations):
    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (kernel_size, kernel_size)
    )
    eroded = cv2.erode(mask, kernel, iterations=iterations)
    dilated = cv2.dilate(mask, kernel, iterations=iterations)
    opened = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel, iterations=iterations
    )
    closed = cv2.morphologyEx(
        mask, cv2.MORPH_CLOSE, kernel, iterations=iterations
    )
    return eroded, dilated, opened, closed


def main():
    mask = create_noisy_mask()
    initial_kernel_size = 7
    initial_iterations = 1

    figure, axes = plt.subplots(1, 5, figsize=(16, 4.6))
    plt.subplots_adjust(bottom=0.24, wspace=0.08)

    titles = ["Original mask", "Erosion", "Dilation", "Opening", "Closing"]
    images = [mask, *apply_operations(mask, initial_kernel_size, initial_iterations)]
    artists = []

    for axis, title, image in zip(axes, titles, images):
        artist = axis.imshow(image, cmap="gray", vmin=0, vmax=255)
        axis.set_title(title)
        axis.axis("off")
        artists.append(artist)

    kernel_axis = figure.add_axes((0.18, 0.12, 0.64, 0.035))
    iteration_axis = figure.add_axes((0.18, 0.06, 0.64, 0.035))
    kernel_slider = Slider(
        kernel_axis,
        "Kernel size",
        3,
        15,
        valinit=initial_kernel_size,
        valstep=2,
    )
    iteration_slider = Slider(
        iteration_axis,
        "Iterations",
        1,
        4,
        valinit=initial_iterations,
        valstep=1,
    )

    def update(_):
        kernel_size = int(kernel_slider.val)
        iterations = int(iteration_slider.val)
        results = apply_operations(mask, kernel_size, iterations)
        for artist, result in zip(artists[1:], results):
            artist.set_data(result)
        figure.canvas.draw_idle()

    kernel_slider.on_changed(update)
    iteration_slider.on_changed(update)

    print("约定：白色为前景，黑色为背景。")
    print("拖动滑块，观察结构元素过大或迭代过多时目标如何被破坏。")
    figure.suptitle("Binary morphology: the same local rule, four different effects")
    plt.show()


if __name__ == "__main__":
    main()
