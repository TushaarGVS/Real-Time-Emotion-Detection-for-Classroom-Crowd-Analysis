import pygame
import os
import pygame.camera
import time
        
def capture_image():
    filename = "img" + time.strftime("-%m.%d.%y_%H.%M.%S") + ".jpg"
    path = "/home/tushaar/Desktop/code.fun.do/captures/images/" + filename
    
    pygame.camera.init()
    cam = pygame.camera.Camera("/dev/video0", (640, 640))
    cam.start()
    image = cam.get_image()
    pygame.image.save(image, path)

    return path
