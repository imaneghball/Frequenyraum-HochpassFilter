import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("robik.jpg",0)

f=np.fft.fft2(img)
fourieBild=np.fft.fftshift(f)
fourieraum=20*np.log(np.abs(fourieBild))
###########################################
###ideal Hi pass Filter
w,h=img.shape
D0=60
out=np.zeros((w,h),dtype=np.float32)
for u in range(w):
    for v in range(h):
        D=np.sqrt((u-w/2)**2 + (v-h/2)**2)+1
        if D <= D0:
            out[u,v]=0
        else:
            out[u,v]=1
resultFilterRaum=fourieraum*out
resultFilterBild=fourieBild*out
backshift=np.fft.ifftshift(resultFilterBild)
Kanten=np.abs(np.fft.ifft2(backshift))
plt.imshow(Kanten,cmap="gray"),plt.xticks([]),plt.yticks([]),
plt.title("Ideales Hochpass-Filter")
plt.show()
################################################
##Butterworth-Filter
# w,h=img.shape
# D0=60
# n=1
# out=np.zeros((w,h),dtype=np.float32)
# for u in range(w):
#     for v in range(h):
#         D=np.sqrt((u-w/2)**2 + (v-h/2)**2)+1
#         out[u,v] = 1/(1+(D0/D)**(2*n))
#
# resultFilterRaum=fourieraum*out
# resultFilterBild=fourieBild*out
# backshift=np.fft.ifftshift(resultFilterBild)
# Kanten=np.abs(np.fft.ifft2(backshift))
# plt.imshow(Kanten,cmap="gray"),plt.xticks([]),plt.yticks([]),
# plt.title("Butterworth-Filter")
# plt.show()
####################################################
# ##GaußFilter
# w,h=img.shape
# D0=10
# out=np.zeros((w,h),dtype=np.float32)
# for u in range(w):
#     for v in range(h):
#         D=np.sqrt((u-w/2)**2 + (v-h/2)**2)
#         out[u,v]=1-np.exp(-D**2/(2*D0*D0))
#
# resultFilterRaum=fourieraum*out
# resultFilterBild=fourieBild*out
# backshift=np.fft.ifftshift(resultFilterBild)
# Kanten=np.abs(np.fft.ifft2(backshift))
# plt.imshow(Kanten,cmap="gray"),plt.xticks([]),plt.yticks([]),
# plt.title("Gauß-Filter")
# plt.show()