import subprocess, os, shutil
from django.http import HttpResponse
from tkinter import filedialog, messagebox
from django.shortcuts import render
from csv import DictReader
import tkinter as Tk

#Função para renderizar o primeiro template
# def sobre(request):
#     return render(request, 'core/dowloads.html')
#-----------------------------------------------------------------------------------------------------    
#Função para renderizar o primeiro template
def home(request):
    return render(request, 'core/index_2.html')

def clear(request):
    termo = os.system("cd static/deepfacelab && start arquivo_clear.bat")
    return render(request, 'core/index_2.html')
#-----------------------------------------------------------------------------------------------------    
def video_audio(request):
    return render(request, 'core/video_audio.html')
#-----------------------------------------------------------------------------------------------------    
def index(request):
    return render(request, 'core/index.html')
#-----------------------------------------------------------------------------------------------------    
def down(request):
    return render(request, 'core/dowloads.html')
#-----------------------------------------------------------------------------------------------------
def sobre(request):
    return render(request, 'core/sobre.html')
#-----------------------------------------------------------------------------------------------------  
#enviar_depoimento
def enviar_depoimento(request):
    #Solicitar o arquivo
    orig = filedialog.askopenfilename()
    
    if orig == "":
        messagebox.showinfo(title='Arquivo não recebido', message='Arquivo não carregado!' )
        return render(request, 'core/index_2.html')
    
    #Salvar o path do arquivo
    with open(os.path.join('static', 'txt' ,'diretorio_o.csv'), 'w') as dirorg:
        dirorg.write('origem\n')
        dirorg.write(f'{orig}')
    
    with open(os.path.join('static', 'txt' ,'diretorio_d.csv')) as dircsv:
        reader = DictReader(dircsv)
        for linha in reader:
            csv = linha['destino']
        
    with open(os.path.join('static', 'txt' ,'diretorio_o.csv')) as dirorg:
        reader = DictReader(dirorg)
        for linha in reader:
            orig = linha['origem']
    
    if shutil.copyfile(orig, csv):
        messagebox.showinfo(title='Arquivo Recebido', message='Arquivo enviado com sucesso! Continue o processo!' )
    else:
        messagebox.showinfo(title='Arquivo não recebido', message='Arquivo não carregado!' )
        return render(request, 'core/index_2.html')
    
    return render(request, 'core/index_2.html')
#-----------------------------------------------------------------------------------------------------    
#Gerar a ata
def gerar_txt(request):
    termo = os.system("cd static/deepfacelab/workspace && python gera_ata.py")
    return render(request, 'core/traducao.html')
#-----------------------------------------------------------------------------------------------------    
def gerar_docs(request):
    return render(request, 'core/dowloads.html')
#-----------------------------------------------------------------------------------------------------    
#Executar script extrair face 1
def extract_face_um(request):
    termo = os.system("cd static/deepfacelab && start arq_1.bat")
    return render(request, 'core/index_2.html')
#-----------------------------------------------------------------------------------------------------    
#Executar script extrair face 2
def extract_face_dois(request):
    termo = os.system("cd static/deepfacelab && start arq_2.bat")
    return render(request, 'core/index_2.html')
#-----------------------------------------------------------------------------------------------------    
#Executar script sort
def src_sort(request):
    termo = os.system("cd static/deepfacelab && start arq_3.bat")
    return render(request, 'core/index_2.html')
#-----------------------------------------------------------------------------------------------------    
#Executar script extrair face dst
def extract_face_tres(request):
    termo = os.system("cd static/deepfacelab && start arq_4.bat")
    return render(request, 'core/index_2.html')
#-----------------------------------------------------------------------------------------------------    
#Executar script extrair face dst
def extract_face_quatro(request):
    termo = os.system("cd static/deepfacelab && start arq_5.bat")
    return render(request, 'core/index_2.html')
#-----------------------------------------------------------------------------------------------------    
#Treinamento
def treina(request):
    termo = os.system("cd static/deepfacelab && start arq_6.bat")
    return render(request, 'core/index_2.html')
#-----------------------------------------------------------------------------------------------------    
#merge rede
def merge_rede(request):
    termo = os.system("cd static/deepfacelab && start arq_7.bat")
    return render(request, 'core/index_2.html')
#-----------------------------------------------------------------------------------------------------    
#Merge mp4
def merge_mp4(request):
    termo = os.system("cd static/deepfacelab && start arq_8.bat")
    return render(request, 'core/index_2.html')