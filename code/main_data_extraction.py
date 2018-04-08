import glob
import os
import cv2

import organize_dataset as od
import remove_multiple_neutrals as rmn
import extract_faces as ef

od.segregate_files()
rmn.remove_neutrals()
ef.extract_faces()
