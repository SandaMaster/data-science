#!/usr/bin/env python
# coding: utf-8

# In[21]:


# import pandas as pd
# import numpy as np


# In[22]:


# path = r"C:/Users/Grzegorz Mróz/Desktop/Projekt DS2.0/chatgpt-reddit-comments.csv"
# csv = pd.read_csv(path)


# In[23]:


# csv


# In[24]:


# comments = csv[["comment_id","comment_parent_id","comment_body"]]
# comments


# In[25]:


# from cleantext import clean


# In[26]:


## segregacja i czyszczenie danych 
# list_comment = []
# clean_list_commnet = []

# for comment_parent, comment_body in zip(comments["comment_parent_id"], comments["comment_body"]):
#     part_data = str(comment_parent)+ ":\n" + str(comment_body) + "\n"
#     clean_part_data = clean(part_data, no_emoji=True, no_urls=True)
#     clean_part_data_ = clean_part_data + "\n"
#     list_comment.append(part_data)
#     clean_list_commnet.append(clean_part_data_)


# In[27]:


# for x in clean_list_commnet[:100]:
#     print(x)


# In[10]:


## zapisywanie danych do pilku .txt
# to_write = "\n".join(clean_list_commnet)
# f = open("reddit_text.txt", mode="w")
# f.write(to_write)
# f.close


# In[36]:


path = "/net/people/plgrid/plgmrogrze/reddit_text.txt"
f = open(path)
data = f.read()
f.close
print(data)


# In[29]:


import tensorflow as tf
import numpy as np
import keras


# In[30]:


## tokenizowanie zanków
token = tf.keras.preprocessing.text.Tokenizer(char_level=True)
token.fit_on_texts([data])


# In[6]:


token.texts_to_sequences(["schocked"])


# In[7]:


token.sequences_to_texts([[8, 14, 10, 5, 14, 25, 2, 12]])


# In[8]:


# całkowita liość tokenów 
max_chars = len(token.word_index)
max_chars


# In[9]:


dataset_size = token.document_count # iliść źródeł z jakich mamy dane 
dataset_size


# In[10]:


"".join(sorted(set(data.lower()))) # dodtakopwy kod pokayje wszyskie 68 znaków zamienionych na małe 


# In[11]:


# funkcjia ustawia domyślnie wyszkie litery na małe
text_vec_layer = tf.keras.layers.TextVectorization(split="character",
                                                   standardize="lower")
text_vec_layer.adapt([data])
encoded = text_vec_layer([data])[0]


# In[12]:


# wywalnie 0 tokenu i 1 - nieznanego
encoded -= 2  
n_tokens = text_vec_layer.vocabulary_size() - 2  
dataset_size = len(encoded)  


# In[13]:


n_tokens


# In[14]:


dataset_size


# In[15]:


def to_dataset(sequence, length, shuffle=False, seed=None, batch_size=32):
# mniejsze podzbiory z długiego tekstu, 200 znaków w jednym podzbiorze i przesunięcie o 1 znak    
    ds = tf.data.Dataset.from_tensor_slices(sequence)
    ds = ds.window(length + 1, shift=1, drop_remainder=True)
# przekształcanie podziorów do jednego wymiaru, płaskiego flat     
    ds = ds.flat_map(lambda window_ds: window_ds.batch(length + 1))
## teraz można przetasować i pogrupować (tam gadzie się kończy jeden zaczyna drugi)    
    if shuffle:
        ds = ds.shuffle(100_000, seed=seed)
    ds = ds.batch(batch_size)
    return ds.map(lambda window: (window[:, :-1], window[:, 1:])).prefetch(1)


# ##### Tworzenie zbiorów 

# In[16]:


# pokazuje w którym miejscu zaczynją się nowe tokeny wyrazów 
list(to_dataset(text_vec_layer(["ve been"])[0], length=4))


# In[17]:


# ilość słow w ramce 200 i 90% zb train
length = 200
tf.random.set_seed(42)
train_set = to_dataset(encoded[:11_141_203], length=length, shuffle=True,
                       seed=42)
valid_set = to_dataset(encoded[11_141_203:11_760_158], length=length)
test_set = to_dataset(encoded[11_760_158:], length=length)


# ##### Sieć i ternowanie 

# In[18]:


from keras import Sequential
from keras import layers


# In[19]:


network = Sequential()
network.add(layers.Embedding(input_dim=max_chars, output_dim=16))
network.add(layers.GRU(256, return_sequences=True, dropout=0.2, recurrent_dropout=0.2))
network.add(layers.GRU(128, return_sequences=True, dropout=0.2, recurrent_dropout=0.2))
network.add(layers.GRU(128, return_sequences=True, dropout=0.2, recurrent_dropout=0.2))
network.add(layers.Dense(max_chars, activation="softmax")) 


# In[20]:


network.compile(loss="sparse_categorical_crossentropy", optimizer="nadam", metrics=["accuracy"])


# In[ ]:


history = network.fit(train_set, validation_data=valid_set, epochs=10)


# In[ ]:


## po wytrenoawnaiu modelu można dostarczyć do niego tekst
def preprocess(text):
    X = np.array(token.texts_to_sequences(text)) -1
    return tf.one_hot(X, max_chars)


# In[ ]:


# prognozowanie litery w jakimś tekscie 
#x_new = preprocess(['Hi how are yo'])
#y_pred = model.predict_classes(x_new)
#token.sequences_to_texts(y_pred +1)[0][-1] # pierwsze zdanie ostatni znak

