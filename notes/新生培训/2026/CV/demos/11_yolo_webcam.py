"""使用 Ultralytics YOLO 对摄像头、图片或视频进行目标检测。"""

import argparse
from pathlib import Path

import cv2


LOCAL_MODEL_PATH = Path(__file__).resolve().parent.parent / "yolo26n.pt"


def parse_source(value):
    """将 0、1 等纯数字参数解析为摄像头编号，其余保留为文件路径。"""
    return int(value) if value.isdigit() else value


def build_argument_parser():
    parser = argparse.ArgumentParser(description="YOLO real-time object detection demo")
    parser.add_argument(
        "--source",
        default="0",
        help="camera index, image path, or video path (default: 0)",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Ultralytics model name or local weight path (default: bundled yolo26n.pt)",
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.35,
        help="confidence threshold (default: 0.35)",
    )
    return parser


def detect_image(model, image_path, confidence):
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"无法读取图像：{image_path}")

    result = model.predict(image, conf=confidence, verbose=False)[0]
    annotated = result.plot()
    cv2.imshow("YOLO detection - press any key to close", annotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_stream(model, source, confidence):
    capture = cv2.VideoCapture(source)
    if not capture.isOpened():
        raise RuntimeError(f"无法打开摄像头或视频：{source}")

    print("按 Q 或 Esc 退出。")
    try:
        while True:
            ok, frame = capture.read()
            if not ok:
                break

            result = model.predict(frame, conf=confidence, verbose=False)[0]
            annotated = result.plot()
            cv2.imshow("YOLO detection", annotated)

            key = cv2.waitKey(1) & 0xFF
            if key in (ord("q"), ord("Q"), 27):
                break
    finally:
        capture.release()
        cv2.destroyAllWindows()


def main():
    try:
        from ultralytics import YOLO
    except ImportError as error:
        raise SystemExit(
            "未安装 ultralytics，请先运行：python3 -m pip install ultralytics"
        ) from error

    arguments = build_argument_parser().parse_args()
    source = parse_source(arguments.source)
    model_source = arguments.model
    if model_source is None:
        model_source = str(LOCAL_MODEL_PATH) if LOCAL_MODEL_PATH.is_file() else "yolo26n.pt"
    model = YOLO(model_source)

    if isinstance(source, str) and Path(source).suffix.lower() in {
        ".bmp", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"
    }:
        detect_image(model, Path(source), arguments.conf)
    else:
        detect_stream(model, source, arguments.conf)


if __name__ == "__main__":
    main()
