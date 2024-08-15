# wahid-dl
```
      ###       ###        ###         ###     ###         #######      ########             #########       ###
     ###       ###      ###   ##      ###     ###         ###          ###    ###           ###    ###      ###
    ###       ###     ###    ##      ###     ###         ###          ###    ###           ###    ###      ###
   >>>  >>>  >>>    >>>>>>>>>>>     >>>>>>>>>>>         >>>          >>>    >>>   >>>>>   >>>    >>>      >>>
  ### ##  # ###    ###      ##     ###     ###         ###          ###    ###           ###    ###      ###
 #####    ###     ###      ##     ###     ###         ###          ###    ###           ###    ###      ###
####      ##     ###      ##     ###     ###     #######          #########            #########       ###
```
Making video and audio download easily

* For Windows/Linux/macOS Version Number: wahid-dl.v4.4.20240815
> Now, wahid-dl v4.0 has been refactored with Python, significantly enhancing code extensibility. Additionally, the installation and update functionalities, also based on Python, have been consolidated into a single .py file. New features include support for live video downloads and the url_list.txt file.

* For Google Colab Version Number: wahid-dl.v2.2.20240225.googlecolab.1
> Fixed video wrong format issues. 
>
> Change the yt-dlp installation method to avoid outdated versions. 
>
> Added instructions to remove completed videos. 
>
> Description correction. 

### First. About
wahid-dl is a video and audio download tool based on yt-dlp, which supports Windows environment and Google Colab cloud environment respectively.
The name wahid-dl comes from Arabic واحد, the intention is to hope that this project is as accessible and easy to use as the number 1.

### Second. Applicable operating environment
* Windows/Linux/macOS
* Google Colab

### Third. Instructions for use
#### For Windows
1. [Installation] Execute wahid-dl-wincmd Install.bat
2. [Using] Choose the function which you want to use

*Notice: Please check for yt-dlp updates when prompted with an error message*

#### For Google Colab
1. Open the file wahid-dl.ipynb using button "Open in Colab"
2. Choose the function which you want to use

### Fourth.  Instructions for functions
#### For Windows based on batchfile
1. wahid-dl-wincmd.bat
> This batch file can download video.

2. wahid-dl-wincmd Cookies Support
> Using this file can download video using Cookies (Default = Chrome).

3. wahid-dl-wincmd for Audio.bat
> This batchfile can download audio.

4. wahid-dl-wincmd Format Checking Tool.bat
> Using this batchfile to check the format of video or audio.

5. wahid-dl-wincmd Dev Mode.bat
> Using this batchfile make yt-dlp command available in wahid-dl.

6. wahid-dl-wincmd Update Tool.bat
> This batchfile will download the file from GitHub to update the complete wahid-dl. Additionally, yt-dlp and ffmpeg will also be updated.

7. wahid-dl-wincmd Install.bat
> This batchfile will download the file from GitHub to install the complete wahid-dl. Additionally, yt-dlp and ffmpeg will also be installed.

#### For Windows based on Python
1. wahid-dl-python-based.py
> This function can download video.

2. wahid-dl-python-based Cookies Support.py
> Using this function can download video using Cookies (Default = Chrome).

3. wahid-dl-python-based for Audio.py
> This function can download audio.

4. wahid-dl-python-based Format Checking Tool.py
> Using this function to check the format of video or audio.

5. wahid-dl-python-based Dev Mode.py
> Using this function make yt-dlp command available in wahid-dl.

6. wahid-dl-python-based for Live.py
> Using this function can download live video.

7. wahid-dl-python-based for List.py
> Using this function can download video using "url_list.txt".

8. wahid-dl-python-based for Quality Selection.py
> Using this function to download videos with specified image quality.

9. wahid-dl-python-based for Subtitle.py
> Using this function to download subtitle of videos.

10. wahid-dl-python-based Install and Update Tool.py
> This function will download the file from GitHub to install or update the complete wahid-dl. Additionally, yt-dlp and ffmpeg will be, also.

### Fifth.  Future outlook
* Specific websites download via aria2 support.
