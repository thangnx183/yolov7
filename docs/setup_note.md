# setup note
- clone repo 
```
    git clone https://github.com/thangnx183/yolov7.git
```

- checkout setup branch
```
    git checkout feat/MCAI-407-review-and-setup
```
- setup docker container
```
    nvidia-docker run --name yolov7 -it -v /datadrive_01/data/:/yolov7/coco/ -v /datadrive_01/coco_stuff:/yolov7/coco_stuff -v /datadrive_01/thang/yolov7/:/yolov7  --shm-size=64g -p 1000:1000 -p 1001:1001 nvcr.io/nvidia/pytorch:21.08-py3
```
- generate coco-stuff yolo format data from coco data in [coco-to-yolo.py](../coco-to-yolo.py) file
- merge 2 training files together in [concat_2_train_files.py](../concat_2_train_files.py) file