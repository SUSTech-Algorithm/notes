"""交互演示针孔相机投影中焦距和物体深度的影响。"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480
PRINCIPAL_POINT = np.array([IMAGE_WIDTH / 2, IMAGE_HEIGHT / 2])

# 一个以原点为中心、边长为 1.6 的三维立方体。
CUBE = np.array(
    [
        [-0.8, -0.8, -0.8],
        [0.8, -0.8, -0.8],
        [0.8, 0.8, -0.8],
        [-0.8, 0.8, -0.8],
        [-0.8, -0.8, 0.8],
        [0.8, -0.8, 0.8],
        [0.8, 0.8, 0.8],
        [-0.8, 0.8, 0.8],
    ],
    dtype=float,
)

EDGES = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]


def project(points_3d, focal_length, object_depth):
    """使用 u=fx*X/Z+cx, v=fy*Y/Z+cy 进行针孔投影。"""
    camera_points = points_3d.copy()
    camera_points[:, 2] += object_depth

    normalized = camera_points[:, :2] / camera_points[:, 2:3]
    pixels = focal_length * normalized + PRINCIPAL_POINT
    return pixels, camera_points


def main():
    initial_focal_length = 500.0
    initial_depth = 5.0

    figure, axis = plt.subplots(figsize=(8, 7))
    plt.subplots_adjust(bottom=0.24)

    lines = [axis.plot([], [], color="#2563eb", linewidth=2)[0] for _ in EDGES]
    points = axis.scatter([], [], color="#ef4444", s=35, zorder=3)
    information = axis.text(
        0.02,
        0.98,
        "",
        transform=axis.transAxes,
        va="top",
        family="monospace",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.9},
    )

    axis.axvline(PRINCIPAL_POINT[0], color="#cbd5e1", linewidth=1, linestyle="--")
    axis.axhline(PRINCIPAL_POINT[1], color="#cbd5e1", linewidth=1, linestyle="--")
    axis.scatter(*PRINCIPAL_POINT, color="#f59e0b", marker="+", s=120, zorder=4)
    axis.text(
        PRINCIPAL_POINT[0] + 8,
        PRINCIPAL_POINT[1] - 8,
        "principal point",
        color="#b45309",
    )

    axis.set_xlim(0, IMAGE_WIDTH)
    axis.set_ylim(IMAGE_HEIGHT, 0)  # 像素坐标的 v 轴向下。
    axis.set_aspect("equal")
    axis.set_xlabel("u (pixels)")
    axis.set_ylabel("v (pixels)")
    axis.set_title("Pinhole projection of a 3D cube")
    axis.set_facecolor("#f8fafc")

    focal_axis = figure.add_axes([0.18, 0.12, 0.68, 0.035])
    depth_axis = figure.add_axes([0.18, 0.06, 0.68, 0.035])
    focal_slider = Slider(focal_axis, "focal length", 150.0, 900.0, valinit=initial_focal_length)
    depth_slider = Slider(depth_axis, "depth", 2.0, 12.0, valinit=initial_depth)

    def update(_=None):
        focal_length = focal_slider.val
        object_depth = depth_slider.val
        pixels, camera_points = project(CUBE, focal_length, object_depth)

        for line, (start, end) in zip(lines, EDGES):
            line.set_data(
                [pixels[start, 0], pixels[end, 0]],
                [pixels[start, 1], pixels[end, 1]],
            )

        points.set_offsets(pixels)
        information.set_text(
            f"f = {focal_length:.0f} px\n"
            f"cube center Z = {object_depth:.1f}\n"
            f"nearest Z = {camera_points[:, 2].min():.1f}"
        )
        figure.canvas.draw_idle()

    focal_slider.on_changed(update)
    depth_slider.on_changed(update)
    update()

    print("拖动 focal length 和 depth 滑块，观察三维立方体的二维投影。")
    print("黄色十字是主点 (cx, cy) = (320, 240)。")
    plt.show()


if __name__ == "__main__":
    main()
