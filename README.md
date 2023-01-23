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
![sampleLungFirstOrder](https://user-images.githubusercontent.com/106053283/214073206-0873b48e-057e-4761-a199-b69f41a1f500.png)

### GLCM  
