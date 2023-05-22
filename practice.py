from google.cloud import vision
from google.oauth2 import service_account
 
IMG_URL = "https://imageslabo.com/wp-content/uploads/2019/05/553_dog_chihuahua_7203-973x721.jpg"
 
# 身元証明書のjson読み込み
credentials = service_account.Credentials.from_service_account_file('practice-386113-856eb9cbc15b.json')
 
client = vision.ImageAnnotatorClient(credentials=credentials)
image = vision.Image()
image.source.image_uri = IMG_URL
 
response = client.label_detection(image=image)
labels = response.label_annotations
 
 
for label in labels:
    print(label.description + ":" + str(label.score))
 
if response.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(
            response.error.message))






    