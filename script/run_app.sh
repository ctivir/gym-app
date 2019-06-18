#!/bin/bash
clear
cd /home/ctivir/PycharmProjects/env  #path to your virtual environment
. bin/activate  #Activate your virtual environment
cd /home/ctivir/PycharmProjects/gym  #After that go to your project directory
python manage.py runserver  #run django server