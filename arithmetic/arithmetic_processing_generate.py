import numpy as np
import os
from os import path
from PIL import Image
import matplotlib.pyplot as plt

im_true_path = path.join('.','positive_general')
im_answer_path = path.join('.','positive_answer')
my_data = np.zeros(shape=(30000, 1921), dtype=float)
# train = np.zeros(shape=(20000, 1921), dtype=float)
# test = np.zeros(shape=(10000, 1921), dtype=float)

for i in range(30000):
    my_num = str(i)
    a = np.array(Image.open(im_true_path+'/'+my_num+'.jpg'))
    # print a.shape
    a = a.reshape(960)
    my_data[i, :960] = a

for i in range(30000):
    num = str(i)
    a = np.array(Image.open(im_answer_path+'/'+num+'.jpg'))
    a = a.reshape(960)
    my_data[i, 960:-1] = a
    if i<7500:
        my_data[i, -1] = 1
    elif i<15000:
        my_data[i, -1] = 2
    elif i<22500:
        my_data[i, -1] = 3
    else:
        my_data[i, -1] = 4

for i in range(30000):
    print(my_data[i,-1])
print(sum(my_data[:,-1]))
np.random.shuffle(my_data)

train = my_data[0:20000, :]
test = my_data[20000:30000, :]
print(train.shape,test.shape)

train_data = train[:, :960]
print(train_data.shape)
# print train_x

train_label = train[:, 960:-1]
print(train_label.shape)
train_label_y = train[:, -1]
print(train_label_y.shape)
print(sum(train_label_y))
# print 124852.0

test_data = test[:, :960]
print(test_data.shape)

test_label = test[:, 960:-1]
print(test_label.shape)
test_label_y = test[:, -1]
print(test_label_y.shape)
print(sum(test_label_y))
# print 12566.0
# train_data, train_label = get_dataset(30000, 'train_numbers.txt', 99999, img_sz)
# test_data, test_label = get_dataset(30000, 'test_numbers.txt', 4999999, img_sz)
mu = np.mean(train_data,axis=0)
np.save("mu", mu)
train_data -= mu
test_data -= mu

rp = np.random.permutation(train_data.shape[0])
train_data = train_data[rp]
train_label = train_label[rp]

np.save('train_X',train_data)
np.save('train_y',train_label)
np.save('test_X',test_data)
np.save('test_y',test_label)

