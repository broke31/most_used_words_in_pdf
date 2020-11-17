import re


def format_text(content_file):
    to_return = re.sub(r'[^\x00-\x7F]+', '', content_file)  # remove all not ascii char
    to_return = re.sub(r'[^\w\s]', '', to_return)  # remove not alphanumeric char
    to_return = ''.join([i for i in to_return if not i.isdigit()])  # remove all digit
    to_return = re.sub(r'\([^)]*\)', '', to_return)
    to_return = to_return.lower()
    return to_return


def split_freq(freq_to_plot):
    first_elts = [x[0] for x in freq_to_plot]
    second_elts = [x[1] for x in freq_to_plot]
    return first_elts, second_elts