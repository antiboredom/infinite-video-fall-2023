# Captioning and labeling scenes with Hugging Face

We can use machine learning to automatically caption or label scenes in a video. There are a number of ways to do this, but we'll be using a resource called [Hugging Face](https://huggingface.co/) which is a repository of pre-trained machine learning models.

To get started, first install the requirements:

```bash
pip install transformers
pip install torch
pip install Pillow
```

HuggingFace provides a ton of different machine learning models that you can use in your Python code. It can be a bit overwhelming. Here we'll look at two kinds of models. One that classifies images, and  another that captions images.

## Classifying or labeling images

Lets start with an image classifier, which attempts to produce a "class" or label for an image. Please note that we are using pre-trained models, which means that the number of classes/labels available are already determined. We'll talk in another class about how to train your own models.

To use Hugging Face models, we import the `pipeline` method. We then provide it with the type of machine learning task we are doing, and the name of a model to run. 

```python

from transformers import pipeline
from PIL import Image

MODEL = "google/vit-base-patch16-224"

labeler = pipeline("image-classification", model=MODEL)

img = Image.open("myimage.jpg")
results = labeler(img)
print(results)

```

Here we are opening a sample image, and then passing it the `labeler` function. It returns a list of labels, each with a score which represents the confidence level that the model has about the label.

We can also run similar code on frames from a video. To do so, we use the moviepy library to grab frames at certain timestamps and then find labels for them.

```python
from moviepy.editor import VideoFileClip
from PIL import Image
from transformers import pipeline
from shots import get_shots

videofile = "myvideo.mp4"

scenes = get_shots(videofile)

clip = VideoFileClip(videofile)

for i, scene in enumerate(scenes):
    start_time = scene["start"]

    # extract a the first frame of the scene
    frame = clip.get_frame(start_time)

    # convert the frame into an image
    img = Image.fromarray(frame)

    # get a label from the image
    results = labeler(img)

    print("scene", i, start_time)
    for r in results:
        print(r["score"], r["label"])

```

## Captioning images

You can also use machine learning to generate captions for images.

The code is very very similar, I've just replaced the name and type of the model.

```python

from transformers import pipeline
from PIL import Image

MODEL = "nlpconnect/vit-gpt2-image-captioning"

captioner = pipeline("image-to-text", model=MODEL)

img = Image.open("myimage.jpg")
results = captioner(img)
print(results)

```

## Exploring models

Here's a list of all the image classification models: https://huggingface.co/models?pipeline_tag=image-classification&sort=trending

And here's a list of all the captioning models (also known as "image-to-text"): https://huggingface.co/models?pipeline_tag=image-to-text&sort=trending

To change the model in the above example, just replace the value of the `MODEL` variable. 

For example to try out a model made by SalesForce (the company):

```
MODEL = "Salesforce/blip-image-captioning-large"
```

Note that the first time you use one of these models, it will download to your computer. Some of them are extremely large (in the gigabytes), so be attentive to hard drive space etc. Some will also be much slower or faster than others -- generally speaking a larger model will be more accurate, but slower.

## Example scripts

I've provided a few example scripts for you to play with.

`caption_shots.py`: captions each shot in a video, and saves the output to a json file

`label_shots.py`: classifies each shot in a video, and saves the output to a json file

`search_scenes.py`: searches through shot labels and makes a supercut based on a search term

`extract_objects.py`: extracts images of objects from frames in a video