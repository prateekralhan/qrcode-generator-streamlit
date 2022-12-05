# ✨ QR Code Generator Streamlit 🚀 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)

A minimalistic webapp to generate QR Codes for the URLs fed in by the user

![Animation](https://user-images.githubusercontent.com/29462447/205723254-6f58404b-239b-4cd7-88ce-32d296dc7f33.gif)

## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the necessary dependencies.

## Usage:
1. Create a new folder `.streamlit` and create a file titled `config.toml` within it. Save this file with the following content:
```
[theme]
primaryColor="#2d4be0"
backgroundColor="#f9f4f4"
secondaryBackgroundColor="#e4edff"
textColor="#3a6ae4"
```
2. Navigate to the root of the folder and simply run the command: 
```
streamlit run app.py
```
2. Navigate to http://localhost:8501 in your web-browser.

![1](https://user-images.githubusercontent.com/29462447/205723396-4809e3ce-4a00-4f97-a708-ce75ed5fdfd5.png)


### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
