# Mall-Customer-Segmentation
# Mall Customer Segmentation

An unsupervised machine learning project for segmenting mall customers using K-Means clustering.

## 📌 Project Overview
This project was completed as part of the Data Mining course at ITI under the guidance of Eng. Khaled Shaker and Eng. Abdulrahman Ashour.

The goal of this project is to analyze mall customer data, perform exploratory data analysis, and apply K-Means clustering to group customers into meaningful segments. A web application is also built using Streamlit to make live predictions based on input features.

## 💡 Objectives
- Perform Exploratory Data Analysis (EDA)
- Preprocess data (nulls, duplicates, label encoding)
- Use K-Means clustering and find the optimal number of clusters (Elbow Method)
- Visualize clusters in 2D and 3D
- Build a Streamlit web app for real-time cluster prediction

## 📁 Dataset Description
The dataset contains the following columns:
- `CustomerID` – Unique identifier (dropped during preprocessing)
- `Gender` – Male/Female
- `Age` – Age of the customer
- `Annual Income (k$)` – Yearly income in thousands
- `Spending Score (1-100)` – Score assigned by the mall based on customer behavior

## 🛠️ Tech Stack
- **Languages**: Python
- **Libraries**: pandas, matplotlib, seaborn, scikit-learn, plotly, Streamlit
- **Model**: KMeans from scikit-learn
- **App**: Streamlit web app

## 🔍 Clustering Approach
1. **EDA & Preprocessing**: Null checks, duplicates removal, label encoding.
2. **Feature Selection**: Focus on `Annual Income (k$)` and `Spending Score (1-100)`.
3. **KMeans Clustering**: Applied KMeans with varying clusters (1–10).
4. **Elbow Method**: Optimal number of clusters found to be 5.
5. **Visualization**:
   - 2D scatter plots of clusters
   - 3D Plotly interactive scatter plots
6. **Web App**: Predicts cluster using trained model (`joblib`) and provides interpretation.

## 🚀 How to Run Locally
```bash
# Clone the repo
git clone https://github.com/MohamedAmmarAI/Mall-Customer-Segmentation.git
cd Mall-Customer-Segmentation

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## 🌐 Live Demo
👉 [Streamlit App](https://mall-customer-segmentation-ybkstwrcuv5jysbrpjxnqw.streamlit.app/)

## 📦 Repository Structure
```
Mall-Customer-Segmentation/
├── Mall_Customers.csv          # Dataset file
├── kmeans_model.pkl           # Trained model file
├── clustering_visuals.ipynb   # Data analysis and clustering code
├── app.py                     # Streamlit web application
├── README.md                  # Project overview
```

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/83198cad-4708-481f-b08b-104da5065cb7)

![image](https://github.com/user-attachments/assets/30659385-d0ea-4d50-9d41-5157e51bb5da)



## 🏷️ Tags
#DataMining #KMeans #CustomerSegmentation #Streamlit #Python #MachineLearning #Clustering #EDA #DataScience #DataAnalyst #PowerBI #DataEngineer #BusinessIntelligence

