import os
import pathlib
from nltk.corpus import stopwords
from tika import parser
from nltk import FreqDist, word_tokenize
import nltk
from collections import Counter

from create_graphics import plot_and_save_graphic
from manupulate_text import format_text, split_freq
from os_system import get_file_names, get_file_without_extension, save_into_file

os.environ['TIKA_SERVER_JAR'] = 'https://repo1.maven.org/maven2/org/apache/tika/tika-server/1.19/tika-server-1.19.jar'
nltk.download('stopwords')


if __name__ == '__main__':
    lists = []
    name_file_final = "Total Frequencies"
    path_out = "outputs/"
    paths = ("outputs", "freq", "figures")
    namesFile = get_file_names(path=".")
    for path in paths:
        check = pathlib.Path(path)
        check.mkdir(parents=True, exist_ok=True)
    for name in namesFile:
        raw = parser.from_file(name)
        nameWithoutExtension = get_file_without_extension(name)
        parser.from_file(name)
        content = raw['content']
        content = format_text(content)
        save_into_file(nameWithoutExtension, content, path_out, "")
        text_tokens = word_tokenize(content)
        tokens_without_sw = [word for word in text_tokens if word not in stopwords.words()]
        cachedStopWords = set(stopwords.words('english'))
        text = ' '.join([word for word in content.split() if word not in cachedStopWords])
        text_list = text.split(" ")
        freqDist = FreqDist(text_list)
        words = list(freqDist.keys())
        freq = freqDist.most_common(25)
        print(freq)  # should give you a sorted list
        labels, values = split_freq(freq)
        save_into_file(nameWithoutExtension, freq, "freq/", "_keywords")
        plot_and_save_graphic(freq, nameWithoutExtension)
        lists.append(freq)
    counter = sum(map(lambda l: Counter(dict(l)), lists), Counter())
    most_common_final = counter.most_common(25)
    plot_and_save_graphic(most_common_final, name_file_final)
    save_into_file(name_file_final, most_common_final, path_out, "")
