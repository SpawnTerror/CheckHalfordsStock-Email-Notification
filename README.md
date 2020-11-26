# About

**halfords-check-stock-send-email**

Overcomplicated Python3.9 script to check stock availablity using 'add to basket' button.
Written to enable me to check if the item I want is already purchasable, as the website is
old and doesn't offer Email Notification.

# Requirements

- **virtual environment**
Install and enable venv before installing anything, like selenium:  
>sudo python3 -m venv env
>source venv/bin/activate

- **selenium==3.141.0**   
selenium library, install requirements.txt with:  
> pip install -r requirements.txt

- **config.py**  
create this file next to check_stock.py and insert these lines replacing what's quoted:  
>mailToAddress = "your_email"  
>mailFromAddress = "sender_email_account"  
>mailFromServer = "smtp.gmail.com:587"  
>mailFromPassword = "less_secure_apps_passowrd"  

# Contact / Questions  
  
Contact me at blackbox.spawnterror.com
