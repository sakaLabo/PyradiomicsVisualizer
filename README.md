# PyradiomicsVisualizer

## Abstract  
Note that although this visualization tool is effective in identifying features, the meaning of features is somewhat different from that of a normal scan.  
Unlike normal operations, this method scans a small mask, computes features, and repositions them as an image.  

## Library

Python 3.7  
pyradiomics 3.0.1  
matplotlib 3.5.3  
tqdm 4.64.1  

## SampleInput
The image obtained by  
radiomics.getTestCase('lung2')  
was used.  
<img width="128" alt="lungSample" src="https://user-images.githubusercontent.com/106053283/214072632-1ff3609b-c420-4076-8cc6-66dec54a3ce2.png">
 
## SampleResult  
The sample source has a resolution of 64, but the results shown here are with a resolution of 256.  
### FirstOrder  
![sampleLungFirstOrder](https://user-images.githubusercontent.com/106053283/214073725-f7510328-bc2d-4b7e-9ac7-980be4161be0.png)

### GLCM  
![sampleLungGLCM](https://user-images.githubusercontent.com/106053283/214073877-10680d61-557a-4809-affe-f2ad59a5d28f.png)

### GLDM  
![sampleLungGLDM](https://user-images.githubusercontent.com/106053283/214073921-2e90a1a8-b2e3-4a64-879c-a847a475f6f4.png)

### GLRLM  
![sampleLungGLSZM](https://user-images.githubusercontent.com/106053283/214073973-46375692-a673-457a-836e-efa61992e7b3.png)

### NGTDM
![sampleLungNGTDM](https://user-images.githubusercontent.com/106053283/214074048-744c7fe8-ee00-4606-8b95-19718a36e2eb.png)

