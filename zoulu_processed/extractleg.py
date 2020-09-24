import json
import os
import sys

path = 'C:/Users/83446/Documents/2DMotion/zoulu_processed/2d_keypoints_zoulu'

for file in os.listdir(path):
	current = os.path.join(path, file)
	if os.path.isfile(current):
		with open(current) as json_file:
			data = json.load(json_file)
			keypoints=data['people'][0]['pose_keypoints_2d']
			with open('zoulu_keypoints.csv','ab') as f:
				to_write = ''
				for i in range(0, 75, 3):	
					to_write += (str(keypoints[i]))
					to_write += (',')
					to_write += (str(keypoints[i+1]))
					to_write += (',')
				to_write = to_write[:-1]
				to_write += ('\n')
				f.write(to_write.encode())