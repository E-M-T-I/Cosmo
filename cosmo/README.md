<!-- Heading -->
# COSMO VOICE FEATURE

Cosmo is the main Django project.
Cosmoapp and howdy are two apps in this project
Cosmoapp is an inbuilt app when I created the Django project.
Howdy is a manually created an app
Used venv and venv6 virtual environments.
In the howdy app, views.py is the main file.

Packages:
Speech Recognition
Pyaudio
gTTS
Playsound 
os
Imported these all packages on the views.py file.

Created a class named as VoiceFeature for implementing speech recognition code. This is the main class. Defined three functions in this class as record_audio, alexis_speak, respond.

Templates:
index.html : Added button in this file.
about.html

Run the "python manage.py runserver" command to use this voice feature.
