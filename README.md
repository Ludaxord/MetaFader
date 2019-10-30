# MetaFader

Simple library to remove and display MetaData of Image.


## Pre-requirements:

* Python (Tested on Python 3.6)

* CMD/Terminal


## Usage

`python run.py --path <path_to_file> --new_path <path_to_new_file>`

## Docs

### MetaFader

MetaFader defines main logic of library. As a constructor it except (required) string argument with path of file user want to scan.

`get_meta(image)` - create dictionary with exif metadata. Except required argument with path to file.

`meta_display()` - create dictionary with exif metadata. If user do not pass any arguments it takes argument from constructor. Additional Arguments: path to file.

`meta_remove()` - create new file with removed exif metadata. Only required argument is save_file. To use if user want to save new file without exif data.

### Parser

Parser defines terminal arguments required to run script. 

`meta_display_args()` - create argument list:

* path - to define path to scan file.
* new_path - to define new path to file with removed metadata.
