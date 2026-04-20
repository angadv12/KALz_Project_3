import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# define base path to extracted zip image data
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

print(os.listdir(base_path))

# check train and test folders
train_path = os.path.join(base_path, "train")
test_path = os.path.join(base_path, "test")

# make sure the zip was extracted into the expected folder layout
required_dirs = [
    os.path.join(train_path, "REAL"),
    os.path.join(train_path, "FAKE"),
    os.path.join(test_path, "REAL"),
    os.path.join(test_path, "FAKE"),
]
missing_dirs = [folder for folder in required_dirs if not os.path.isdir(folder)]

if missing_dirs:
    raise FileNotFoundError(f"Missing expected image folders: {missing_dirs}")

print("Train folders:", os.listdir(train_path))
print("Test folders:", os.listdir(test_path))

# Build a dataframe with image paths and labels
def load_image_paths(folder, split):
    data = []
    for label in ["REAL", "FAKE"]:
        class_path = os.path.join(folder, label)
        for file in os.listdir(class_path):
            path = os.path.join(class_path, file)
            if not os.path.isfile(path):
                continue

            data.append({
                "path": path,
                "label": label,
                "split": split
            })
    return pd.DataFrame(data)


# build df for each set then combine into one DF
train_df = load_image_paths(train_path, "train")
test_df = load_image_paths(test_path, "test")
df = pd.concat([train_df, test_df], ignore_index=True)

print(df.head())
print("Total images:", df.shape)

# first check class distribution in train and test sets
train_df['label'].value_counts().plot(kind='bar')
plt.title("Train Class Distribution")
plt.show()

test_df['label'].value_counts().plot(kind='bar')
plt.title("Test Class Distribution")
plt.show()

# show some sample images from each class to get a visual sense of the data
def show_images(df, label, n=8):
    label_df = df[df['label'] == label]
    subset = label_df.sample(min(n, len(label_df)), random_state=42)
    display_n = len(subset)

    plt.figure(figsize=(12, 3))
    for i, row in enumerate(subset.itertuples()):
        img = Image.open(row.path)
        plt.subplot(1, display_n, i + 1)
        plt.imshow(img)
        plt.axis('off')

    plt.suptitle(f"{label} Images")
    plt.show()


show_images(df, "REAL")
show_images(df, "FAKE")

sizes = []

# check image sizes to confirm they are all the same dimensions (32x32)
for path in df['path'].sample(min(1000, len(df)), random_state=42):
    img = Image.open(path)
    sizes.append(img.size)

sizes = pd.DataFrame(sizes, columns=["width", "height"])

# plot distributions of widths and heights to confirm all images are 32x32
sizes['width'].hist()
plt.title("Width Distribution")
plt.show()

sizes['height'].hist()
plt.title("Height Distribution")
plt.show()

print(sizes.head())

# check pixel value distributions for REAL vs FAKE images to see if 
# there are obvious diffs in brightness or variance that could be used
# as simple features for classification
def get_brightness(df, n=2000):
    vals = []
    sample = df.sample(min(n, len(df)), random_state=42)

    for path in sample['path']:
        img = np.array(Image.open(path))
        vals.append(img.mean())

    return vals


real_brightness = get_brightness(df[df.label == "REAL"])
fake_brightness = get_brightness(df[df.label == "FAKE"])

# plot brightness dists
plt.hist(real_brightness, alpha=0.5, label="REAL")
plt.hist(fake_brightness, alpha=0.5, label="FAKE")
plt.legend()
plt.title("Brightness Distribution")
plt.show()

# check variance distribution to see if there are diffs in
# texture or noise patterns that could be used as features
def get_variance(df, n=2000):
    vals = []
    sample = df.sample(min(n, len(df)), random_state=42)

    for path in sample['path']:
        img = np.array(Image.open(path))
        vals.append(img.var())

    return vals


real_var = get_variance(df[df.label == "REAL"])
fake_var = get_variance(df[df.label == "FAKE"])

# plot variance dists
plt.hist(real_var, alpha=0.5, label="REAL")
plt.hist(fake_var, alpha=0.5, label="FAKE")
plt.legend()
plt.title("Pixel Variance Distribution")
plt.show()
