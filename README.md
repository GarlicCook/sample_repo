# Image Preprocessor

### This is an image preprocessor with five features: color extraction, color filter, blurr filter, count face, and EXIF removal.

# Installation

### Install through pip :
```bash
$ pip install imgPreprocessor
```

# usage e.g.

```python
from img import extract_color_palette, plot_palette,

plot_palette((extract_color_palette("image_path.jpg"))) 
```

```python
from imgPreprocessor import ColorFilter

c=ColorFilter("image_path.jpg") 

user_color = (201, 251, 206)
#(B, G, R)
c.custom_colorfilter(user_color)
c.show()

c.deepskyblue_colorfilter()
c.show()
```

```python
from imgPreprocessor import CountFace

c=CountFace()
c.set_image_path("image_path.jpg")
print(c.count_faces())
```
```python
from imgPreprocessor import CustomBlurFilter
c=CustomBlurFilter("image_path.jpg")
c.load_image()
c.enhance_and_blur(clip_limit=2.0, tile_grid_size=(8, 8), blur_ksize=(15, 15))
#optional: clip_limit, tile_grid_size, blur_ksize
c.display_images()
``` 
```python 
from imgPreprocessor import modexif
modexif("image_path.jpg", "output_path.jpg", make = "samsung", model = "S24", datetime = "2024:12:05 12:57:54") 
#optional: make, model, datetime
#datetime format : "year:month:day hour:minute:second" 
```


### authors

- [GarlicCook](mailto:kms300508@gmail.com)
- [ugyo](mailto:rss1234567@hanyang.ac.kr)
- [jaesung05](mailto:1004jaesung@gmail.com)
- [rlaehdrbb](mailto:donggyug713@gmail.com)
- [hong02jp](mailto:hong02jp@gmail.com)


