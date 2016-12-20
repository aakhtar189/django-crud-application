import json

from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from students.models import Student
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
from django.forms.models import model_to_dict


from django.core.urlresolvers import reverse
from students.forms import EditStudentForm
from students.utils import create_username


# Create your views here.
def homepage(request):
    students = Student.objects.all()
    query = request.GET.get('q', '')
    if query:
        students = students.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        )

    return render_to_response("student/homepage.html", {
        'query': query,
        'current': 'homepage',
        'students': students
    }, context_instance=RequestContext(request))


def profile(request, username):
    student = Student.objects.get(user__username=username)

    return render_to_response("student/profile.html",{
    'student':student
    }, context_instance=RequestContext(request))


def edit_student(request, username):
    student= Student.objects.get(user__username=username)

    if request.method == "POST":
        form = EditStudentForm(request.POST, request.FILES, instance=student)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user.first_name = form.cleaned_data["first_name"]
            obj.user.last_name = form.cleaned_data["last_name"]
            obj.user.email = form.cleaned_data["email"]
            obj.user.save()
            obj.save()

            return redirect(reverse("profile", kwargs={"username": student.user.username}))

        return render_to_response("student/edit_student",{
            "student": student,
            "form": form,
        }, context_instance=RequestContext(request))

    else:
        form = EditStudentForm(instance=student, initial={
            'first_name': student.user.first_name,
            'last_name': student.user.last_name,
            'email': student.user.email
        })

        return render_to_response("student/edit_student.html",{
            "form": form,
            "student": student
        }, context_instance=RequestContext(request))


def delete_student(request):

    if request.is_ajax():

        response = {"status": False, "errors": []}

        student_id = request.GET.get('student_id', '')

        student = Student.objects.get(id=student_id)

        student_id= student.id
        response["student_deleted"] = model_to_dict(student, fields=['username', 'id'])

        student.user.delete()

        
        response["status"] = True

        return HttpResponse(json.dumps(response))  
        


def create_student(request):
    if request.method == "POST":
        form = EditStudentForm(request.POST, request.FILES)

        if form.is_valid():
            user = User.objects.create(
                username=create_username('%s %s' % (form.cleaned_data["first_name"], form.cleaned_data["last_name"])),
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
            )

            student = Student.objects.create(
                user=user,
                gender=form.cleaned_data["gender"],
                address=form.cleaned_data["address"],
                country=form.cleaned_data["country"],
                nationality=form.cleaned_data["nationality"]
            )

            if request.FILES:
                student.avatar = request.FILES.get("avatar")
            student.save()

            return redirect("/")
    else:
        form = EditStudentForm()

    return render_to_response("student/edit_student.html", {
        "form": form,
        "current": "signup"
    }, context_instance=RequestContext(request))
