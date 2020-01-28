# Fake News Classifier

In this job, I collaborated with <a href="https://github.com/IhebeddineRyahi">Ihebeddine RYAHI</a>

## Table of contents
1. [Overview](#Overview)
2. [Requirements](#Requirements)
3. [Setting up the API](#Setup)  
4. [Start the App](#StartApp)


<a name="Overview"/>  

## Overview
In this project, we built an end to end fake news classifier. This starts from training a machine learning classifier to deploying a web app.😀  

**How to do 🤔?**

First of all, let's have a look how the app looks like 🤓:  

<p align="center">
    <img src="https://user-images.githubusercontent.com/53185260/71131550-4796f100-21f5-11ea-9832-94662f4b8de7.gif"  style="margin:15px">
</p>

As you see, this web app allows a user to detect either an article is fake or real news. To do, the user just pastes the article in the text area and click on `Predict`. 

**NB** : You can add some articles in the test dataset file : `server/data/fake_or_real_news_testset.csv`  

To build this app, we followed this main steps:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Training a machine learning classifier (Logistic Regression)    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Building an interactive web app using `React.js`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Setting a `REST API` using `Flask`  

<a name="Requirements"/>

## Requirements
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Node.js (version 12.13.0)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Python (version 3.7.4)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Flask : `pip install flask`  
 
<a name="Setup"/>

## Setting up the API
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Go to `server\` directory and run `app.py` script in order to start the API  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • You can get the pickle of our trained model from Dropbox: `https://www.dropbox.com/s/r2bhfdvzb7rb99k/model.pkl?dl=0` and store it in `server\model` directory  
**NB** : Keep in mind that when you first run the `app.py` script, the machine learning model (~350MB) will be loaded into your machine RAM  
  


<a name="StartApp"/>

## Start the App  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Go to `client\` directory and run **npm install && npm start** to start the App  
