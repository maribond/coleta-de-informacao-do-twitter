# -*- coding: utf-8 -*-
"""
Created on Mon May 14 08:53:54 2018

@author: Daniel
"""

import numpy as np
import string
from TwitterSearch import *#bliblioteca usada
try:
    tuo = TwitterUserOrder('dunfrey') #conta que deseja verificar as informações
    ts = TwitterSearch(
        #informaçoes da api do twitter               
        consumer_key = 'IMJh4kjQLGDzUaT9t1v0RXm5Y',
        consumer_secret = 'cjt9d684CpvElXof1BxUMgSakNnFBVLDweQTSpGZolzzrnU8JE',
        access_token = '968521944944529408-oI5NcJVaZellwrsPjhsQkQPDeAZJzKf',
        access_token_secret = 'hc7bTI65fG97smD3ZEB6iCjLrBzHBxn2Sp6TIaX8fZSJZ'
     )


    s = ""# variavel criada para armazenar a informaçao do twitter

    for tweet in ts.search_tweets_iterable(tuo):  #laço que pega um twitter por vez           
        texto = ( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        print (texto)#printa o twitter
       
        s+=str(texto) #joga toda informação coletada em uma variavel
        
        
except TwitterSearchException as e:
    print(e)#tratamento de exceção
 
    
text= s.lower()  #informaçao coletada é colocada em letra minuscula para que ela possa ser tratada logo abaixo

text = text = text.translate({ord(k): None for k in string.punctuation})
words = text.split()
wordset = set(words)
freq={word: words.count(word) for word in wordset}#codigo encontrado pronto da internet para calcular informaçao

print ("Palavra   |  Contador | Autoinformação")
word_count_information = []
entropy = 0
for word in wordset:
   probability = freq[word] / float(1.0 * len(words))
   self_information = np.log2(1.0/probability)
   entropy += (probability * self_information)
   word_count_information.append([word, freq[word], self_information])

sorted_word_count_information = list(sorted(word_count_information, key=lambda k:k[2], reverse=True))
for ii in sorted_word_count_information:
   
   separation = '\t\t' if len(ii[0]) < 7 else '\t'
   if len(ii[0]) >= 15: separation = ''
   print("%s %s %s \t %s"%(ii[0], separation, str(ii[1]), str(ii[2])))
print( "\n\nEntropia do texto completo: {}".format(entropy)) 

