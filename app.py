import streamlit as st
import ffmpeg
import shutil
import pathlib
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
            This website was made using Python, you can view the source [here](https://github.com/dylnbk/switchy).

            Convert & compress single/batches of images, videos & audio.
            
            To show support, you can ☕ [buy me a coffee](https://www.buymeacoffee.com/dylnbk).
            """)

        st.write("***")

        st.write("""
            ##### Image
            - Convert to popular image formats.
            - Compress by reducing colour depth & image quality.
            """)
        
        st.write("***")

        st.write("""
            ##### Video
            - Convert to popular video formats.
            - Compress to greatly reduce file size - can take quite a while.
            """)

        st.write("***")

        st.write("""
            ##### Audio
            - Convert to popular audio formats.
            - Compress by reducing sample rate & bit rate.
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

    # initialize a list to store file names
    data = []

    # iterate over the files that have been uploaded
    for item in content:

        # append file name to the list
        data.append(item.name)

        # write the file from memory in to the system
        with open(item.name, "wb") as f:

            f.write(item.getbuffer())

    # return the list of file names
    return data

# zip and download
def file_download(filenames):

    # create a ZipFile object
    with ZipFile(f"switchy.zip", 'w') as zipObj:

        for f in filenames:

            # Add file to zip
            zipObj.write(f)
    
    # create download button for the zip file
    with open("switchy.zip", "rb") as file:
        st.download_button("Download", data=file, file_name="switchy.zip", mime="zip")

# conversion section
def image_menu(images, selection):

    # if the user wants to convert
    if selection == "Convert":

        # create a form to capture URL and take user options
        with st.form("input image convert", clear_on_submit=True):

            # offer a checkbox selection
            selection_image = st.radio('Into:', ('JPEG', 'PNG', 'BMP', 'TIFF', 'WEBP'), label_visibility="visible", horizontal=True)
            
            # submit button
            confirm_image_convert = st.form_submit_button("Submit")

        # generate the info box - used here for layout purposes
        info_box()

        # if the user hits submit
        if confirm_image_convert:

            # start visual spinner
            with st.spinner(''):

                # upload the files and store the file names
                data_names = file_upload(images)

                # call conversion func, store return value
                results = image_conversion(data_names, selection_image)

                # send the converted files to the dowload func
                file_download(results)

                # removing files
                for count, f in enumerate(results):

                    delete_files(f)
                    delete_files(data_names[count])

                # remove the zip file
                delete_files(f"switchy.zip")

    elif selection_type == "Compress":

        # create a form to capture URL and take user options
        with st.form("input image compress", clear_on_submit=True):

            quality_image = st.slider("Quality:", 0, 100, 100)

            confirm_image_compress = st.form_submit_button("Submit")

        info_box()

        if confirm_image_compress:

            with st.spinner(''):

                data_names = file_upload(images)

                results = image_compression(data_names, quality_image)

                if results:

                    file_download(results)

                    # removing files
                    for count, f in enumerate(results):

                        delete_files(f)
                        delete_files(data_names[count])

                    delete_files(f"switchy.zip")

# conversion section
def video_menu(videos, selection):

    # if the user wants to convert
    if selection == "Convert":

        # create a form to capture URL and take user options
        with st.form("input video convert", clear_on_submit=True):

            # offer a checkbox selection
            selection_video = st.radio('Into:', ('MP4', 'AVI', 'MKV', 'MOV', 'WEBM'), label_visibility="visible", horizontal=True)

            # submit button
            confirm_video_convert= st.form_submit_button("Submit")

        # generate the info box - here for layout purposes
        info_box()

        # if the user hits submit
        if confirm_video_convert:

            # start visual spinner
            with st.spinner(''):
                
                # upload the files and store the file names
                data_names = file_upload(videos)

                # call conversion func, store return value
                results = video_conversion(data_names, selection_video)

                # send the converted files to the dowload func
                file_download(results)

                # removing files
                for count, f in enumerate(results):

                    delete_files(f)
                    delete_files(data_names[count])

                # remove the zip file
                delete_files(f"switchy.zip")

    # if the user wants to compress
    elif selection == "Compress":

        # create a form to capture URL and take user options
        with st.form("input video compress", clear_on_submit=True):

            # ffmpeg compression method - lower number = higher quality
            quality_video = 35 - round(st.slider("Quality:", 0, 100, 100) / 20)

            # submit button
            confirm_video_compress = st.form_submit_button("Submit")

        # generate the info box - here for layout purposes
        info_box()

        # if the user hits submit
        if confirm_video_compress:

            # start visual spinner
            with st.spinner(''):

                # upload the files and store the file names
                data_names = file_upload(videos)

                # call compression func, store return value
                results = video_compression(data_names, quality_video)

                # send the converted files to the dowload func
                file_download(results)

                # removing files
                for count, f in enumerate(results):

                    delete_files(f)
                    delete_files(data_names[count])

                # remove the zip file
                delete_files(f"switchy.zip")

# conversion section
def audio_menu(audio, selection):

    # if the user wants to covert
    if selection == "Convert":

        # create a form to capture URL and take user options
        with st.form("input audio convert", clear_on_submit=True):

            # offer a checkbox selection
            selection_audio = st.radio('Into:', ('MP3', 'M4A', 'WAV', 'OGG', 'FLAC'), label_visibility="visible", horizontal=True)

            # submit button
            confirm_audio_convert = st.form_submit_button("Submit")

        # generate the info box - here for layout purposes
        info_box()

        # if the user hits submit
        if confirm_audio_convert:

            # start visual spinner
            with st.spinner(''):

                # upload the files
                data_names = file_upload(audio)

                # call conversion func, store return value
                results = audio_conversion(data_names, selection_audio)

                # send the converted files to the dowload func
                file_download(results)

                # removing files
                for count, f in enumerate(results):
                    
                    delete_files(f)
                    delete_files(data_names[count])

                # remove the zip file
                delete_files(f"switchy.zip")
    
    # if the user wants to compress
    elif selection == "Compress":

        # create a form to capture URL and take user options
        with st.form("input audio compress", clear_on_submit=True):

            # ffmpeg compression method - lower number = higher quality
            quality_audio = 10 - st.slider("Quality:", 0, 100, 100) / 10

            # submit button
            confirm_audio_compress = st.form_submit_button("Submit")

        # generate the info box - here for layout purposes
        info_box()

        # if the user hits submit
        if confirm_audio_compress:

            # start visual spinner
            with st.spinner(''):

                # upload the files and store the file names
                data_names = file_upload(audio)

                # call compression func, store return value
                results = audio_compression(data_names, quality_audio)
                
                # send the compressed files to the dowload func
                file_download(results)

                # removing files
                for count, f in enumerate(results):
                    
                    delete_files(f)
                    delete_files(data_names[count])

                # remove the zip file
                delete_files(f"switchy.zip")

# image convert
def image_conversion(images, target_type):

    # initialize list for the completed file info
    image_results = []

    # iterate over uploaded files
    for count, item in enumerate(images):

        if target_type == "JPEG":

            # open the image
            raw = Image.open(item)

            # convert to RGB
            image = raw.convert('RGB')

        else:
            
            # open the image
            image = Image.open(item)

        # save it as a new file format
        image.save(f"new-image-{count}.{target_type}", target_type)

        # append the file name to the results list
        image_results.append(f"new-image-{count}.{target_type}")

    # return the results
    return image_results

# image compression
def image_compression(images, quality):

    # initialize list for the completed file info
    image_results = []

    # iterate over uploaded files
    for count, item in enumerate(images):

        # load the image with PIL
        image = Image.open(item)

        # get the file format and force it uppercase
        target_type = image.format.upper()
       
        if target_type == "JPEG" or target_type == "JPG":
            
            # if jpeg convert to RGB mode
            image = image.convert(mode='RGB', palette=Image.ADAPTIVE)
            
        else:
            
            # compress by reducing colours, good for lossless formats
            image = image.quantize(method=2)
        
        if target_type == "TIF" or target_type == "TIFF":

                # if tiff save using optimize only
                image.save(f"new-image-{count}.{target_type}", optimize=True) 

                # append the file name to the results list
                image_results.append(f"new-image-{count}.{target_type}")

        else:

            # save using optimize and quality reduction
            image.save(f"new-image-{count}.{target_type}", optimize=True, quality=quality) 

            # append the file name to the results list
            image_results.append(f"new-image-{count}.{target_type}")
    
    # return the results
    return image_results

# image convert
def video_conversion(videos, target_type):
    
    # initialize list for the completed file info
    video_results = []

    # iterate over uploaded files
    for count, item in enumerate(videos):

        # convert the file with ffmpeg
        ffmpeg.input(item).output(f"new-video-{count}.{target_type}").run()

        # append the file name to the results list
        video_results.append(f"new-video-{count}.{target_type}")

    # return the results
    return video_results

# image compression
def video_compression(videos, quality):

    # initialize list for the completed file info
    video_results = []

    # iterate over uploaded files
    for count, item in enumerate(videos):

        # get the file format extension
        target_type = pathlib.Path(item).suffix

        # compress the file
        ffmpeg.input(item).output(f"new-video-{count}{target_type}", vcodec='libx265', preset='fast', crf=quality).run()

        # append the file name to the results list
        video_results.append(f"new-video-{count}{target_type}")

    # return the results
    return video_results

# image convert
def audio_conversion(audio, target_type):
    
    # initialize list for the completed file info
    audio_results = []

    # iterate over uploaded files
    for count, item in enumerate(audio):
        
        # convert the file with ffmpeg, for lossy formats try min bitrate of 320kpbs
        ffmpeg.input(item).output(f"new-audio-{count}.{target_type}", audio_bitrate=320000).run()

        # append the file name to the results list
        audio_results.append(f"new-audio-{count}.{target_type}")

    return audio_results

# image compression
def audio_compression(audio, quality):

    # initialize sample rate variable
    sample_rate = 0

    # initialize list for the completed file info
    audio_results = []

    # higher = lower quality. drop sample rate by max amount
    if quality > 7:

        sample_rate = 22050

    # medium quality
    elif quality > 5 and quality <= 7:

        sample_rate = 32000

    # highest quality, lowest compression
    else:

        sample_rate = 37800

    # iterate over uploaded files
    for count, item in enumerate(audio):

        # get the file format extension
        target_type = pathlib.Path(item).suffix

        # compress the file
        ffmpeg.input(item).output(f"new-audio-{count}{target_type}", aq=quality, ar=sample_rate).run()

        # append the file name to the results list
        audio_results.append(f"new-audio-{count}{target_type}")

    # return the results
    return audio_results

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
tab1, tab2, tab3 = st.tabs(["Image", "Video", "Audio"])

# start script
if __name__ == "__main__":

    try:
        
        # image upload
        with tab1:

            # upload function, stores media in variable as a file-like object
            images = st.file_uploader("upload image:", accept_multiple_files=True, label_visibility="collapsed")

            # drop down menu options
            selection_type = st.selectbox('image', ('Convert', 'Compress'), label_visibility="collapsed")

            # call menu function, pass the media and compression/conversion choice
            image_menu(images, selection_type)

        # video upload
        with tab2:

            # upload function, stores media in variable as a file-like object
            videos =  st.file_uploader("upload video:", accept_multiple_files=True, label_visibility="collapsed")
            
            # drop down menu options
            selection_type = st.selectbox('video', ('Convert', 'Compress'), label_visibility="collapsed")

            # call menu function, pass the media and compression/conversion choice
            video_menu(videos, selection_type)
            
        # audio upload
        with tab3:

            # upload function, stores media in variable as a file-like object
            audio = st.file_uploader("upload audio:", accept_multiple_files=True, label_visibility="collapsed")

            # drop down menu options
            selection_type = st.selectbox('audio', ('Convert', 'Compress'), label_visibility="collapsed")

            # call menu function, pass the media and compression/conversion choice
            audio_menu(audio, selection_type)

    # pain
    except Exception as e:
                st.error("Something went wrong...", icon="💔")