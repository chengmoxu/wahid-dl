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

* For Windows/Linux/macOS Version Number: v5.4-20241230.1
> feat: Call the new unified UI  
> feat: Improved version information display  
> style/fix: Removed old annotations/Removed old code  
 rename: Renamed wahid-dl Cookies Support to wahid-dl for Cookies Support  

* For Google Colab Version Number: wahid-dl-colab.v5.1.20240906.googlecolab.1
> fix: Fixed video wrong format issues  
> fix: Changed the yt-dlp installation method to avoid outdated versions  
> style: Description correction  
> feat: Added instructions to remove completed videos  

### First. About
wahid-dl is a video and audio download tool based on yt-dlp, which supports Windows environment and Google Colab cloud environment respectively.  
The name wahid-dl comes from Arabic واحد, the intention is to hope that this project is as accessible and easy to use as the number 1.  

### Second. Applicable operating environment
* Windows/Linux/macOS  
* Google Colab  

### Third. Instructions for use
#### For Windows and Linux
1. [Install or update wahid-dl, wahid-dl DEV, yt-flp or FFmpeg] Execute wahid-dl Tool.py  
2. [Using] Choose the function which you want to use

*Notice: Please check for yt-dlp updates when prompted with an error message*  
*Notice: Linux only supports some functions*  

#### For macOS
*Notice: macOS is not supported yet* 

#### For Google Colab
1. Open the file wahid-dl-colab.ipynb using button "Open in Colab"  
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

#### For Windows and Linux based on Python
1. wahid-dl Tool.py
> This function will download the file from GitHub to install or update the complete wahid-dl. Additionally, yt-dlp and ffmpeg will be, also.  
2. wahid-dl.py
> This function can download video.  
3. wahid-dl for Cookies Support.py
> Using this function can download video using Cookies (Default = Chrome).  
4. wahid-dl for Audio.py
> This function can download audio.  
5. wahid-dl Format Checking Tool.py
> Using this function to check the format of video or audio.  
6. wahid-dl Dev Mode.py
> Using this function make yt-dlp command available in wahid-dl.  
7. wahid-dl for Live.py
> Using this function can download live video.  
8. wahid-dl for List.py
> Using this function can download video using "url_list.txt".  
9. wahid-dl for Quality Selection.py
> Using this function to download videos with specified image quality.  
10. wahid-dl for Subtitle.py
> Using this function to download subtitle of videos.  
