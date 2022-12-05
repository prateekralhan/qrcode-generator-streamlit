import qrcode
from datetime import datetime
from PIL import Image
import streamlit as st
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask

st.set_page_config(
    page_title="QR Code Generator",
    page_icon="💫",
    layout="centered",
    initial_sidebar_state="auto",
)

generated_qrcodes_path = "generated_qrcodes/"

def generate_qrcode(url):
    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=2
                        )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=HorizontalGradiantColorMask())

    current_ts = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    qrcode_path = generated_qrcodes_path + "qrcode_" + str(current_ts) + ".png"
    img.save(qrcode_path)
    return qrcode_path

main_image = Image.open('static/main_banner.png')

st.image(main_image,use_column_width='auto')
st.title("✨ QR Code Generator 🚀")
url = st.text_input("Enter your URL please 👇")
if url is not None and url != "":
    with st.spinner(f"Generating QR Code... 💫"):
        qrcode_path = generate_qrcode(str(url))

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        image = Image.open(qrcode_path)
        st.image(image, caption='Here\'s the Generated QR Code ✅')
    with col3:
        st.write(' ')

else:
    st.warning('⚠ Please enter your URL! 😯')


st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=QRCode Generator WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
