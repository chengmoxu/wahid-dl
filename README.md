# wahid-dl
Making video and audio download easily

### First. About
wahid-dl is a video and audio download tool based on yt-dlp, which supports Windows environment and Google Colab cloud environment respectively.
The name wahid-dl comes from Arabic واحد, the intention is to hope that this project is as accessible and easy to use as the number 1.

### Second. Applicable operating environment
* Windows
* Google Colab

### Third. Instructions for use
#### For Windows
1. Create folder "wahid-dl" in C:\
2. Copy "yt-dlp.exe", "ffmpeg.exe", "ffplay.exe" and "ffprobe.exe" below C:\wahid-dl
3. Choose the function which you want to use

*Notice: Please check for yt-dlp updates when prompted with an error message*

#### For Google Colab
1. Open the file wahid-dl.ipynb using button "Open in Colab"
2. Choose the function which you want to use

### Fourth.  Instructions for functions
#### For Windows
1. wahid-dl-wincmd.bat
> This package can download video.

2. wahid-dl-wincmd for Audio.bat
> This package can download audio.

3. wahid-dl-wincmd Format Checking Tool.bat
> Using this package to check the format of video or audio.

4. wahid-dl-wincmd Dev Mode.bat
> Using this package make yt-dlp command available in wahid-dl.

5. wahid-dl-wincmd Update Tool.bat
> The yt-dlp update function have been combined into wahid-dl-wincmd.bat, wahid-dl-wincmd for Audio.bat, wahid-dl-wincmd Format Checking Tool.bat and wahid-dl-wincmd Dev Mode.bat. Generally you don't need to using this package to update yt-dlp. 

### Fifth.  Future outlook
* Cookies support.
* Download list support.
* Specific websites download via aria2 support.
