import json
import numpy as np

def load_json_file(filename):

	with open(filename, 'r') as json_file:
		json_list = list(json_file)
	json_file.close()

	texts = [json.loads(x)['text'] for x in json_list]

	return texts

def load_standard_json(filename, check_by_image):
	data = {}
	with open(filename, 'r') as json_file:
		data = dict(json.load(json_file))
	texts= []
	if check_by_image is True:
		dataDict = {}
		for img_name, captions in data.items():
			text = ""
			for caption in captions:
				text = text + caption + " "
			texts.append(text)
	if check_by_image is False:
		for img_name, captions in data.items():
			for caption in captions:
				texts.append(caption)
	return texts

def load_caption_file(filename, check_by_image):
	with open(filename, 'r') as file:
		textLines = file.readlines()
	file.close()
	texts = []
	if check_by_image:
		dictionaryByImage = {}
		for line in textLines:
			if line.split(":")[0] in dictionaryByImage:
				dictionaryByImage[line.split(":")[0]] = dictionaryByImage[line.split(":")[0]] + line.split(":")[1].replace("\n", " ")
			if line.split(":")[0] not in dictionaryByImage:
				dictionaryByImage[line.split(":")[0]] = line.split(":")[1].replace("\n", " ")
		texts = list(dictionaryByImage.values())
		# print(dictionaryByImage)
	if not check_by_image:
		for line in textLines:
			texts.append(line.split(":")[1])
	return texts

def get_results(experiment_name, dataset_type, adv_textList: list, results: list, num_ch : list):
	print('Results for ' + experiment_name)

	results = np.float32(np.asarray(results))

	num_human = 0
	num_mutation = 0
	num_synthetic = 0
	num_changed = 0
	avg = 0
	for adv in adv_textList:
		avg += len(adv)

	for i in range(results.size):
		if np.float32(results[i]) == 0:
			num_mutation += 1
		elif np.float32(results[i]) == 1:
			num_human += 1
		else:
			num_synthetic += 1
		num_changed+=np.float32(num_ch[i])#How many characters cut off

	print('Number human:', f'Human: {num_human}, Mutation: {num_mutation}, Synthetic: {num_synthetic}')
	if dataset_type == 0:
		print('Detector accuracy:', (num_mutation / results.size))
	elif dataset_type == 1:
		print('Detector accuracy:', (num_human / results.size))
	else:
		print('Detector accuracy:', (num_synthetic / results.size))
	print('Average number of changes:', num_changed / len(num_ch))
	print('Number of Attacks Run:', results.size)
