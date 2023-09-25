# Downloading video with yt-dlp

`yt-dlp` is a command line tool that allows you to very easily download almost any video from the web.

> NOTE: as of the time of writing, `yt-dlp` seems to be the best and most maintained video downloader. This may change! If it's not working, try `youtube-dl` or `youtube-dlc`.

## Installation

`yt-dlp` is written in Python. To install it run:

```
pip3 install yt-dlp
```

## Basic usage

To download a video, just type `yt-dlp` and the URL of the video you want. This will work for YouTube, Vimeo, Twitter and _hundreds_ of other websites. For example, if we want to download some highlights from the nightmarish Metaverse announcement video, it's as easy as:

```bash
yt-dlp "https://www.youtube.com/watch?v=gElfIo6uw4g"
```

_Note: I've surrounded the video URL in quotes to avoid problems that can occur if the URL contains special characters. This isn't always necessary, but I usually do it anyway._

You can also download an entire user, channel, playlist, or search query. For example this will download the entire White House channel (it will take a long time).

```bash
yt-dlp "https://www.youtube.com/user/whitehouse/"
```

And this will download videos matching the search query "capitalism:"

```bash
yt-dlp "https://www.youtube.com/results?search_query=capitalism"
```

You can pretty much give yt-dlp any URL on YouTube, or any other video site.


## File formats

Websites like youtube and vimeo will store videos in multiple file formats and sizes. To get a list of all of them for a video, simply add the `-F` option:

```
yt-dlp [URL] -F
```
 
You can choose a specific format with `-f` and the code for that format

```
yt-dlp [URL] -f 22
```

Some formats let you download only the video, or only the audio.


## Change the output

By default yt-dlp will automatically select a filename to save to. To override this, add the `-o` flag.

```  
yt-dlp [URL] -o whatever.mp4
```    


## Always save mp4s

If you always want to save a file as an mp4, add the `--merge-output-format` option:

```    
yt-dlp [URL] --merge-output-format mp4
``` 

## Updating

Always be sure that your version of yt-dlp is updated. To keep it fresh, use pip's update command  (the `-U`):

```
pip3 install -U yt-dlp
```