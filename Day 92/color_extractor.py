"""
Color extraction logic using NumPy.

The core idea:
1. Load the image and turn it into a NumPy array of RGB pixel values.
2. "Bucket" similar colors together (round them to the nearest step),
   so that near-identical shades count as the same color.
3. Count how often each bucketed color appears.
4. Return the top N most common colors as hex codes.
"""

import numpy as np
from PIL import Image


def extract_top_colors(image_path, num_colors=10, bucket_size=32, resize_to=150):
    """
    Analyzes an image and returns its top `num_colors` most common colors.

    Returns a list of dicts, each with:
        - hex: e.g. "#ff5733"
        - rgb: e.g. (255, 87, 51)
        - percentage: how much of the image this color covers, e.g. 12.4
    """
    # Open the image and make sure it's in standard RGB (3 channels, no alpha)
    image = Image.open(image_path).convert("RGB")

    # Shrink the image before analysis — a 4000x3000 photo has 12 million
    # pixels, which is slow to process and unnecessary for finding the
    # *dominant* colors. A small thumbnail gives basically the same result,
    # much faster.
    image = image.resize((resize_to, resize_to))

    # Turn the image into a NumPy array. Shape is (height, width, 3) —
    # 3 for the Red, Green, Blue values of each pixel.
    pixels = np.array(image)

    # Reshape into a flat list of pixels: (height * width, 3).
    # We no longer care about *where* each pixel is, only its color.
    pixels = pixels.reshape(-1, 3)

    # --- Bucketing step ---
    # Without this, (254, 87, 51) and (255, 88, 52) would be counted as
    # two completely different colors, even though they look identical
    # to the human eye. Real photos can contain thousands of these tiny
    # variations, so raw counting rarely finds meaningful "top colors".
    #
    # Instead, we round every channel down to the nearest `bucket_size`
    # (e.g. 32), then shift it to the middle of that bucket. This groups
    # nearby shades into the same "bucket" of color.
    buckets = (pixels // bucket_size) * bucket_size + bucket_size // 2
    buckets = np.clip(buckets, 0, 255)  # keep values within valid RGB range

    # Find every unique bucketed color, and how many pixels fall into it.
    # axis=0 means "treat each row (each RGB triplet) as one unit to compare".
    unique_colors, counts = np.unique(buckets, axis=0, return_counts=True)

    # Sort bucket indices by count, descending, and keep the top N.
    top_indices = np.argsort(-counts)[:num_colors]

    total_pixels = pixels.shape[0]
    results = []

    for index in top_indices:
        r, g, b = unique_colors[index]
        count = counts[index]
        percentage = round(float(count) / total_pixels * 100, 1)
        hex_code = "#{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))

        results.append({
            "hex": hex_code,
            "rgb": (int(r), int(g), int(b)),
            "percentage": percentage,
        })

    return results
