from django.urls import path
from .views import (index,contact
                        ,about,courses,A404,team,
                    testimonial,addsdetailview,websdetailview,papularsdetailview,expertsdetailview,
                    expsdetailview,instructsdetailview,coursdetailview,aexpsdetailview,teamsdetailview,
                    CoursesUpdateView,CoursesDeleteView,courseDetail,CourseCreateView )



urlpatterns = [
    path('courses/', courses, name='courses'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('', index, name='index'),
    path('A404/',A404,name='A404'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('adds/<int:id>', addsdetailview, name='addsDetail'),
    path('webs/<int:id>', websdetailview, name='websDetail'),
    path('papulars/<int:id>', papularsdetailview, name='papularsDetail'),
    path('experts/<int:id>', expertsdetailview, name='expertsDetail'),
    path('exps/<int:id>', expsdetailview, name='expsDetail'),
    path('instructs/<int:id>', instructsdetailview, name='instructsDetail'),
    path('cours/<int:id>', coursdetailview, name='coursDetail'),
    path('aexps/<int:id>', aexpsdetailview, name='aexpsDetail'),
    path('teams/<int:id>', teamsdetailview, name='teamsDetail'),
    path('course/edit/<slug>/', CoursesUpdateView.as_view(),name="courseUpdate",),
    path('course/delete/<slug>/',CoursesDeleteView.as_view(), name = 'courseDelete'),
    path('course/<slug:course>',courseDetail, name='coursedetail'),
    path("course/create",CourseCreateView.as_view(),name="course_create")
    ]






































































































