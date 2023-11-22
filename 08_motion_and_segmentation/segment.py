from PIL import Image
from transformers import pipeline

pipe = pipeline("image-segmentation")

img = Image.open("test.jpg")

results = pipe(img)

for i, r in enumerate(results):
    print(r)
    r["mask"].save(f"mask{i}.png")

    transparent_image = img.copy()
    transparent_image.putalpha(r["mask"])
    transparent_image.save(f"transparent{i}.png")
