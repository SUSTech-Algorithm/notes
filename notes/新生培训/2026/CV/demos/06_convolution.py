"""交互演示一个 3x3 核如何在 5x5 数值图像上滑动并计算输出。"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.widgets import Slider


IMAGE = np.array(
    [
        [10, 10, 10, 80, 80],
        [10, 10, 10, 80, 80],
        [10, 10, 10, 80, 80],
        [20, 20, 20, 90, 90],
        [20, 20, 20, 90, 90],
    ],
    dtype=float,
)

KERNEL = np.array(
    [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1],
    ],
    dtype=float,
)


def correlate_valid(image, kernel):
    """不填充、步长为 1 的滑动窗口运算。"""
    output_height = image.shape[0] - kernel.shape[0] + 1
    output_width = image.shape[1] - kernel.shape[1] + 1
    output = np.empty((output_height, output_width), dtype=float)

    for row in range(output_height):
        for column in range(output_width):
            patch = image[row : row + kernel.shape[0], column : column + kernel.shape[1]]
            output[row, column] = np.sum(patch * kernel)

    return output


def annotate_grid(axis, values):
    for row in range(values.shape[0]):
        for column in range(values.shape[1]):
            axis.text(
                column,
                row,
                f"{values[row, column]:.0f}",
                ha="center",
                va="center",
                color="black",
                fontsize=11,
            )
    axis.set_xticks(np.arange(-0.5, values.shape[1], 1), minor=True)
    axis.set_yticks(np.arange(-0.5, values.shape[0], 1), minor=True)
    axis.grid(which="minor", color="white", linewidth=2)
    axis.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)


def main():
    output = correlate_valid(IMAGE, KERNEL)
    output_width = output.shape[1]

    figure, axes = plt.subplots(1, 3, figsize=(12, 5))
    plt.subplots_adjust(bottom=0.22)

    axes[0].imshow(IMAGE, cmap="Blues", vmin=0, vmax=100)
    axes[0].set_title("5 x 5 input")
    annotate_grid(axes[0], IMAGE)

    axes[1].imshow(KERNEL, cmap="coolwarm", vmin=-1, vmax=1)
    axes[1].set_title("3 x 3 kernel")
    annotate_grid(axes[1], KERNEL)

    axes[2].imshow(output, cmap="Oranges", vmin=output.min(), vmax=output.max())
    axes[2].set_title("3 x 3 output")
    annotate_grid(axes[2], output)

    input_box = Rectangle((-0.5, -0.5), 3, 3, fill=False, edgecolor="#facc15", linewidth=4)
    output_box = Rectangle((-0.5, -0.5), 1, 1, fill=False, edgecolor="#ef4444", linewidth=4)
    axes[0].add_patch(input_box)
    axes[2].add_patch(output_box)

    formula = figure.text(0.5, 0.14, "", ha="center", family="monospace", fontsize=12)
    slider_axis = figure.add_axes([0.2, 0.06, 0.6, 0.035])
    position_slider = Slider(
        slider_axis,
        "window position",
        0,
        output.size - 1,
        valinit=0,
        valstep=1,
    )

    def update(_=None):
        position = int(position_slider.val)
        row, column = divmod(position, output_width)
        patch = IMAGE[row : row + 3, column : column + 3]
        products = patch * KERNEL

        input_box.set_xy((column - 0.5, row - 0.5))
        output_box.set_xy((column - 0.5, row - 0.5))
        formula.set_text(
            f"position ({row}, {column}): sum(patch x kernel) "
            f"= {products.sum():.0f}"
        )
        figure.canvas.draw_idle()

    position_slider.on_changed(update)
    update()

    print("Output:\n", output)
    print("拖动 window position 滑块，观察输入窗口与输出位置的对应关系。")
    plt.show()


if __name__ == "__main__":
    main()
