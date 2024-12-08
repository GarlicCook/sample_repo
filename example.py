from imgPreprocessor import *

image_path = './example_img/4.jpg'

#CustomBlurFilter
filter = CustomBlurFilter(image_path)
filter.load_image()
filter.enhance_and_blur()
filter.display_images()

#ColorFilter
filter = ColorFilter(image_path)
user_color = (1, 255, 125)

filter.make_gray_image()
filter.show()

filter.custom_colorfilter(user_color)
filter.show()


#color_extracter
plot_palette((extract_color_palette(image_path, 3)))

#CountFace
face = CountFace()
face.set_image_path("./example_img/person.jpg")
face.count_faces()

#modexif
modexif("./example_img/test.jpg", "output_path.jpg", "", "S24", "2023:12:05 12:57:54")
