from PIL import Image, ImageDraw
from transformers import pipeline

LABELS = [
    "human eyebrow",
    "human forehead",
    "human ear",
    "human face",
    "human nose",
    "human eye",
    "human mouth",
]
MODEL = "google/owlvit-base-patch32"

detector = pipeline(model=MODEL, task="zero-shot-object-detection")

image = Image.open("cops.jpg")

predictions = detector(
    image,
    candidate_labels=LABELS,
)

draw = ImageDraw.Draw(image)
for prediction in predictions:
    box = prediction["box"]
    label = prediction["label"]
    score = prediction["score"]
    xmin, ymin, xmax, ymax = box.values()
    draw.rectangle((xmin, ymin, xmax, ymax), outline="red", width=1)
    draw.text((xmin, ymin), f"{label}: {round(score,2)}", fill="white")
image.save("output.jpg")
