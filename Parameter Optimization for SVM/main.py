# Library Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm

# Read the CSV file
df = pd.read_csv("C:\\Users\\acer\\Desktop\\Thapar\\Subjects\\6th Semester\\UCS654 PREDICTIVE ANALYTICS USING STATISTICS\\PS Rana Ass\\Parameter Optimization Using SVM\\Dry_Bean_Dataset.csv", nrows=10000)

# Select columns of interest
cols_of_interest = ["Area", "Perimeter", "MajorAxisLength", "MinorAxisLength", "AspectRation", "Eccentricity", "ConvexArea", "Solidity", "Class"]
df = df[cols_of_interest]

# Convert the Class column to a factor
df["Class"] = pd.Categorical(df["Class"], categories=["SEKER", "BARBUNYA", "BOMBAY", "CALI", "DERMASON", "HOROZ", "SIRA"])

# Map the factor levels to numeric values
df["Class"] = df["Class"].cat.codes

# Check the structure of the dataset
df.info()

# Check for missing values
print(df.isnull().sum())

# Summary statistics
print(df.describe())

# Correlation matrix
print(df.corr())

# Histograms for each column
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 8))
for i, ax in enumerate(axes.flat):
    if i < len(df.columns)-1:
        ax.hist(df.iloc[:, i], bins=20)
        ax.set_title(df.columns[i])
plt.tight_layout()

# Boxplots for each column
df.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False, figsize=(10, 10))

# Scatterplot matrix
pd.plotting.scatter_matrix(df.iloc[:, :-1], figsize=(12, 8))
plt.suptitle("Scatterplot Matrix")
plt.show()

# Cross-tabulation of Class and Area
pd.crosstab(df["Class"], df["Area"])

# Mean of each column by class 
print(df.groupby("Class").mean())

# Initialize empty vectors to store iteration numbers and accuracies
iter_vec = []
accuracy_vec = []

# Create an empty data frame to store the results
results_df = pd.DataFrame(columns=['sample', 'accuracy', 'kernel', 'nu', 'epsilon'])

# Run the iterations on 10 samples
for sample_num in range(1, 11):
    #Variables Declaration
    bestAccuracy = 0
    bestKernel = ""
    bestNu = 0
    bestEpsilon = 0
    iteration = 1000
    kernelList = ['rbf', 'poly', 'linear', 'sigmoid']
    
    # Split the data into 70:30 train-test split
    X = df.iloc[:, :-1].values
    Y = df.iloc[:, -1].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)
    
    def fitnessFunction(k, n, e):
        # k stands for Kernel, n for Nu, e for Epsilon
        # Building the model
        model = svm.NuSVC(kernel=k, nu=n, gamma='auto', cache_size=1000)
        
        # Fitting the model
        model.fit(X_train, Y_train)
        
        # Prediction of Testing Dataset
        predicted = model.predict(X_test)
        
        # Model Evaluation Accuracy
        accuracy = round(np.mean(Y_test == predicted) * 100, 2)
        return accuracy  
    
    # Run the iteration loop for each sample
    for i in range(1, iteration+1):
        print("Sample:", sample_num, ", Iteration:", i)
        k = np.random.choice(kernelList)
        n = np.random.uniform()
        e = np.random.uniform()
        Accuracy = fitnessFunction(k, n, e)

        # Update best parameters if accuracy is higher than previous best
        if Accuracy > bestAccuracy:
            bestKernel = k
            bestNu = n
            bestEpsilon = e
            bestAccuracy = Accuracy
        bestAccuracy = max(Accuracy, bestAccuracy)

        # Append iteration number and accuracy to the vectors
        iter_vec = np.append(iter_vec, i + (sample_num-1)*iteration)
        accuracy_vec = np.append(accuracy_vec, bestAccuracy)

    # Add a new row to the results data frame
    new_row = pd.DataFrame([[sample_num, bestAccuracy, bestKernel, bestNu, bestEpsilon]], 
                           columns=['sample', 'accuracy', 'kernel', 'nu', 'epsilon'])
    results_df = pd.concat([results_df, new_row], ignore_index=True)

results_df.to_csv("results.csv", index=False)

# Find the sample with maximum accuracy
max_sample = np.argmax(results_df['accuracy'])

# Extract the iteration and accuracy vectors for the sample with maximum accuracy
max_iter_vec = iter_vec[(iter_vec > (max_sample - 1)*iteration) & (iter_vec <= max_sample*iteration)]
max_accuracy_vec = accuracy_vec[(iter_vec > (max_sample - 1)*iteration) & (iter_vec <= max_sample*iteration)]

# Plot the convergence graph
plt.plot(max_iter_vec, max_accuracy_vec, '-o')
plt.xlabel('Iteration')
plt.ylabel('Accuracy')
plt.show()