import streamlit as st
import ffmpeg
import shutil
import PIL
import os
from zipfile import ZipFile
from PIL import Image

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

# delete files
def delete_files(path):

    # check if file or directory exists
    if os.path.isfile(path) or os.path.islink(path):
        
        # remove file
        os.remove(path)

    elif os.path.isdir(path):

        # remove directory and all its content
        shutil.rmtree(path)

# upload the file
def file_upload(content):

    data = []

    for item in content:

        data.append(item.name)

        with open(item.name, "wb") as f:

            f.write(item.getbuffer())

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

# conversion section
def image_menu(images, selection):

    if selection == "Convert":

        # create a form to capture URL and take user options
        with st.form("input image convert", clear_on_submit=True):

            selection_image = st.radio('Into:', ('JPEG', 'PNG', 'BMP', 'TIFF', 'WEBP'), label_visibility="visible", horizontal=True)

            confirm_image_convert = st.form_submit_button("Submit")

        info_box()

        if confirm_image_convert:

            data_names = file_upload(images)

            results = image_conversion(data_names, selection_image)

            file_download(results)

            # removing files
            for count, f in enumerate(results):

                delete_files(f)
                delete_files(data_names[count])

            delete_files(f"switchy.zip")

    elif selection_type == "Compress":

        # create a form to capture URL and take user options
        with st.form("input image compress", clear_on_submit=True):

            quality_image = st.slider("Quality:", 0, 100, 80)

            confirm_image_compress = st.form_submit_button("Submit")

        info_box()

        if confirm_image_compress:

            data_names = file_upload(images)

            results = image_compression(data_names, quality_image)

            file_download(results)

            # removing files
            for count, f in enumerate(results):

                delete_files(f)
                delete_files(data_names[count])

            delete_files(f"switchy.zip")

# conversion section
def video_menu(videos, selection):

    if selection == "Convert":

        # create a form to capture URL and take user options
        with st.form("input video convert", clear_on_submit=True):

            selection_video = st.radio('Into:', ('MP4', 'AVI', 'MKV', 'MOV', 'WEBM'), label_visibility="visible", horizontal=True)

            confirm_video_convert= st.form_submit_button("Submit")

        info_box()

        if confirm_video_convert:

            file_upload(videos)

    elif selection == "Compress":

        # create a form to capture URL and take user options
        with st.form("input video compress", clear_on_submit=True):

            quality_video = st.slider("Quality:", 0, 100, 80)

            confirm_video_compress = st.form_submit_button("Submit")

        info_box()

        if confirm_video_compress:

            st.write("yes")

# conversion section
def audio_menu(audio, selection):

    if selection == "Convert":

        # create a form to capture URL and take user options
        with st.form("input audio convert", clear_on_submit=True):

            selection_audio = st.radio('Into:', ('MP3', 'WAV', 'OGG', 'AAC', 'FLAC'), label_visibility="visible", horizontal=True)

            confirm_audio_convert = st.form_submit_button("Submit")

        info_box()

        if confirm_audio_convert:

            file_upload(audio)

    elif selection == "Compress":

        # create a form to capture URL and take user options
        with st.form("input audio compress", clear_on_submit=True):

            quality_audio = st.slider("Quality:", 0, 100, 80)

            confirm_audio_compress = st.form_submit_button("Submit")

        info_box()

        if confirm_audio_compress:

            st.write("yes")

# conversion section
def docs_menu(docs):

    # create a form to capture URL and take user options
    with st.form("input doc convert", clear_on_submit=True):

        selection_settings = st.radio('Into:', ('PDF', 'DOCX', 'ODT', 'RTF'), label_visibility="visible", horizontal=True)

        confirm_docs = st.form_submit_button("Submit")

    info_box()

    if confirm_docs:

        file_upload(docs)

# image convert
def image_conversion(images, target_type):

    image_results = []

    for count, item in enumerate(images):

        if target_type == "JPEG":

            raw = Image.open(item)
            image = raw.convert('RGB')

        else:
            
            image = Image.open(item)

        image.save(f"new-image-{count}.{target_type}", target_type)
        image_results.append(f"new-image-{count}.{target_type}")

    return image_results

# image compression
def image_compression(images, quality):

    return False

# image convert
def video_conversion(videos, target_type):
    
    return

# image compression
def video_compression(videos, quality):

    return

# image convert
def audio_conversion(audio, target_type):
    
    return

# image compression
def audio_compression(audio, quality):

    return

# image convert
def docs_conversion(docs, target_type):
    
    return

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

# start script
if __name__ == "__main__":

    try:
        
        # image upload
        with tab1:

            images = st.file_uploader("upload image:", accept_multiple_files=True, type=['jpeg', 'jpg', 'png', 'bmp', 'tiff', 'tif', 'webp'], label_visibility="collapsed")

            selection_type = st.selectbox('image', ('Convert', 'Compress'), label_visibility="collapsed")

            image_menu(images, selection_type)

        # video upload
        with tab2:

            videos =  st.file_uploader("upload video:", accept_multiple_files=True, type=['mp4', 'avi', 'mkv', 'mov', 'webm'], label_visibility="collapsed")

            selection_type = st.selectbox('video', ('Convert', 'Compress'), label_visibility="collapsed")

            video_menu(videos, selection_type)
            
        # audio upload
        with tab3:

            audio = st.file_uploader("upload audio:", accept_multiple_files=True, type=['mp3', 'wav', 'ogg', 'aac', 'flac'], label_visibility="collapsed")

            selection_type = st.selectbox('audio', ('Convert', 'Compress'), label_visibility="collapsed")

            audio_menu(audio, selection_type)

        # document upload
        with tab4:

            docs = st.file_uploader("upload doc:", accept_multiple_files=True, type=['pdf', 'docx', 'odt', 'rtf'], label_visibility="collapsed")

            selection_type = st.selectbox('doc', ('Convert',), label_visibility="collapsed")

            docs_menu(docs)

    # pain
    except Exception as e:
                st.error(e, icon="💔")