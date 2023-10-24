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
