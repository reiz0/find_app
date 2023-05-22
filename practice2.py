import cv2
import numpy as np
from PIL import Image
import pyocr


k = 3




picture.show()

# picture=Image.open(pil_image)
# picture = img
cv2.imshow("Image", img)

# OCRエンジンを取�?
engines = pyocr.get_available_tools()
engine = engines[0]

# 対応言語取�?
langs = engine.get_available_languages()
# print("�Ή�����:",langs) # ['eng', 'jpn', 'osd']

# 画像�?��?字を読み込む
txt = engine.image_to_string(picture, lang="jpn") # 修正点?��lang="eng" -> lang="jpn"

txt = txt.splitlines()

print(txt)