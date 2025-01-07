# Signal Fingerprint
![alt text](screenshots/home.png)


## Description

- Desktop Application Designed For Identifying Music By Analyzing Its Unique Intrinsic Features
- This Application Mimics The Functionality Of Shazam
- Allows Identifying Audio Composed Of 2 Different Songs

## Tech Stack Used

|**Functionality** | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)|
|--- | --- |
|**UI** | ![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)|
|**Styling** | [![CSS](https://img.shields.io/badge/CSS-1572B6?logo=css3&logoColor=fff)](#)|

## Demo

https://github.com/user-attachments/assets/d4f41313-98ee-4964-8df0-78ed5dac24ad

## How It Works
- Split Each Song In Our Dataset Into 3 Audio Files, Consisting Of Original Song, Instruments Only, Vocals Only
- Generate Spectrogram For Each Audio File In Our Dataset `data` directory
- Extract Specific Features From The Spectrogram
- Normalize & Specular Hash Each Feature
- Save The Hashed Features Of Each Audio File
- Run The Application And Browse Any Song
- Compare The Hashed Features Of the Browsed Song With Our Hashed Dataset `hashed` directory


## Installation

1. Make Sure That Pip & Python Are Installed On Your System

2. Clone The Repo Onto Your Local System or Download The Zip File & Extract It
   ```bash
    git clone https://github.com/mostafa-aboelmagd/signal-fingerprint.git
    ```

3. Nagivate To The Project's Directory 
   
4. Install The Required Libraries
    ```bash
    pip install -r requirements.txt
    ```

5. Run `main.py` File
    ```bash
    python MainWindow.py
    ```

## Contributors

| Name | GitHub | LinkedIn |
| ---- | ------ | -------- |
| Mostafa Ayman | [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/mostafa-aboelmagd) | [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mostafa--aboelmagd/) |
| Ali Zayan | [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/alizayan684) | [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/%D8%B9%D9%84%D9%8A-%D8%B2%D9%8A%D8%A7%D9%86-%F0%9F%94%BB%F0%9F%87%B5%F0%9F%87%B8-b98239264/) |
| Zeyad Amr | [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/Zisco2002)| [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zeyad-amr-3506b225b/) |
| Mostafa Mousa | [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/MostafaMousaaa) | [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mostafa-mousa-b81b8322a/) |
| Omar Khaled | [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](#)| [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/omar-khaled-064b7930a/) |
