
If the video from criterion D is insufficient for product demonstration, please feel free to follow the steps as mentioned to deploy the website.

1. Make sure you have VSCode downloaded
2. Ensure that Python (preferably version 3.8 or later) is installed on your device. Youcan download Python from the official site - https://www.python.org/downloads/
3. After installation, verify the installation by opening a terminal (or command prompt) and running:   python --version
4. Install pip (if it's not already installed): pip is the Python package installer. It should come pre-installed with Python, but in case it’s missing, run the following command:     python.exe -m install --upgrade pip
5. You will also need to install Pillow to run static variables so run the command: python -m pip install Pillow
6. I have included a requirements.txt through which you can install the project dependencies listed using: pip install -r requirements.txt
   But if the terminal gives you an error just ignore step 6 it should not ve requrired. I have covered all installations in other steps


   Now that all the pre-requisites have been established you should navigate to the Project folder. 
   1. To do that, extract the .zip file, and open the folder named 'Product' in your code editor.
   2. use the command 'cd' to navigate into the application within your terminal: cd .\scents_website\
   3. run the command: python -m venv venv
      by making a virtual environment through the above step you will activate the django framework
   4. Now run the command: python manage.py runserver
   5. then your terminal should take you to the development server @ http://127.0.0.1:8000/
      Now you can see the deployed website
   
   6. To add products as the owner of the website create a superuser using the following command: python manage.py createsuperuser
      follow the steps to make your credentials and open a new tab in your browswer: http://127.0.0.1:8000/admin
   7. Log in using your new credentials
   8. In the Django admin panel, go to the "Products" section. Add products as needed and refresh the products page to see them on the website.


