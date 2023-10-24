from transformers import pipeline
from PIL import Image

# based on tutorial at: https://huggingface.co/docs/transformers/main/tasks/zero_shot_image_classification
# other models to use: https://huggingface.co/models?pipeline_tag=zero-shot-image-classification&sort=downloads

IMAGE_NAME = "beer.png"
LABELS = ["soda", "cat", "can", "beer"]
# MODEL = "openai/clip-vit-large-patch14" #1.7gb
MODEL = "openai/clip-vit-base-patch32" #600mb

detector = pipeline(model=MODEL, task="zero-shot-image-classification")
results = detector(Image.open(IMAGE_NAME), candidate_labels=LABELS)

for r in results:
  print(r["score"], r["label"])
