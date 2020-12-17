# WorkBC API

### Setting Up Your Environment

    You can edit and run the file in visual studio, however I reccomend Pycharm community,
    it allows you to use the pyhton console as well so you can replicate the api requests.
    it can be found here: https://www.jetbrains.com/pycharm/download/#section=windows 

### Cloning Your Repo

    open your Command prompt, or powershell and navigate to where you'd like
    your repo to be held (i.e. User/username/gitProjects/) from here you can run the command: 

        git clone https://github.com/bcgov-elmsd/workbc-helpbot.git

### Open and Run Code

    Open Visual Studio or Pycharm which you installed when setting up your environment and
    open your workbc-helpbot project. in the terminal your going to need to ensure you're 
    running atleast python 3.7  you can check using python --version. You will also need pip
    to execute the following command:
        
        pip install flask, keras, tensorflow, nltk, pickle-mixin
    
    Once those modules are installed you can run:
       
       python train_chatbot.py
    
    to create the h5 and pkl files for the chatapp.py script.
    Note: you will see some error messages, they can be ignored they're not neccessary
    to run the script. 
    now you can either run:
       
       python chatgui.py
            or
        python App.py
     
    the chatgui.py will open a gui for you to test the AI's responses,
    the app.py will run the api which you can test either in at http://127.0.0.1:5000/
    by adding a phrase or word to the end i.e. http://127.0.0.1:5000/thank%20you which will show
    the response on the webpage. or you can use the python console using the request:
       
       requests.get("http://localhost:5000/Thanks").text
            or
        r = requests.get("http://localhost:5000/Thanks")
        r.text
### Code References
    ![picture](https://github.com/bcgov-elmsd/workbc-helpbot/blob/main/HelpbotCode.png)
    
### Using Git Command-line

    When editing the project use your own branch, you can create a new branch by using  the command:

        git checkout -b newBranch

    this will automatically replicate your project and put you on your new branch called "newBranch".
    To commit your local work to your remote branch you can need to first save your changes locally 
    then add your changes to your commit using one of the following commands:

        // this adds all of the files you've changed
        git add -A  
        
        // will add the file specified to your commit
        git add filename

    to commit the file you've added you can either create a large or small note using one of the two commands:

        // when submitting a small message about your commit contents
        git commit -m "This is my commit message"   

        // when submitting a detailed message about your commit
        git commit
        // this will open your vim editor so you can create a larger commit message.

    finally to push your commit to your remote branch you use the following command:

        git push origin newBranch

    This will push your changes to your remote branch and if you'd like to merge it with the master 
    or main branch you can visit the https://github.com/bcgov-elmsd/workbc-helpbot repo and create a 
    "new pull request" for the members to review and approve.

    If you're ever locally your branch does not auto update so it you want the latest version of the project you can use the command:

        git pull origin main

    Some more references for git:

        cheat sheet - https://education.github.com/git-cheat-sheet-education.pdf
        Common git issues - https://www.codementor.io/@citizen428/git-tutorial-10-common-git-problems-and-how-to-fix-them-aajv0katd
        
        
   ### License
   
        Copyright 2020 Province of British Columbia

        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this file except in compliance with the License.
        You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.
