#!/usr/bin/python
import re
from statistics import median

def search_repeat(text):
    frequency = dict()
    match_pattern = re.findall('[а-яё]{2,15}', text)
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
    print(frequency)
    return frequency

    
def average_count(text):
    result = re.sub('[!?]', '.', text)
    sent_count = len(result.split('.'))-1  
    word_count = len(result.split())
    average_count = word_count/sent_count
    return average_count
    
    
def median_count(text):
    result = re.sub('[!?]', '.', text)
    print(median([len(sentence.split()) for sentence in result.split('.')]))
    
    
def top_K(text, K, N):
    token = re.split('\W+',text)
    z = zip(*[token[i:] for i in range(N)])
    ngrams = [" ".join(N) for N in z]
    frequency = dict()
    for word in ngrams:
        count = frequency.get(word,0)
        frequency[word] = count + 1
    sorted_dict = {}
    sorted_val = sorted(frequency, key=frequency.get, reverse = True)
    
    i = 0
    for w in sorted_val:
        i += 1 
        sorted_dict[w] = frequency[w]
        if i==K:
            break
        
    
    print(sorted_dict)
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
    top_K(text, 2, 4)
    
    print("Введите N: ")
    N = input()
    print("Введите K: ")
    K = input()
    top_K(text, int(N), int(K))
    
    
if __name__ == "__main__":
    main()
