# Extensions-of-Fisher-s-method
In statistics, extensions of Fisher's method are a group of approaches that allow approximately valid statistical inferences to be made when the assumptions required for the direct application of Fisher's method are not valid. Fisher's method is a way of combining the information in the p-values from different statistical tests so as to form a single overall test: this method requires that the individual test statistics (or, more immediately, their resulting p-values) should be statistically independent.（ref:https://en.wikipedia.org/wiki/Extensions_of_Fisher%27s_method)

## Fish’s method with weight and under statistics dependence condition

### Usage


import efm

f = efm.model(p,w,c) #Initialize Fish’s method

f.org() #Application to independent test statistics

f.dep() #Extension to dependent test statistics

f.wei() #Extension to weighted test statistics
 
f.depwei() #Extension to dependent and weighted test statistics

### Method
Defining the statistic that followed a chi-squared distribution with 2 degrees of freedom,

![image](http://www.sciweavers.org/upload/Tex2Img_1544173326/eqn.png)

When introducing weight(w), the overall p-value corresponding T-statistic followed a chi-squared distribution with 2n degrees of freedom and can be approximated by scaled chi-squared distribution,

![image](http://www.sciweavers.org/upload/Tex2Img_1544174689/eqn.png)

Considering statistics aren't independent, when estimating the parameters, the covariance matrix can be expressed as[1],

![image](http://www.sciweavers.org/upload/Tex2Img_1544175306/eqn.png)

where

![image](http://www.sciweavers.org/upload/Tex2Img_1544175683/eqn.png)

and

![image](http://www.sciweavers.org/upload/Tex2Img_1544175547/eqn.png)

Rho hat is the Pearson correlation coefficient between test statistics

Using the method of moments, the parameters can be estimated as,

![image](http://www.sciweavers.org/upload/Tex2Img_1544241135/eqn.png)

![image](http://www.sciweavers.org/upload/Tex2Img_1544241211/eqn.png)


[1] Yang, J.J. Distribution of fisher's combination statistic when the tests are dependent. J Stat Comput Sim 2010, 80, 1-12.
