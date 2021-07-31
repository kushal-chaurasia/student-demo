from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate
from .utils import get_token
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer

# Create your views here.

class LoginView(APIView):
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        output_status = False
        output_detail = 'failed'
        output_data = {}
        res_status = HTTP_400_BAD_REQUEST
        username =  request.data.get('username', None)
        password =  request.data.get('password', None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                output_status = True
                output_detail = 'Success'
                res_status = HTTP_200_OK
                output_detail = get_token(user)
            else:
                output_detail = 'invalid username or password'
        else:
            output_detail = 'Please provide both username and password'
        context = {
            'status' : output_status,
            'detail' : output_detail,
            'data' : output_data,
        }
        return Response(context, status=res_status, content_type='application/json')


class StudentView(APIView):
    def get(self, request, *args , **kwargs):
        output_status = False
        output_detail = 'failed'
        res_status = HTTP_400_BAD_REQUEST
        output_data = {}
        user = request.user
        studen_obj = Student.objects.filter(user=user).first()
        if studen_obj:
            output_status = True
            output_detail = 'Success'
            res_status = HTTP_200_OK
            output_data = StudentSerializer(studen_obj).data
        else:
            output_detail = 'No student found'
        context = {
            'status' : output_status,
            'detail' : output_detail,
            'data' : output_data,
        }
        return Response(context, status=res_status, content_type='application/json')

class TeacherView(APIView):
    def patch(self, request):
        output_status = False
        output_detail = 'failed'
        res_status = HTTP_400_BAD_REQUEST
        subject = request.data.get('subject', None)
        output_data = {}
        user = request.user
        teacher_obj = Teacher.objects.filter(user=user).first()
        if teacher_obj and subject:
            teacher_obj.update_subjects(subject)
            output_status = True
            output_detail = 'Success'
            res_status = HTTP_200_OK
            output_data = TeacherSerializer(teacher_obj).data
        else:
            output_detail = 'Invalid Request'
        context = {
            'status' : output_status,
            'detail' : output_detail,
            'data' : output_data,
        }
        return Response(context, status=res_status, content_type='application/json')

def show_report(request):
    obj = Student.objects.all()
    if obj:
        context = {'obj' : obj}
    return render(request, 'authentication/report.html', context)

