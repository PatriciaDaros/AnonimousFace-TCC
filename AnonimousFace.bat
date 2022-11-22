@echo off
start /b pip install python
start /b pip install django
cd novoAmbiente/Scripts
start /b activate 
start chrome "http://127.0.0.1:8000/"

pause