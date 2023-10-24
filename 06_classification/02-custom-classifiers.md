# Custom Classifiers

There are three principle ways to customize image classifiers. You can either train your own classifier from scratch (not something we'll be doing), fine-tune an existing classifier, or use a "zero-shot" classifier.

## Zero Shot Classification

Some machine learning models contain supplementary information about the images they've been trained on. A zero-shot classifier uses this supplemental info to recognize images that were not necessarily included in its original training set.

Hugging face has a nice [tutorial on zero-shot classification](https://huggingface.co/docs/transformers/main/tasks/zero_shot_image_classification). And here's a [full list of models](https://huggingface.co/models?pipeline_tag=zero-shot-image-classification&sort=downloads) that support this method.

To use a zero-shot classifier, you just supply a list of labels of things you're looking for.

Here's an example using a single image.

```python
from transformers import pipeline
from PIL import Image

IMAGE_NAME = "beer.png"
LABELS = ["soda", "cat", "can", "beer"] # these are the things it's looking for!
MODEL = "openai/clip-vit-base-patch32" #600mb

detector = pipeline(model=MODEL, task="zero-shot-image-classification")
results = detector(Image.open(IMAGE_NAME), candidate_labels=LABELS)

for r in results:
  print(r["score"], r["label"])
```

Results will be a list of dictionaries, each dictionary contents a label and score between 0.0 and 1.0

To run this on a video, use the `custom_classifer_video.py` script. It will produce a `customlabels` json file with each scene labeled. To make a supercut of these, run `supercut_from_classifier.py`.

## Visualgrep

I've made an example script that combines scene detection, custom labeling, and super-cutting: `visualgrep.py`.

To use:

```bash
python3 visualgrep.py --input "myvideo.mp4" --labels "first label" "second label" "third label" --threshold 0.7 --search "first label" --output output.mp4
```

`--input`: input video  
`--label`: a list of labels to search for  
`--threshold`: only include clips equal to or above this threshold (between 0 and 1)  
`--search`: the search label to look for (defaults to the first one)  
`--output`: the supercut to save to

Please be aware that this script doesn't save a json file of labels. So each time you run it, it has to re-label everything. Meaning that it's good to play around with small video files, but not great for larger videos or collections of videos.

## Fine-tuning a model

Sometimes zero-shot classification doesn't work very well for particular labels you provide. In this situation, it can be better to train your own classifier based on a dataset of images that you provide. However, training your own machine learning model requires a ton of computational resources. Instead you can "fine-tune" an existing model. This means you start with a model that's already trained, and then add to the training with your own set of custom data.

To do this you'll need to collect source material to train on. Make a folder called `dataset` (or something similar) and inside that folder create a new folder for each type of image you'd like your model to recognize. For example, if I wanted to detect cops vs workers, I'd make two folders: `cops` and `workers` and then put images of cops in the cops folder and images of workers in the workers folder. Try to collect at least 100 images for each label your training on.

Because training a model, even fine-tuning one, can take a while on your own computer, I've prepared a google colab notebook that let's you fine-tune.

Click here: https://colab.research.google.com/drive/1thtUPgv9CoaNM5xuWxLy2MdBO4LMpbQW

In order to use the script, you'll need to first upload your dataset to your google drive, then mount the drive in the notebook.

Change the DATA_DIR variable to the name of your dataset folder, keeping the start of the line "drive/MyDrive/". So if you have a folder called "cat_dog_dataset" the variable should be set to: "drive/MyDrive/cat_dog_dataset/"

Then click the "play" button on each cell of code.

After a bit you should have a new folder saved to your google drive called "mymodel". You can then download that folder and use it in your scripts.

To use, just replace the model name in any of our previous examples with the name of the folder that you've downloaded.

### Automatically downloading images

It's probabably a good idea to hand-craft the images you use to train a model, but if you just want to download a bunch _very hegemonic_ ones from the internet, I've included a script called `download_images.py`.

The script looks like this:

```python
from bing_image_downloader import downloader

search_terms = ["cat", "dog"]

for query in search_terms:
    downloader.download(
        query,
        limit=300,
        output_dir="dataset",
        adult_filter_off=False,
        force_replace=False,
        timeout=60,
        verbose=True,
    )
```

Replace the list of search terms with whatever you'd like, and it will download images from bing into a folder called "dataset" with subfolders for your search terms.

Then, install the `bing-image-downloader` library with:

```
pip3 install bing-image-downloader
```

And run the script:

```bash
python3 download_images.py
```
