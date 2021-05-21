import cv2                                
import numpy as np                                 
import pyrealsense2 as rs                
import PIL.Image
import os



# 配置
pipe = rs.pipeline()
cfg = rs.config()
cfg.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30) # 可設width height，最後一個是 frame rate

i = 40
  
profile=pipe.start(cfg)
  
while True:
    # 获取图片帧
    frameset = pipe.wait_for_frames()
    color_frame = frameset.get_color_frame()
    color_img = np.asanyarray(color_frame.get_data())
    
    #更改通道的顺序为RGB
    b, g, r = cv2.split(color_img)
    img2 = cv2.merge([r, g, b])

    cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('RealSense', img2)
    k=cv2.waitKey(1)
    #Esc退出，
    if k==27:
        cv2.destroyAllWindows()
        break
    #输入空格保存图片
    elif k == ord(' '):
        i = i + 1
        PIL.Image.fromarray(color_img).save(os.path.join("/home/itriq200/realsense_folder/data_process/collect_picture/picture_data",str(i)+'.png'))
        print("Frames{} Captured".format(i))

pipe.stop()