from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvluationSerializer


# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def tset(request):
    course_code = request.data.get("course_code", "")
    course_name = request.data.get("course_name", "")
    course_professor = request.data.get("course_professor", "")
    course_semester = request.data.get("course_semester", "")

    course = Course.objects.all()
    if course_code != "":
        course = course.filter(course_code=course_code)

    course = CourseSerializer(course, many=True).data
    return Response(course, status=200)
    # return render(request, "course.html", {"course": course})


@api_view(["POST"])
@permission_classes([AllowAny])
def create_course_evaluation(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"message": "no such objects"}, status=404)

    review = request.data.get("review", "")
    grade = request.data.get("grade", 3)
    password = int(request.data.get("password", 0000))

    evaluation = Evaluation.objects.create(
        course=course, grade=grade, review=review, password=password
    )

    evaluation = EvluationSerializer(evaluation).data
    print("!")
    return Response(evaluation, status=200)


# @api_view(["GET"])
# @permission_classes([AllowAny])
# def fetch_course_evaluation(request, course_id):
#     course_id = request.GET.get("course_id")
#     try:
#         course = Course.objects.get(id=course_id)
#     except Course.DoesNotExist:
#         return Response({"message": "no such objects"}, status=404)
#     evaluation = Evaluation.objects.filter(course=course_id)
#     return render(request, "detail.html", {"course": course, "evaluation": evaluation})


# def evaluation(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     return render(request, "evaluation_form.html", {"course": course})


# def save(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     new_eval = Evaluation.objects.create(
#         course=course,
#         grade=request.GET["grade"],
#         review=request.GET["review"],
#         password=request.GET["password"],
#     )
#     new_eval.save()
#     return redirect("/course-evaluation/" + str(course.id))

# def save(request, fiadetail_id):
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     new_eval = evaluation()
#     new_eval.subject = fia_detail.name
#     new_eval.star = request.GET["star"]
#     new_eval.text = request.GET["written"]
#     new_eval.password = request.GET["password"]
#     new_eval.save()
#     return redirect("/fia/" + str(fia_detail.id))

# def delete_request(request, fiadetail_id, fiaeval_id):
#     fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     return render(
#         request, "deletePassword.html", {"fia_detail": fia_detail, "fia_eval": fia_eval}
#     )

# def delete(request, fiadetail_id, fiaeval_id):
#     fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     if fia_eval.password != int(request.GET["enteredPassword"]):
#         return render(
#             request,
#             "deletePassword.html",
#             {"fia_detail": fia_detail, "fia_eval": fia_eval},
#         )
#     fia_eval.delete()
#     return redirect("/fia/" + str(fia_detail.id))

# def update_request(request, fiadetail_id, fiaeval_id):
#     fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     return render(
#         request, "updatePassword.html", {"fia_detail": fia_detail, "fia_eval": fia_eval}
#     )

# def update(request, fiadetail_id, fiaeval_id):
#     fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     if fia_eval.password != int(request.GET["enteredPassword"]):
#         return render(
#             request,
#             "updatePassword.html",
#             {"fia_detail": fia_detail, "fia_eval": fia_eval},
#         )
#     return render(
#         request, "update.html", {"fia_detail": fia_detail, "fia_eval": fia_eval}
#     )

# return render(request, "course.html", {"data": data})


# def updateFinal(request, fiadetail_id, fiaeval_id):
#     fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     fia_eval.star = request.GET["star"]
#     fia_eval.text = request.GET["written"]
#     fia_eval.password = request.GET["password"]
#     fia_eval.save()
#     return redirect("/fia/" + str(fia_detail.id))
