//사람인식
import cv2
import torch
import numpy as np

# YOLOv5 모델 로드하기
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

# COCO 클래스 이름 가져오기
COCO_INSTANCE_CATEGORY_NAMES = model.names

# 웹캠 연결하기
cap = cv2.VideoCapture(0)

while True:
    # 웹캠에서 프레임 가져오기
    _, frame = cap.read()

    # 객체 탐지 수행하기
    with torch.no_grad():
        results = model(frame, size=640)  # 이미지 크기는 필요에 따라 조정할 수 있습니다.

    # 탐지된 객체 출력하기
    for *xyxy, conf, label in results.xyxy[0]:
        # 클래스 이름이 'person'인 경우에 대해 처리하기
        if COCO_INSTANCE_CATEGORY_NAMES[int(label)] == "person" and conf > 0.5:
            x1, y1, x2, y2 = int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 화면에 출력하기
    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) == ord("q"):
        break

# 자원 해제하기
cap.release()
cv2.destroyAllWindows()