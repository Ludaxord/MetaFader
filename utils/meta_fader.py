import locale

from PIL import Image, ExifTags

from utils.parser import meta_display_args


class MetaFader:
    file_path = None

    def __init__(self, file_path):
        self.file_path = file_path

    def meta_display(self, file_path=None):
        if file_path is None:
            file_path = self.file_path
        image = Image.open(file_path)
        exif = self.get_meta(image)
        return exif

    def get_meta(self, image):
        try:
            exif = {ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in ExifTags.TAGS}
        except Exception as e:
            print(f"{e}")
            exif = {}
        return exif

    def decode_maker_note(self, exif):
        maker_note = exif.get("MakerNote")
        maker_notes = [maker_note[i:i + 1] for i in range(0, len(maker_note), 1)]
        encodings = ['utf-8', 'utf-16', 'ascii', 'base64']
        print(f"encoding {encodings}")
        decoded = []
        for encoding in encodings:
            decoded_note = ""
            for note in maker_notes:
                try:
                    decoded_note += note.decode(encoding)
                except Exception as e:
                    exception = e
            decoded.append(decoded_note)
        return decoded

    def meta_remove(self, save_file, file_path=None, new_file_path=None):
        if file_path is None:
            file_path = self.file_path
        image = Image.open(file_path)
        data = list(image.getdata())
        removed_data_image = Image.new(image.mode, image.size)
        removed_data_image.putdata(data)
        if save_file:
            if new_file_path is None:
                new_file_path = file_path
            removed_data_image.save(new_file_path)
        return removed_data_image
