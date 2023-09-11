# Infinite Video @ SFPC, Fall 2023

**Instructor:** [Sam Lavigne](https://lav.io) | [splavigne@gmail.com](mailto:splavigne@gmail.com)  
**Assistant Teachers:** [Ilona Brand](https://theilonabrand.com/) & [Jonathan Gray](https://jonathangray.org/)  
**Location:** Online  
**Time:** Tuesdays 6pm to 9pm & Wednesdays 10am to 1pm (NY time)  
**Office Hours:** By appointment  

## Description

How can code and automation help us see and manipulate large collections of videos in new ways? What do novel approaches in machine learning help make evident? On the flip side, what do these same approaches prevent us from seeing? What do they obscure? How can automated "content generation" be leveraged for political, poetic, and critical ends?

In this experimental video art class students will explore the possibilities (and limitations) of using Python, command line tools, and machine learning models as a means to critically analyze, filter, sort, edit, and compose video.

We will look at historic and contemporary examples of artists and activists working with video archives, with a focus on the political dimensions of experimental filmmaking. Students may bring their own video archives to work with, or use material we collect online. The class will conclude with a public screening of student work.

## Assignments

At the start of the course, you'll select a video corpus that you'd like to work with throughout the ten weeks (you can, of course, change this at any time). Each week we'll cover a new technique for programmatically editing, composing, or analyzing video. The assignments are meant to be short exercises to familiarize yourself with the tools, and to apply them to your corpus of material. Outputs should be short and experimental rather than completely realized works. Every week a few people will share what they've made.

The last 3-4 weeks of the class you'll work on a longer project with an open brief. If you choose, you can also just work on this throughout the course and *ignore* the weekly assignments. It's up to you!

In either case, every week there will be an opportunity for a few students to share what they made with the rest of the class. 

## Schedule

### Week 1: Orientation

- Meet the participants, setting up your computer, intro to the command line (time-permitting)


#### Readings 

- Archive Fever: Photography Between History and the Monument by Okwui Enwezor
- Radical Software Volume I "Presentation"
- Beyond Noblesse Oblige by Rick Prelinger


#### Assignment - Archive (due week 2):

Find a collection of video material to work with. This could be something that you don't currently have access to. It could also be material that you've produced yourself. Share it with the class. Why are you interested in this archive? What does it say or reveal? What does it omit or exclude? If possible, bring a short clip to share in class (no more than 3 minutes) that highlights some of the qualities of the archive that you find interesting.

---

### Week 2: Basic tools

- Assistant teacher presentations
- The command line, downloading material with yt-dlp, playing video with VLC & MPV, manipulating video with FFmpeg


#### Readings

- The Cutup Method
- Glitch Studies Manifesto
- Busting the Tube: A Brief History of Video Art


#### Assignment - Supercut (due week 3):

Create a composition using just FFmpeg. Feel free to use [FFmpeg Explorer](https://ffmpeg.lav.io), or the command line if you prefer. Experiment with running the same FFmpeg command on different source material.

---

### Week 3: Spoken word

- Videogrep, natural language processing


#### Readings

- [On the Dangers of Stochastic Parrots by Emily Bender et all](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)
- [Language models can only write poetry by Allison Parrish](https://posts.decontextualize.com/language-models-poetry/)
- [A Genealogy of Distant Reading](http://www.digitalhumanities.org/dhq/vol/11/2/000317/000317.html)


#### Assignment - Language (due week 4):

Create a supercut using Videogrep. Feel free to experiment with natural language processing techniques using spacCy if you'd like.

---

### Week 4: Editing video with code

- Moviepy, vidpy


#### Readings

- When Film and Database Collide by Perry Bard
- Always Already Just


#### Assignment - Procedural composition (due week 5):

Create a composition using MoviePy or VidPy. Experiment with order, randomness, layout, transitions, juxtaposition, and text.

---


### Week 5: Object detection

- Splitting a video into shots, analyzing the content of shots


#### Readings

- In Defense of the Poor Image
- [AI Is a Lot of Work](https://www.theverge.com/features/23764584/ai-artificial-intelligence-data-notation-labor-scale-surge-remotasks-openai-chatbots)


#### Assignment - Subject composition (due week 6):

Create a composition that selects for particular visual subject matter.

---


### Week 6: Classification

- Using classifiers, training classifiers, zero-shot classifiers

#### Readings

- The Syrian Archive by Jeff Deutch and Hadi Habal
- Data Activism and Meta Documentary in Six Films by Forensic Architecture

#### Assignment - Classification (due week 7):

Use an existing classifier, or train a new one to identify content in your video material.

---


### Week 7: Camera motion

- Pans, tilts, and zooms


#### Readings

- TBD

#### Assignment - Final project:

For the rest of the class, you should work on a single project. It's completely up to you what you make.

---

### Week 8: Work time

- Individual meetings

---

### Week 9: Work time

- Small group crits

---

### Week 10: Final presentations

- Share your work!

---

### Week 11: Screening

- We'll conclude with a screening of student work from both sections, data TBD.

---


## Technical Resources

### General

- [Command line tutorial (by me)](https://scrapism.lav.io/intro-to-the-command-line/)
- [UNIX tutorial for beginners](http://www.ee.surrey.ac.uk/Teaching/Unix/)
- [Python basics tutorial (by me)](https://scrapism.lav.io/intro-to-python/)
- [Learn Python](https://www.learnpython.org/) - a free and reasonably good python book
- [Hugging Face](https://huggingface.co/) - a huge collection of machine learning models that you can use


### Video
- [FFmpeg](https://ffmpeg.org/): command-line multimedia manipulator
    - [FFmpeg Explorer](https://ffmpeg.lav.io/) - visual tool to explore FFmpeg and generate commands
    - [FFmpeg.app](https://ffmpeg.app/) - good FFmpeg examples
    - [ffmprovisr](https://amiaopensource.github.io/ffmprovisr/) - many basic ffmpeg commands
    - [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) - python library for ffmpeg
- [OpenCV](https://opencv.org/) - computer vision library
- [MoviePy](https://zulko.github.io/moviepy/) - Python library for editing video
- [VidPy](https://antiboredom.github.io/vidpy/) - Another Python library for editing video
- [Videogrep](https://github.com/antiboredom/videogrep)
    - [Videogrep tutorial](https://lav.io/notes/videogrep-tutorial/)
    - [Videogrep & NLP tutorial](https://lav.io/notes/videogrep-and-spacy/)
- [VLC](https://www.videolan.org/vlc/) - video player
- [MPV](https://mpv.io/) - another video player
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - command line tool to download video from almost any website

### Audio
- [pydub](https://github.com/jiaaro/pydub) - Python library for editing audio
- [sox tutorial](https://madskjeldgaard.dk/posts/sox-tutorial-cli-tape-music/) - tutorial for working with Sox, a command-line audio editor
- [Paulstretch](https://github.com/ojczeo/paulstretch_python) - Python tool for making audio super slow

### Language
- [spaCy](https://spacy.io/) - a great natural language processing library
    - [Advanced NLP with spaCy](https://course.spacy.io/en/)


## Some Artists, Archives & Inspiration

- [Nam June Paik](https://americanart.si.edu/artist/nam-june-paik-3670)
- [Soda Jerk](https://sodajerk.info/): [Hello Dankness](https://www.hellodankness.net/)
- [Arthur Jafa](https://en.wikipedia.org/wiki/Arthur_Jafa): [LOVE IS THE MESSAGE, THE MESSAGE IS DEATH](https://www.youtube.com/watch?v=lKWmx0JNmqY)
- [Hannah Black: My Bodies](https://fourthree.boilerroom.tv/film/hannah-black-my-bodies-2014)
- [Christian Marclay: The Clock](https://www.tate.org.uk/whats-on/tate-modern/christian-marclay-clock)
- [Aarati Akkapeddi](https://aarati.online/)
- [Rodell Warner: Augmented Archive](https://www.rodellwarner.com/Augmented-Archive)
- [Nao Bustamante: Rosa Does Joan](https://www.youtube.com/watch?v=TaD1faxcmJo)
- [Crackhead Barney](https://www.youtube.com/channel/UCepzS80JI8P5Lz6eYD0i4aA)
- [Kameron Neal: Down the Barrel (of a Lens)](https://www.broadwayworld.com/article/NYC-Department-of-Records-Public-Artist-in-Residence-Kameron-Neal-Debuts-Film-Installation-DOWN-THE-BARREL-OF-A-LENS-20230614)
- [John Akomfrah: The Last Angel of History](https://www.youtube.com/watch?v=xca3VqHt5Xk)
- [The Prelinger Archives](https://archive.org/details/prelinger)
- [Adam Harvey: Exposing AI](https://exposing.ai/)
- [Syrian Archive](https://syrianarchive.org/)
- [Forensic Architecture](https://forensic-architecture.org/)
- [Everest Pipkin: Default Filename TV](https://default-filename-tv.neocities.org/)
- [Andrew Normal Wilson: ScanOps](http://www.andrewnormanwilson.com/ScanOps.html)
- [Liz Magic Laser](https://www.lizmagiclaser.com/)
- [Neta Bomani: Dark matter objects](https://netabomani.com/darkmatter/)
- [James Bridle: The Distractor](https://jamesbridle.com/works/the-distractor)
- [Total Refusal: Red Redemption](https://totalrefusal.com/home/red-redemption)
- [Bruce Connor: Crossroads](https://www.tomatazos.com/videos/468893/Crossroads-1976-Documental)
- [Josh Begley](http://joshbegley.com/)
- [Emily Jacir: Ramallah/New York](https://www.moma.org/collection/works/110909)
- [Mimi Onuoha: Machine Sees More than it Says](https://mimionuoha.com/machine-sees-more-than-it-says)
- [Addie Wagenknecht and Pablo Garcia: brbxoxo](https://www.pablogarcia.org/brbxoxo)
- [Natalie Bookchin: Mass Ornament](https://bookchin.net/projects/mass-ornament/)
- [Gretchen Bender](https://spruethmagers.com/artists/gretchen-bender/)
- [Disnovation: The Pirate Cinema](https://disnovation.org/piratecinema.php)
- [Jeff Thompson: Computers on Law & Order](https://computersonlawandorder.tumblr.com/)
- [Monoskop Video Art Archive](https://monoskop.org/Video_art)
- [Big list of digital artists working with archives](http://collectheworld.linkartcenter.eu/)



