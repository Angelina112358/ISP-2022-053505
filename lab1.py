#!/usr/bin/python
import re
from statistics import median

def search_repeat(text):
    frequency = dict()
    match_pattern = re.findall('[а-яё]{3,15}', text)
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
    print(frequency)
    return frequency

    
def average_count(text):
    result = re.sub('[!?]', '.', text)
    sent_count = len(result.split('.'))-1  
    word_count = len(result.split())
    print(sent_count)
    print(word_count)
    average_count = word_count/sent_count
    print(average_count)
    
def median_count(text):
    result = re.sub('[!?]', '.', text)
    print(median([len(sentence.split()) for sentence in result.split('.')]))
    
def top_K(text, K, N):
    frequency = dict()
    match_pattern = re.findall('[а-яё]{3,15}', text)
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
    print(frequency)
    
    
    
    return frequency
    

    
def main():
    text_dict = dict()
    print("Введите текст: ")
    text = input().lower()
    
    print("Повторы: ")    
    search_repeat(text)
    
    print("Среднее количесво слов: ")
    average_count(text)    
    
    print("Медианное количество слов: ")
    median_count(text)
    
    print("Top K")
    top_K(text, 10, 4)
    
    
if __name__ == "__main__":
    main()
