import streamlit as st
import requests
from PIL import Image


class Web:
    def __init__(self):
        st.set_page_config(page_title="Lab")

        self.model = self.input_model()
        self.file = self.main_page()
        self.inference()

    def input_model(self):
        model = st.radio("Choose model", API.keys())
        return model

    def predict(self, data):
        response = requests.post(API[self.model], headers=headers, data=data)
        return response.json()

    def inference(self):
        c1, c2 = st.columns(2)
        if self.file is not None:
            output = self.predict(self.file.read())
            im = Image.open(self.file)
            c1.image(im, caption="Uploaded image", use_column_width=True)
            c2.write(output)
            st.balloons()

    def main_page(self):
        st.title("Object detection")
        st.header("Input an image")
        return st.file_uploader('', type=['png', 'jpg', 'jpeg'])


headers = {"Authorization": "Bearer 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"}
API = {
    'efficientnet-b7': "https://api-inference.huggingface.co/models/google/efficientnet-b7",
    'resnet-18': "https://api-inference.huggingface.co/models/microsoft/resnet-18",
    'super_duper_model': 'https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large'
}

if __name__ == '__main__':
    Web()
