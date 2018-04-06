# 머신러닝/딥러닝을 위한 Python

## 강의개요
본 강의는 머신러닝, 딥러닝을 배우기 위해 기본적으로 이해해야하는 Python을 다룹니다.  빠른 시간 내에 Python 기초 문법을 복습하고 머신러닝, 딥러닝의 근간을 이루는 Numpy, Pandas와 친숙해지고 싶은 분에게 추천합니다. 참고 - [머신러닝/딥러닝을 위한 Python](https://blog.naver.com/con9755/221186922122)

## 강의정보
* 강좌명: 머신러닝/딥러닝을 위한 Python
* 강의자명: 가천대학교 산업경영공학과 최성철 교수 (sc82.choi@gachon.ac.kr, Director of [TEAMLAB](http://theteamlab.io/))
* Email: teamlab.gachon@gmail.com

## 강의구성
### Chapter 0 - Environment setup
- 파이썬 설치 - [강의영상](https://www.youtube.com/watch?v=OMuHLDvmQl4&list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz&index=4)
- Atom 설치
  - windows - [강의영상](https://www.youtube.com/watch?v=8Z6_JSvKux0&list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz&index=7), [설치문서](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/desc/atom_windows.md)
  - Mac - [강의영상](https://www.youtube.com/watch?v=XYvP4NeFo0Y&list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz&index=9), [설치문서](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/desc/atom_macos.md)
- Python Ecosystem for Machine Learning - [강의영상](https://youtu.be/zpPEA_XZ7IU?list=PLBHVuYlKEkUIbVgM5H_9fh7cE9u45fR1J)
##### Package installation
```bash
conda create -n ml_python python=3.5
conda install numpy seaborn scikit-learn jupyter
conda install nltk gensim matplotlib
```

### Chapter 1 - Pythonic Code
- Pythonic Code Overview
- Split & Join
- List Comprehension
- Enumerate & Zip
- Map & Reduce
- Asterisk
- Lab: Simple Linear algebra concepts
- Lab: Simple Linear algebra codes
- Assignment: [Linear algebra with pythonic code](https://github.com/blissray/connect_python/tree/master/lab_assignments/lab_1)
- Assignment: [연산자 끼워넣기](https://www.acmicpc.net/problem/14891)
- Assignment: [톱니바퀴](https://www.acmicpc.net/problem/14891)

### Chapter 2 - Numpy section
- Numpy overview
- ndarray
- Handling shape
- Indexing & Slicing
- Creation functions
- Opertaion functions
- Array operations
- Comparisons
- Boolean & fancy Index
- Numpy data i/o
- Assignment: Numpy in a nutshell

### Chapter 3 - Pandas section
- Pandas overview
- Series
- DataFrame
- Selection & Drop
- Dataframe operations
- lambda, map apply
- Pandas builit-in functions
- Lab Assignment: Build a matrix
- Groupby I
- Groupby II
- Casestudy
- Pivot table & Crosstab
- Merg & Concat
- Database connection & Persistance

### Chapter 4 - OOP section
- Objective oriented programming overview
- Objects in Python
- Lab: Note and Notebook
- OOP characteristics
- Decorators, Static And Class Methods
- Abstract Classes

### Chapter 5 - Linear regression
- Linear regression overview
- Cost functions
- Linear Equality
- Gradient descent approach
- Linear regression wtih gradient descent
- Linear regression wtih Numpy
- Multivariate linear regression models
- Multivariate linear regression with NumPy
- - Regularization - L1 and L2
- Implementation of generalization with NumPy
- Linear regression with sklearn

### Chapter 6 - Logistic regression
- Logistic regression overview
- Sigmoid function
- Cost function
- Logistic regression implementation with Numpy
- Maximum Likelihood estimation
- Regularization problems
- Logistic regresion with sklearn
- Softmax fucntion for Multi-class classification
- Cross entropy loss function
- Softmax Logistic Regression
- Performance measures for classification


## References
- [K-MOOC: 데이터 과학을 위한 파이썬 입문](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC)
- [Operation Research with Python Programming](https://github.com/TeamLab/Gachon_CS50_OR_KMOOC)
