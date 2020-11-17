import glob
import os


def get_file_names(path, extension='pdf'):
    os.chdir(path)
    result = glob.glob('*.{}'.format(extension))
    return result


def get_file_without_extension(filename):
    split = os.path.splitext(filename)
    return split[0]


def save_into_file(name_file, freq_, path, suff):
    text_file = open(path + name_file + suff + ".txt", "w+")
    text_file.write(str(freq_))
    text_file.close()