# Parameter Optimization of SVM Using Dry Bean Dataset
This repository contains code for parameter optimization of Support Vector Machines (SVM) using the Dry Bean Dataset. The dataset is a multi-class classification problem with 17 features and 7 classes. The goal of this project is to find the best parameters for the SVM model in order to achieve the highest accuracy possible. <br>
### Dataset
The Dry Bean Dataset consists of 13611 instances with 16 attributes, including 17 feature attributes, 1 ID attribute, and 2 quality attributes. The dataset is publicly available at the UCI Machine Learning Repository. The features include geometric shape, form, and structure features of the beans that are important in selecting high-quality beans. The dataset is preprocessed and ready to be used for classification tasks.<br>
### 1. Number of Instances: 13611
### 2. Number of Attributes: 17
### 3. Attribute Information:<br>

1.) Area (A): The area of a bean zone and the number of pixels within its boundaries.<br>
2.) Perimeter (P): Bean circumference is defined as the length of its border.<br>
3.) Major axis length (L): The distance between the ends of the longest line that can be drawn from a bean.<br>
4.) Minor axis length (l): The longest line that can be drawn from the bean while standing perpendicular to the main axis.<br>
5.) Aspect ratio (K): Defines the relationship between L and l.<br>
6.) Eccentricity (Ec): Eccentricity of the ellipse having the same moments as the region.<br>
7.) Convex area (C): Number of pixels in the smallest convex polygon that can contain the area of a bean seed.<br>
8.) Equivalent diameter (Ed): The diameter of a circle having the same area as a bean seed area.<br>
9.) Extent (Ex): The ratio of the pixels in the bounding box to the bean area.<br>
10.)Solidity (S): Also known as convexity. The ratio of the pixels in the convex shell to those found in beans.<br>
11.)Roundness (R): Calculated with the following formula: (4piA)/(P^2)<br>
12.)Compactness (CO): Measures the roundness of an object: Ed/L<br>
13.)ShapeFactor1 (SF1)<br>
14.)ShapeFactor2 (SF2)<br>
15.)ShapeFactor3 (SF3)<br>
16.)ShapeFactor4 (SF4)<br>
17.)Class (Seker, Barbunya, Bombay, Cali, Dermosan, Horoz and Sira)<br>
### Requirements
To run the code in this repository, you will need to have the following libraries installed:<br>
1. scikit-learn<br>
2. pandas<br>
3. numpy<br>
4. matplotlib<br>
5. seaborn<br>
### Usage
The repository contains a Jupyter notebook (svm_drybean.ipynb) that walks through the process of parameter optimization for SVM using the Dry Bean Dataset. The notebook includes detailed explanations and comments for each step of the process.<br>
To run the notebook, you can simply open it in Jupyter and run the cells one by one. You can also run the notebook in Google Colab or any other similar environment.
<br>
### Results
The results of the parameter optimization process are summarized in the notebook. The best parameters for the SVM model were found using GridSearchCV and resulted in an accuracy of 97.8%.<br>
### Scatter Plot
![Scatter Plot](https://github.com/j-sonali2003/Predictive-Analysis-/assets/130656646/fd33bde3-00aa-4a21-92b6-1515a7d46c01)
<br>
### Histogram
![Histogram](https://github.com/j-sonali2003/Predictive-Analysis-/assets/130656646/8b1829f0-5050-44af-be13-fcb0d7725bea)
<br>
### Box Plot
![Box Plot](https://github.com/j-sonali2003/Predictive-Analysis-/assets/130656646/91268788-b8cd-4899-8710-f60b01837573)
<br>
### Accuracy Plot
![Accuracy Plot](https://github.com/j-sonali2003/Predictive-Analysis-/assets/130656646/e5eed17b-97c9-4eb0-a7e1-841c9c5fcdce)
