# -*- coding: utf-8 -*-
"""Automação leitura email.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FexaFOan0YzNuaq43RkrXjCPbEnlfZIF
"""

!pip install imbox
import os
from google.colab import auth, drive
from google.auth import default
import os.path
from imbox import Imbox
import json

# Dados de acesso
#host = 'Automação - Email' # This is likely not a valid hostname for your email provider.
host = 'imap.gmail.com' # Change to the correct hostname for your email provider.
email = ['seuemail']
password = ['suasenha']

# Conectando ao serviço de email
with Imbox(host, username=email[0], password=password[0]) as imbox: # Accessing the list elements directly
    # Aqui você pode realizar ações como ler e enviar emails
    if unread_messages:= imbox.messages(unread=True):
      for uid, msg in unread_messages: # Iterate through unread_messages, getting uid and message object
        imbox.mark_seen(uid) # Mark the current message as read using its uid