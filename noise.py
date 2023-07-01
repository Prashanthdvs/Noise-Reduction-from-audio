from scipy.io import wavfile

import noisereduce as nr
# load data
rate, data = wavfile.read(r"C:\Users\damojipurapuv.d\Downloads\Audio-Denoising-master\Audio-Denoising-master\recording.wav")
# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate) #, thresh_n_mult_nonstationary=2,stationary=False)
wavfile.write("mywav_reduced_noise.wav", rate, reduced_noise)
