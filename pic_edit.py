import cv2
import numpy as np
from PIL import Image
import pyocr

k = 3
def make_sharp_kernel(k: int):
  return np.array([
    [-k / 9, -k / 9, -k / 9],
    [-k / 9, 1 + 8 * k / 9, k / 9],
    [-k / 9, -k / 9, -k / 9]
  ], np.float32)

def pic_edi(pct):

  img = cv2.imread(pct)
  #画像の読み込み(OpenCVで画像処理を行うために使う関数)

  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  #グレースケール化

  ret, img_thr = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
  #二値化

  kernel = make_sharp_kernel(k)
  img = cv2.filter2D(img_thr, -1, kernel).astype("uint8")
  #鮮鋭化


  picture = Image.fromarray(img)
  return picture

pict = pic_edi(input())

pict.show()