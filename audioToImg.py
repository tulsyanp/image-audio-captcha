import librosa
import librosa.display
from matplotlib import pylab
from pylab import *
import os


def audio_to_spect(src_dir, out_dir, ext):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(ext):
                save_path = os.path.join(out_dir, os.path.splitext(file)[0]+'.png')
                if not os.path.exists(save_path):
                    print(root, file)
                    sig, fs = librosa.load(os.path.join(root, file))
                    pylab.figure(figsize=(1.28, 0.64), dpi=100)
                    pylab.axis('off')
                    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
                    S = librosa.feature.melspectrogram(y=sig, sr=fs)
                    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
                    save_path = os.path.join(out_dir, os.path.splitext(file)[0]+'.png')
                    pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
                    pylab.close()

input_dir = './audio'
output_dir = './audioSpec'

audio_to_spect(input_dir, output_dir, 'mp3')
