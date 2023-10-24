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