from bing_image_downloader import downloader
downloader.download("cat", limit=20,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
downloader.download("dog", limit=20,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
