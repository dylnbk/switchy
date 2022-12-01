import streamlit as st
import ffmpeg
from zipfile import ZipFile

# load & inject style sheet
def local_css(file_name):

    # write <style> tags to allow custom css
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# generate the see info box
def info_box():

    # create an info box
    with st.expander("See info"):

        st.write("### Thanks for visiting Switchy!")

        st.write("""
            This website was made using Python, you can view the source [here](https://github.com/dylnbk/chat-bot).
            
            To show support, you can ☕ [buy me a coffee](https://www.buymeacoffee.com/dylnbk).
            """)

        st.write("***")

        st.write("""
            ##### asdfasdfs
            - gfdagsfdsaf
            """)
        
        st.write("***")

        st.write("""
            ##### sdfasdf
            - fdsfasdf
            """)

        st.write("***")

        st.write("""
            ##### fdsfd
            - sdfsdfsdf
            - asdfsadfasdfasd
            """)

        st.write("")
        st.write("")

# upload the file
def file_upload():

    data = []

    for image in images:

        data.append(image.name)

        with open(image.name, "wb") as f:

            f.write(image.getbuffer())

    return data

# zip and download
def file_download(filenames):

    # create a ZipFile object
    with ZipFile(f"switchy.zip", 'w') as zipObj:

        for f in filenames:

            # Add file to zip
            zipObj.write(f)
        
    with open("switchy.zip", "rb") as file:
        st.download_button("Download", data=file, file_name="switchy.zip", mime="zip")

# image convert
def image_conversion(target_type):

    return False

# image compression
def image_compression():

    return False

# main VISUAL ELEMENTS BEGIN HERE <<----------------------------------------------------------------------------||

# burger menu config
st.set_page_config(
    page_title="Change it.",
    page_icon="⚙️",
    menu_items={
        'Report a bug': "mailto:dyln.bk@gmail.com",
        'Get help': None,
        'About': "Made by dyln.bk"
    }
)

# inject css
local_css("style.css")

# page title
st.title('Change it.')

# define tabs
tab1, tab2, tab3, tab4 = st.tabs(["Image", "Video", "Audio", "Docs"])

# image upload
with tab1:

    images = st.file_uploader("upload image:", accept_multiple_files=True, type=['jpeg', 'jpg', 'png','avif', 'tiff', 'tif', 'webp'], label_visibility="collapsed")

    selection_type = st.selectbox('image', ('Convert', 'Compress'), label_visibility="collapsed")

    if selection_type == "Convert":

        # create a form to capture URL and take user options
        with st.form("input image convert", clear_on_submit=True):

            selection_settings = st.radio('Into:', ('JPEG', 'PNG', 'AVIF', 'TIFF', 'WEBP'), label_visibility="visible", horizontal=True)

            confirm_image_convert = st.form_submit_button("Submit")

    elif selection_type == "Compress":

        # create a form to capture URL and take user options
        with st.form("input image compress", clear_on_submit=True):

            quality_image = st.slider("Quality:", 0, 100, 80)

            confirm_image_compress = st.form_submit_button("Submit")

    info_box()

# video upload
with tab2:

    videos =  st.file_uploader("upload video:", accept_multiple_files=True, type=['mp4', 'avi', 'mkv', 'mov', 'webm'], label_visibility="collapsed")

    selection_type = st.selectbox('video', ('Convert', 'Compress'), label_visibility="collapsed")

    if selection_type == "Convert":

        # create a form to capture URL and take user options
        with st.form("input video convert", clear_on_submit=True):

            selection_settings = st.radio('Into:', ('MP4', 'AVI', 'MKV', 'MOV', 'WEBM'), label_visibility="visible", horizontal=True)

            confirm_video_convert= st.form_submit_button("Submit")

    elif selection_type == "Compress":

        # create a form to capture URL and take user options
        with st.form("input video compress", clear_on_submit=True):

            quality_video = st.slider("Quality:", 0, 100, 80)

            confirm_video_compress = st.form_submit_button("Submit")

    info_box()

# audio upload
with tab3:

    audio = st.file_uploader("upload audio:", accept_multiple_files=True, type=['mp3', 'wav', 'ogg', 'aac', 'flac'], label_visibility="collapsed")

    selection_type = st.selectbox('audio', ('Convert', 'Compress'), label_visibility="collapsed")

    if selection_type == "Convert":

        # create a form to capture URL and take user options
        with st.form("input audio convert", clear_on_submit=True):

            selection_settings = st.radio('Into:', ('MP3', 'WAV', 'OGG', 'AAC', 'FLAC'), label_visibility="visible", horizontal=True)

            confirm_audio_convert = st.form_submit_button("Submit")

    elif selection_type == "Compress":

        # create a form to capture URL and take user options
        with st.form("input audio compress", clear_on_submit=True):

            quality_audio = st.slider("Quality:", 0, 100, 80)

            confirm_audio_compress = st.form_submit_button("Submit")

    info_box()

# document upload
with tab4:

    docs = st.file_uploader("upload doc:", accept_multiple_files=True, type=['pdf', 'docx', 'odt', 'rtf'], label_visibility="collapsed")

    selection_type = st.selectbox('doc', ('Convert',), label_visibility="collapsed")

    if selection_type == "Convert":

        # create a form to capture URL and take user options
        with st.form("input doc convert", clear_on_submit=True):

            selection_settings = st.radio('Into:', ('PDF', 'DOCX', 'ODT', 'RTF'), label_visibility="visible", horizontal=True)

            confirm_docs = st.form_submit_button("Submit")

    info_box()

# start script
if __name__ == "__main__":

    try:

        if confirm_image_convert:

            pass

        if confirm_image_compress:

            pass

        if confirm_video_convert:

            pass

        if confirm_video_compress:

            pass

        if confirm_audio_convert:

            pass

        if confirm_image_compress:

            pass

        if confirm_docs:

            pass
         
    # pain
    except Exception as e:
                st.error(e, icon="💔")