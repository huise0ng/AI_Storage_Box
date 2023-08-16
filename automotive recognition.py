import cv2
import torch
import torchvision

COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
    'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite',
    'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake',
    'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop',
    'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink',
    'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    frame_tensor = torch.from_numpy(frame).permute(2, 0, 1).float() / 255.0
    frame_tensor = frame_tensor.unsqueeze(0)

    with torch.no_grad():
        detections = model(frame_tensor)[0]

    if 'labels' in detections and 'boxes' in detections:
        for i, label in enumerate(detections['labels']):
            # 레이블이 올바른 범위 내에 있는지 확인
            if 0 <= label < len(COCO_INSTANCE_CATEGORY_NAMES):
                if detections['scores'][i] >= 0.5 and COCO_INSTANCE_CATEGORY_NAMES[label] == 'car':
                    x, y, w, h = detections['boxes'][i]
                    cv2.rectangle(frame, (int(x), int(y)), (int(w), int(h)), (0, 0, 255), 2)
                    print(1)

    cv2.imshow('Car Detection', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()