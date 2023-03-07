# VoiceChanger-with-python
There are some differences between voice of women and men. The most important one of them is that the higher pitch. 
In general, women speak at a higher pitch—about an octave higher than men. An adult woman's average range is from 165 to 255 Hz, while 
a man's is 85 to 155 Hz (see sources). Men's voices are generally deeper because the surge of testosterone released during puberty causes their 
vocal cords to elongate and thicken. 
\
So, to do this project i use an structure like following picture:
\
\
![image](https://user-images.githubusercontent.com/58389567/223437677-73573cc9-a4b2-4096-be50-520a948dcb91.png)
\
But before do this, we need to find the gender of input audion before shifting pitch; So our projecف is divided into the following sections:
- gender ditection
- find pitch
- shift pitch according to gender
- plot audio pitch before and after of shifting


# gender detection
I define a gender detection function wichh uses fourier series and power spectrum to find max point. After that our function decides about the gender of audio according 
to a threshold. 
\
\ 
We can also use an AI model like regression or neural network and etc; But these models have more calculation load.

# find pitch
I use librosa library to find the pitch of input audio and it's useful to plot our pitch according to frequency.

# shift pitch according to gender
After finding gender, we need to shift the pitch but if our gender is male, we should shift upthe pitch and if our gender is female, we should shift down the pitch.

# plot audio pitch before and after of shifting
Finally, we should design a plot pitch function to plot input audio's pithch before and after of shifting
