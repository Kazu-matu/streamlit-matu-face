import requests
import streamlit as st
from PIL import Image
from PIL import ImageDraw
import streamlit
import json
import io

# This key will serve all examples in this document.
subscription_key="bf2087b529b84a5eba7ea73e0a85208a"
# This endpoint will be used in all examples in this quickstart.
face_api_url = "https://20210322matu.cognitiveservices.azure.com/face/v1.0/detect"

headers = {
    'Content-Type':'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}


st.title('顔認証アプリ')
uploaded_file = st.file_uploader("Chose an image....",type='jpg')
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img,caption='Uploaded Image.',use_column_width=True)
    with io.BytesIO() as output:
        img.save(output,format='JPEG')
        binary_img = output.getvalue()


        res = requests.post(face_api_url, params=params,
                         headers=headers, data=binary_img)

        results = res.json()
        for result in results:
            rect =result['faceRectangle']

            draw = ImageDraw.Draw(img)
            draw.rectangle([(rect['left'],rect['top']),(rect['left']+rect['width']),(rect['top']+rect['height'])],fill=None,outline='green')
        st.image(img,caption='Uploaded Image.',use_column_width=True)