# +MEDIC
A Whatsapp Bot developed by **Team Quasar** for HackCBS 2021. 
<br>
As in emergency it's quite hard to search for an ambulance, hospital in google or to download new health related apps from PlayStore/Appstore. Also nowadays almost everyone have a Whatsapp account, so we thought to build a WhatsApp Bot which will arrange ambulance in no time.

## Inspiration
According to NIEM almost 20 % of patients die due to traffic delays, & in year 2016 only 1.4 lakh people died in road accident out of which almost 30% died due to late arrival of Ambulance.
<br>
So we came up with this idea to build a WhatsApp Bot which will help a user to contact an Ambulance, Hospital & nearby Police Station in no time.

## Web Page:

We have created this web page to guide people about to use the bot in times of need: [Visit Here](https://cutt.ly/rRCQRDK)
<br>
Below are few glimpses of it: 
<details>
<summary>Image 1</summary>
<br>
  
![image](https://user-images.githubusercontent.com/74824675/139568257-9806017c-009d-4aa2-b0a3-d86a5df7f63f.png)
</details>

<details>
<summary>Image 2</summary>
<br>
  
![image](https://user-images.githubusercontent.com/74824675/139568291-68008154-4f05-4c0c-a5eb-61f22f71de22.png)
</details>

<details>
<summary>Image 3</summary>
<br>
  
![image](https://user-images.githubusercontent.com/74824675/139568363-ce995175-a58f-4954-84d3-844dc25b3443.png)
</details>

<details>
<summary>Image 4</summary>
<br>
  
![image](https://user-images.githubusercontent.com/74824675/139568349-226632df-6cec-435e-8bbc-a54779671dd9.png)
</details>


## What it does:
It asks a WhatsApp user to share his/her 'current location' and according to that it searches for nearby Ambulances & shares that patient's complete details (with live location)   to the nearest Ambulance.
<details>
<summary>Image Here</summary>
<br>
  
![image](https://user-images.githubusercontent.com/74824675/139565134-f262a6e5-f38e-477f-9221-de6b2f02a7a4.png)
</details>

And then it searches for nearest hospital (with highest rating in google) within a given radius & shares that data with the ambulance & patient as destination (with distance &     estimate driving time) in a single WhatsApp message.
<details>
<summary>Image Here</summary>
<br>
  
![image](https://user-images.githubusercontent.com/74824675/139565142-7a216e04-7e43-47f4-a819-788527b31553.png)
</details>

And then it searches for nearest police station to Hospital & nearest police station to the Patient and asks both of them to clear road jam between Ambulance Location - Patient Location & Patient Location - Hospital Location , and shares ambulance's complete details (eg. Number Plate Details) with pick up & drop off location.
<details>
<summary>Image Here</summary>
<br>
  
![image](https://user-images.githubusercontent.com/74824675/139565160-313b9b8c-f08a-45e2-a923-ef5f1bb5498a.png)
</details>

## How we built it:
We built it using `Flask`, `Twilio`, `Google API`and to access csv datas we have used pandas.

## User Manual

`pip install twilio`
<br>
`pip install Flask`
<br>
`pip install requests`

For Twillo:
<br>
* Login / Create using email or mobile number.
* Click on: Develop -> Messaging -> Try it out -> Send a Whatsapp Message
* Send your activation code (eg.: join...) to +14155238886

For Google API:
* Login using Google
* Create a `project`
* Create --> `Billing Account` --> Wait for Verification
* Search --> `Geocoding API` --> Enable it ---> Copy --> `API KEY`
* Search --> `Places API` --> Enable it ---> Copy --> `API KEY` Search --> `Distance MAtrix API` --> Enable it ---> Copy --> `API KEY`

Download **ngrok**
* Unzip the file
* open `terminal` from `Downloads` or where you have saved that file
* paste `./ngrok http 5000` inside your terminal & press enter
* Copy --> Forwarding No.1 (eg. http://..........ngrok.io) --> & Paste that [here](https://console.twilio.com/us1/develop/sms/settings/whatsapp-sandbox?frameUrl=%2Fconsole%2Fsms%2Fwhatsapp%2Fsandbox%3Fx-target-region%3Dus1) [When A Message Comes In Box]
* Copy --> Forwarding No.2 (eg. http://..........ngrok.io) --> & Paste that [here](https://console.twilio.com/us1/develop/sms/settings/whatsapp-sandbox?frameUrl=%2Fconsole%2Fsms%2Fwhatsapp%2Fsandbox%3Fx-target-region%3Dus1) [Status Callback URL]

