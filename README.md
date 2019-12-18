# Fake News Detection
[ INDP3 AIM - SUPCOM ] Project : Fake News Detection  
Realized by :  
• **Ihebeddine Riahi** : ihebeddine.riahi@supcom.tn  
• **Chaima Bouzaidi** : chayma.bouzaidi@supcom.tn  

## Table of contents
1. [Overview](#Overview)
2. [Requirements](#Requirements)
3. [Setting up the API](#Setup)  
4. [Start the App](#StartApp)


<a name="Overview"/>  

## Overview
This app allows a user to detect fake news.  

**How to do 🤔 ?**  
Let's have a look at the demo below 🤓:  

<p align="center">
    <img src="https://user-images.githubusercontent.com/53185260/71131550-4796f100-21f5-11ea-9832-94662f4b8de7.gif"  style="margin:15px">
</p>

So, It is easy The user paste the article in the text area and just click on `Predict`.  

To build this app, we followed this steps:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Training a machine learning model (Logistic Regression) on the dataset located in `\server\data`   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Building a user interface using React  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Building an API using Flask  

**NB**: To fit our dataset, we have done a benchmark of multiple models and chosen the one that gives the best performances  

<a name="Requirements"/>

## Requirements
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Node (v12.13.0)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Python (3.7.4)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • All Python packages specified in Python scripts  
 

<a name="Setup"/>

## Setting up the API
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Go to `server\` directory and run `app.py` script in order to start the API  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • You have to get the pickle of our trained model from Dropbox: `https://www.dropbox.com/s/r2bhfdvzb7rb99k/model.pkl?dl=0` and store in in `server\model` directory  
**NB** : Keep in mind that when you first run the `app.py` script, the machine learning model (~350MB) will be loaded into your machine RAM  
  


<a name="StartApp"/>

## Start the App  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Go to `fakenews-ui\` directory and run **npm install && npm start** to start the App  