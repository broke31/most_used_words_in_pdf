# Most used words in pdf

## What is it?
This small tool extracts the most used words (excluding "stopwords", punctuation and numbers) from a pdf. 
Finally it generates graphs and saves all the contents of the file in text format.

## How to use it?

Insert the files in pdf format in the root of the folder

and then launch this command:

```
python3 main.py
```

## Outputs

you will find in the directory "freq" the frequencies of each keywords identified, in the directory "outputs" the files in txt format (without keywords, punctuation and numbers)
and in the directory "figures" the frequency plot for each pdf and the most used frequency plot in n processing (Total frequencies)
