from rest_framework import serializers
from authentication.models import Student, Teacher, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', )

class TeacherSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()
    name = serializers.CharField(source = 'get_full_name')
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'subjects')
    def get_subjects(self, obj):
        sub_list =[]
        for i in obj.subjects.all():
            sub_list.append(i.name)
        return sub_list if len(sub_list) > 0 else None
        

class StudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='get_full_name')
    teachers = TeacherSerializer(many = True)

    class Meta:
        model = Student
        fields = ('student_name','id', 'teachers')