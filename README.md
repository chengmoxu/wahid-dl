# wahid-dl
Making video and audio download easily

Stable Version Number: 
* Windows: wahid-dl.v3.2.20240616.windows-cmd.1
> Now, wahid-dl v3.2 can be installed using the wahid-dl-wincmd Install.bat. Furthermore, the update function is capable of updating ffmpeg.

* Google Colab: wahid-dl.v2.2.20240225.googlecolab.1

### First. About
wahid-dl is a video and audio download tool based on yt-dlp, which supports Windows environment and Google Colab cloud environment respectively.
The name wahid-dl comes from Arabic واحد, the intention is to hope that this project is as accessible and easy to use as the number 1.

### Second. Applicable operating environment
* Windows
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
#### For Windows
1. wahid-dl-wincmd.bat
> This batch file can download video.

2. wahid-dl-wincmd Cookies Support
> Using this packagebatch file can download video using Cookies (Default = Chrome).

3. wahid-dl-wincmd for Audio.bat
> This batch file can download audio.

4. wahid-dl-wincmd Format Checking Tool.bat
> Using this batch file to check the format of video or audio.

5. wahid-dl-wincmd Dev Mode.bat
> Using this batch file make yt-dlp command available in wahid-dl.

6. wahid-dl-wincmd Update Tool.bat
> This batch file will download the file from GitHub to update the complete wahid-dl. Additionally, yt-dlp and ffmpeg will also be updated.

7. wahid-dl-wincmd Install.bat
> This batch file will download the file from GitHub to install the complete wahid-dl. Additionally, yt-dlp and ffmpeg will also be installed.

### Fifth.  Future outlook
* Download list support.
* Specific websites download via aria2 support.
