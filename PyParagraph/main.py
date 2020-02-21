import os
import re
letter_count=[]
words_per_sentence=[]

with open('DC_sample.txt', 'r') as file:
    words=file.read()
    count=words.split()
    sentences=words.split('.')   
    
    #word count and sentence count
    word_count=len(count)
    sentence_count=len(sentences)

    #letter count per word
    for word in count:
        letter_count.append(len(word))
    letter_p_word= (sum(letter_count)/len(letter_count))
    
    #word count per sentence
    for sentence in sentences:
        words_in_sentence=sentence.split()
        words_per_sentence.append(len(words_in_sentence))
    avg_sentence_length=(sum(words_per_sentence)/len(words_per_sentence))
    
    print("Approximate word count: " + str(word_count))
    print("Approximate sentence count: " + str(sentence_count))
    print("Approximate letter count (per word): " + str(letter_p_word))
    print("Approximate word count (per sentence): " + str(avg_sentence_length))    
    

