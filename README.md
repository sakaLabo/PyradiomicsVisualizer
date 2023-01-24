# PyradiomicsVisualizer

## Abstract  
This is a tool for visualizing PyRadiomics features.  
Note that although this visualization tool is effective in identifying features, the meaning of features is somewhat different from that of a normal scan.  
Unlike normal operations, this method scans a small mask, computes features, and repositions them as an image.  

## Library

Python 3.7  
pyradiomics 3.0.1  
matplotlib 3.5.3  
tqdm 4.64.1  

## SampleInput
The sample image obtained by  
radiomics.getTestCase('lung2')  
was used.  
<img width="128" alt="lungSample" src="https://user-images.githubusercontent.com/106053283/214072632-1ff3609b-c420-4076-8cc6-66dec54a3ce2.png">  
Although unconfirmed, any image in the format of the sample image will be visualized.  

## SampleResult  
The sample source has a resolution of 64, but the results shown here are with a resolution of 256.  
### FirstOrder  
<img width="1000" alt="sampleLungFirstOrder" src="https://user-images.githubusercontent.com/106053283/214075495-3af06272-c580-4dda-a386-ca0ebe3981a7.png">

### GLCM  
![sampleLungGLCM](https://user-images.githubusercontent.com/106053283/214076866-731cbd08-336d-4466-9ba0-7fb565f1d922.png)

### GLDM  
<img width="1000" alt="sampleLungGLDM" src="https://user-images.githubusercontent.com/106053283/214075670-67801201-aab5-49fc-8a37-b5c9f2eecfbf.png">

### GLRLM  
<img width="1000" alt="sampleLungGLRLM" src="https://user-images.githubusercontent.com/106053283/214075725-3c06cbbf-c377-4cd0-892b-bf73b178b27f.png">

### GLSZM  
<img width="1000" alt="sampleLungGLSZM" src="https://user-images.githubusercontent.com/106053283/214075870-fed04024-cd36-4a39-9f43-991135e03867.png">

### NGTDM  
<img width="1000" alt="sampleLungNGTDM" src="https://user-images.githubusercontent.com/106053283/214075800-d31d0044-d055-45fe-ba6e-676b08a8e034.png">

Note that features related to shape cannot be visualized with this tool, although it is obvious.
