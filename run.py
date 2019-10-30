from utils.meta_fader import MetaFader
from utils.parser import meta_display_args

parser = meta_display_args()

path = parser.path
new_file_path = parser.new_path

meta = MetaFader(path)

exif = meta.meta_display()

print(exif)

new_image = meta.meta_remove(True, new_file_path=new_file_path)

new_exif = meta.meta_display(file_path=new_file_path)

print(new_exif)
