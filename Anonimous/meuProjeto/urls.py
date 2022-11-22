from django.contrib import admin
from django.urls import path, include, re_path
from meuProjeto.view import home, sobre, clear, down, video_audio, index, gerar_docs, extract_face_um, gerar_txt, src_sort, extract_face_tres, extract_face_quatro,treina, enviar_depoimento, extract_face_dois, merge_rede, merge_mp4

urlpatterns = [
    path('', include('core.urls')),
    path('', index, name = "index"),
    path('video_audio', video_audio, name = "video_audio"),
    path('sobre', sobre, name = "sobre"),
    path('down', down, name = "down"),
    
    path('clear', clear),
    path('extract_face_dois', extract_face_dois),
    path('extract_face_um', extract_face_um),
    path('src_sort', src_sort),
    path('extract_face_tres', extract_face_tres),
    path('merge_rede', merge_rede),
    path('merge_mp4', merge_mp4),
    path('treina', treina),
    path('extract_face_quatro', extract_face_quatro),
    path('enviar_depoimento', enviar_depoimento),
    path('gerar_txt', gerar_txt),
    path('gerar_docs', gerar_docs),
]