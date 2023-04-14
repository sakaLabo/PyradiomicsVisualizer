import numpy
import matplotlib.pyplot as plt
import SimpleITK as sitk
import radiomics
import tqdm
import six
import threading
import logging


# Inputs
imageDir = 'sampleCamera.tif'
#imageDir = 'lungSample.tif'
image = sitk.ReadImage(imageDir)
dstName = 'lungSample'

# Parameters
dstSize = 64 # 2**n (recomend:64)
kernelSize = 3 # Odd (recomend:3)
row = 5
column = 5
col = "jet"
multiThread = True

# Preparation
funcList = [radiomics.firstorder.RadiomicsFirstOrder,radiomics.glcm.RadiomicsGLCM, radiomics.glrlm.RadiomicsGLRLM, radiomics.glszm.RadiomicsGLSZM, radiomics.ngtdm.RadiomicsNGTDM, radiomics.gldm.RadiomicsGLDM]
textList = ["FirstOrder" , "GLCM", "GLRLM", "GLSZM", "NGTDM", "GLDM"]
logger = logging.getLogger("radiomics.glcm")
logger.setLevel(logging.ERROR)

resize = int(image.GetWidth() / dstSize)
image = image[::resize,::resize]
ndImg = sitk.GetArrayFromImage(image)
mask = sitk.GetImageFromArray(numpy.ones((kernelSize, kernelSize), numpy.int16))

resultList = []
titleList = []
for idx, func in enumerate(funcList):
    print(textList[idx])
    dummyImg = image[0:kernelSize,0:kernelSize]
    features = func(dummyImg, mask)
    features.enableAllFeatures()
    res = features.execute()
    titles = ['Original']
    for (key, val) in six.iteritems(res):
        titles.append(key)
    titleList.append(titles)
    resultList.append(numpy.zeros((len(res),image.GetHeight(),image.GetWidth()), dtype=numpy.float64))

# Cal
print('Calculating...')
def ScanningRadiomics(Func, Results):
    settings = {}
    for j in tqdm.tqdm(range(image.GetHeight() - kernelSize + 1)):
        for i in range(image.GetWidth() - kernelSize + 1):
            imgPatch = image[i:i + kernelSize,j:j + kernelSize]
            features = Func(imgPatch, mask, **settings)
            features.enableAllFeatures()
            result = features.execute()
            for id, (key, val) in enumerate(six.iteritems(result)):
                Results[id, j + int(kernelSize / 2),i + int(kernelSize / 2)] = val
                
if multiThread:
    threadList = []
    for idx, func in enumerate(funcList):
        threadList.append(threading.Thread(target=ScanningRadiomics, args=(func, resultList[idx])))
        threadList[idx].start()
    for thre in threadList:
        thre.join()
else:
    for idx, func in enumerate(funcList):
        ScanningRadiomics(func, resultList[idx])


# Visualize
print('Visualize')
for idx, resList in enumerate(resultList):
    plt.figure(figsize=(20,15))
    plotid = list(range(1, len(resList) + 1 + 1, 1))
    outs = [ndImg]
    for re in resList:
        data_arr = numpy.array(re)
        normalized_data = ((data_arr - numpy.min(data_arr)) / (numpy.max(data_arr) - numpy.min(data_arr))) * 255
        scaled_data = normalized_data.astype(numpy.uint8)
        outs.append(scaled_data)
    for i in range(len(titleList[idx])):
        plt.subplot(row,column,plotid[i])
        plt.tick_params(labelbottom=False, labelleft=False)
        plt.xticks([])
        plt.yticks([])
        if i == 0:
            plt.imshow(outs[i], cmap = "gray")
        else:
            plt.imshow(outs[i], cmap = col)
        plt.title(titleList[idx][i], fontsize=15)

    plt.tight_layout(pad=0.5)
    fName = dstName + textList[idx] + '.png' 
    plt.savefig(fName)
    #plt.show()

print('Fin')