import pandas

image = pandas.read_csv('imageSubmission.csv', header=None)
audio = pandas.read_csv('audioSubmission.csv', header=None)

image_audio = pandas.concat([image, audio])
image_audio = image_audio.sort_values(1)

image_audio.to_csv('submitty_19303677_sorted_submission.csv', index=False, header=False)