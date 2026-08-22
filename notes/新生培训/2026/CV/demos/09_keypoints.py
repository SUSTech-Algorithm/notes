"""在同一张图像上对比 Harris 角点与 SIFT 关键点。"""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


IMAGE_PATH = Path(__file__).resolve().parent.parent / "images" / "Lenna.jpg"
MAX_KEYPOINTS = 120


def main():
    image_bgr = cv2.imread(str(IMAGE_PATH))
    if image_bgr is None:
        raise FileNotFoundError(f"无法读取图像：{IMAGE_PATH}")

    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    harris_corners = cv2.goodFeaturesToTrack(
        gray,
        maxCorners=MAX_KEYPOINTS,
        qualityLevel=0.01,
        minDistance=7,
        blockSize=3,
        useHarrisDetector=True,
        k=0.04,
    )
    harris_view = image_rgb.copy()
    if harris_corners is not None:
        for x, y in np.round(harris_corners[:, 0]).astype(int):
            cv2.circle(harris_view, (x, y), 3, (255, 40, 40), thickness=-1)

    sift = cv2.SIFT_create(nfeatures=MAX_KEYPOINTS)
    sift_keypoints, descriptors = sift.detectAndCompute(gray, None)
    sift_view_bgr = cv2.drawKeypoints(
        image_bgr,
        sift_keypoints,
        None,
        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
    )
    sift_view = cv2.cvtColor(sift_view_bgr, cv2.COLOR_BGR2RGB)

    print(f"Harris corners: {0 if harris_corners is None else len(harris_corners)}")
    print(f"SIFT keypoints: {len(sift_keypoints)}")
    print(f"SIFT descriptor shape: {None if descriptors is None else descriptors.shape}")

    figure, axes = plt.subplots(1, 3, figsize=(14, 5))
    panels = [
        (image_rgb, "Original image"),
        (harris_view, "Harris corners"),
        (sift_view, "SIFT keypoints: scale and orientation"),
    ]
    for axis, (panel, title) in zip(axes, panels):
        axis.imshow(panel)
        axis.set_title(title)
        axis.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
