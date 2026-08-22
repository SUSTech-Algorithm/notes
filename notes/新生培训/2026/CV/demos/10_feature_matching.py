"""使用 SIFT、比例检验和 RANSAC 演示两图特征匹配。"""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


IMAGE_PATH = Path(__file__).resolve().parent.parent / "images" / "Lenna.jpg"
RATIO_THRESHOLD = 0.75
MAX_DRAW_MATCHES = 60


def create_second_view(image):
    """通过透视变换生成同一平面的第二个视角。"""
    height, width = image.shape[:2]
    source = np.float32(
        [[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]]
    )
    destination = np.float32(
        [[28, 18], [width - 38, 3], [width - 8, height - 26], [12, height - 5]]
    )
    transform = cv2.getPerspectiveTransform(source, destination)
    second_view = cv2.warpPerspective(image, transform, (width, height))
    return second_view


def main():
    first_image = cv2.imread(str(IMAGE_PATH))
    if first_image is None:
        raise FileNotFoundError(f"无法读取图像：{IMAGE_PATH}")

    second_image = create_second_view(first_image)
    first_gray = cv2.cvtColor(first_image, cv2.COLOR_BGR2GRAY)
    second_gray = cv2.cvtColor(second_image, cv2.COLOR_BGR2GRAY)

    sift = cv2.SIFT_create(nfeatures=600)
    first_keypoints, first_descriptors = sift.detectAndCompute(first_gray, None)
    second_keypoints, second_descriptors = sift.detectAndCompute(second_gray, None)
    if first_descriptors is None or second_descriptors is None:
        raise RuntimeError("图像中没有找到足够的 SIFT 特征。")

    matcher = cv2.BFMatcher(cv2.NORM_L2)
    candidate_pairs = matcher.knnMatch(first_descriptors, second_descriptors, k=2)
    ratio_matches = [
        nearest
        for nearest, second_nearest in candidate_pairs
        if nearest.distance < RATIO_THRESHOLD * second_nearest.distance
    ]

    inlier_mask = np.zeros(len(ratio_matches), dtype=np.uint8)
    if len(ratio_matches) >= 4:
        first_points = np.float32(
            [first_keypoints[match.queryIdx].pt for match in ratio_matches]
        ).reshape(-1, 1, 2)
        second_points = np.float32(
            [second_keypoints[match.trainIdx].pt for match in ratio_matches]
        ).reshape(-1, 1, 2)
        _, mask = cv2.findHomography(first_points, second_points, cv2.RANSAC, 3.0)
        if mask is not None:
            inlier_mask = mask.ravel().astype(np.uint8)

    inlier_matches = [
        match for match, is_inlier in zip(ratio_matches, inlier_mask) if is_inlier
    ]
    inlier_matches.sort(key=lambda match: match.distance)
    displayed_matches = inlier_matches[:MAX_DRAW_MATCHES]

    match_view_bgr = cv2.drawMatches(
        first_image,
        first_keypoints,
        second_image,
        second_keypoints,
        displayed_matches,
        None,
        matchColor=(40, 220, 40),
        singlePointColor=(80, 80, 255),
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
    )
    match_view = cv2.cvtColor(match_view_bgr, cv2.COLOR_BGR2RGB)

    print(f"First-view keypoints: {len(first_keypoints)}")
    print(f"Second-view keypoints: {len(second_keypoints)}")
    print(f"Matches after ratio test: {len(ratio_matches)}")
    print(f"RANSAC inliers: {len(inlier_matches)}")

    plt.figure(figsize=(14, 7))
    plt.imshow(match_view)
    plt.title(
        f"SIFT matching: {len(ratio_matches)} ratio-test matches, "
        f"{len(inlier_matches)} RANSAC inliers"
    )
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
