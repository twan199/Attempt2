from PIL import Image
import glob
import os
import shutil
import hashlib


def create_hash(filename, imagepath):
    md5hash = hashlib.md5(
        Image.open(os.path.join(os.path.join(imagepath, filename))).tobytes())
    hashname = md5hash.hexdigest()
    hashimagespath = os.path.join(imagepath, hashname)
    os.makedirs(hashimagespath, exist_ok=True)
    shutil.move(os.path.join(imagepath, filename), hashimagespath)
    filepath = os.path.join(hashimagespath, "original")
    os.rename(os.path.join(hashimagespath, filename), filepath)
    quality_factor = 50
    im = Image.open(filepath)
    rgb_im = im.convert('RGB')
    rgb_im.save(os.path.join(hashimagespath, "image.png"),
                quality=quality_factor,
                optimize=True)
    rgb_im.save(os.path.join(hashimagespath, "image.jpg"),
                quality=quality_factor,
                optimize=True)
    rgb_im.save(os.path.join(hashimagespath, "image.gif"),
                quality=quality_factor,
                optimize=True)
    # resize to reduce size and more practical possible
    filesize = []
    filenames = []

    for image in glob.glob(hashimagespath + "/image.*"):
        filenames.append(image)
        filesize.append(os.path.getsize(image))
        if len(filenames) > 1:
            if filesize[0] > filesize[1]:
                os.remove(filenames[0])
                del (filesize[0])
                del (filenames[0])
            else:
                os.remove(filenames[1])
                del (filesize[1])
                del (filenames[1])

    while os.path.getsize(filenames[0]) > 10000:
        resizer(filenames[0])
    os.rename(filenames[0], hashimagespath + "/optimized")

    if os.path.getsize(hashimagespath +
                       "/optimized") > os.path.getsize(hashimagespath +
                                                       "/original"):
        os.remove(hashimagespath + "/optimized")
        shutil.copy2(hashimagespath + "/original",
                     hashimagespath + "/optimized")

    rgb_im.save(hashimagespath + "/thumbnail.png")
    while os.path.getsize(hashimagespath + "/thumbnail.png") > 1000000:
        resizer(hashimagespath + "/thumbnail.png")
    return (hashimagespath + "/thumbnail.png")


def resizer(imagepath):
    image = Image.open(imagepath)
    xx, yy = image.size
    xx = int(xx / 2)
    yy = int(yy / 2)
    image = image.resize((xx, yy), Image.ANTIALIAS)
    image.save(imagepath)


# create_hash(
#     "04016_cosmologicalmasterpiece_6400x4000.jpg",
#     "/mnt/c/Users/Bouts/Documents/Biogrund/attempt2test/Attempt2/instance/images/"
# )