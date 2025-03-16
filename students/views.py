from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Create a new student
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

# Update student details
def student_update(request, id):
    student = get_object_or_404(Student, id=id)  # Get the student or show 404
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)  # Pass instance to edit
        if form.is_valid():
            form.save()
            messages.success(request, "Student details updated successfully!")
            return redirect("student_list")  # Redirect after successful update
        else:
            messages.error(request, "Please correct the errors below.")  # Show error message
    else:
        form = StudentForm(instance=student)  # Prefill form with student data

    return render(request, "student_form.html", {"form": form})

# Delete a student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_detail.html', {'student': student})
