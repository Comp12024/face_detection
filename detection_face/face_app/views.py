from django.http import HttpResponse
from django.shortcuts import render
from face_app.models import *
import face_recognition
from PIL import Image, ImageDraw
import pickle

from face_app.forms import RegisterUserForm


# def compare_faces(img1_path, img2_path):
#     img1 = face_recognition.load_image_file(img1_path)
#     img1_encodings = face_recognition.face_encodings(img1)[0]
#     # print(img1_encodings)
#
#     img2 = face_recognition.load_image_file(img2_path)
#     img2_encodings = face_recognition.face_encodings(img2)[0]
#
#     result = face_recognition.compare_faces([img1_encodings], img2_encodings)
#     # print(result)
#
#     if result[0]:
#         print("Welcome to the club! :*")
#     else:
#         print("Sorry, not today... Next!")


def index(request):
    username = User.objects.all()
    # img1 = face_recognition.load_image_file("face_app/dataset/stat.png")
    # img1_encodings = face_recognition.face_encodings(img1)[0]
    # # print(img1_encodings)
    #
    # img2 = face_recognition.load_image_file("face_app/dataset/regina_2.jpg")
    # img2_encodings = face_recognition.face_encodings(img2)[0]
    # # print(img2_encodings)
    #
    # result = face_recognition.compare_faces([img1_encodings], img2_encodings)
    # # print(result)
    #
    # if result[0]:
    #     print("Welcome to the club! :*")
    # else:
    #     print("Sorry, not today... Next!")
    data = {
        'username': username,
    }
    return render(request, 'face_app/index.html', data)


def date_user(request, user_id):
    return render(request, 'face_app/date.html')


def page_not_found(request, exception):
    return HttpResponse('<h1>Страница не найдена!</h1>')


def registration(request):
    form = RegisterUserForm()
    return render(request, 'face_app/registration.html', {'form': form})

