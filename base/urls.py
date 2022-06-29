from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,UserLoginView,UserLogoutView,SignUpView

urlpatterns = [
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),

    path('signup/',SignUpView.as_view(),name='signup'),

    path('',TaskList.as_view(),name='tasklist'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='taskdetail'),
    path('task-create/',TaskCreate.as_view(),name='taskcreate'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='taskupdate'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='taskdelete'),

]