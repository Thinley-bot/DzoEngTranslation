from pickle import load
from numpy import array
from numpy import argmax
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import load_model
from numpy.random import rand
from numpy.random import shuffle



# load a clean dataset
def load_clean_sentences(filename):
	return load(open(filename, 'rb'))

# Function to load pickle data from disk
def load_files(filename):
    return load(open(filename,'rb'))

# load dataset
raw_dataset = load_clean_sentences('english-german.pkl')


# encode and pad sequences
def encode_sequences(tokenizer, length, lines):
	# integer encode sequences
	tokenizer=Tokenizer()
	X = tokenizer.texts_to_sequences(lines)
	# pad sequences with 0 values
	X = pad_sequences(X, maxlen=length, padding='post')
	return X

# map an integer to a word
def word_for_id(integer, tokenizer):
	for word, index in tokenizer.word_index.items():
		if index == integer:
			return word
	return None

# generate target given source sequence
def predict_sequence(model, tokenizer, source):
	prediction = model.predict(source, verbose=0)[0]
	integers = [argmax(vector) for vector in prediction]
	target = list()
	for i in integers:
		word = word_for_id(i, tokenizer)
		if word is None:
			break
		target.append(word)
	return ' '.join(target)

      


# prepare english tokenizer
eng_tokenizer = create_tokenizer(dataset[:, 0])
eng_vocab_size = len(eng_tokenizer.word_index) + 1
eng_length = max_length(dataset[:, 0])
# prepare german tokenizer
ger_tokenizer = create_tokenizer(dataset[:, 1])
ger_vocab_size = len(ger_tokenizer.word_index) + 1
ger_length = max_length(dataset[:, 1])


# load model
model = load_model('model.h5')

def ppredict(pranab):
	pagla=[pranab]
	testX = encode_sequences(eng_tokenizer, eng_length, pagla)
	translation = predict_sequence(model, ger_tokenizer, testX)
	return translation