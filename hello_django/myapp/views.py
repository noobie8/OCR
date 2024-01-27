from django.shortcuts import render
from django.http import HttpResponse

from PIL import Image
import os

# Create your views here.
def print_hello(request):
    return render(request,"main.html")



def image_convertion()
    # Set the path of the directory containing the TIFF files
    tiff_dir = '/path/to/tiff/directory'

    # Set the path of the directory to save the JPEG files
    jpeg_dir = '/path/to/jpeg/directory'

    # Loop through all the files in the TIFF directory
    for filename in os.listdir(tiff_dir):
        if filename.endswith('.tif') or filename.endswith('.tiff'):
            # Open the multi-TIFF file
            im = Image.open(os.path.join(tiff_dir, filename))

            # Save each frame of the multi-TIFF as a separate JPEG file
            for i in range(im.n_frames):
                im.seek(i)
                # Set the filename of the JPEG file
                jpeg_filename = os.path.splitext(filename)[0] + f'_frame{i}.jpg'
                # Save the current frame as a JPEG file
                im.save(os.path.join(jpeg_dir, jpeg_filename))