from django.shortcuts import render
from .models import Question
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# Create your views here.


class QuestionList(ListView):
    model = Question
    
    template_name = 'question_list.html'
    
    
class QuestionCreate(CreateView):
    model = Question
    
    fields = ['author', 'question', 'created_at', 'content', 'tags']
    
    template_name = 'forum/question_add.html'
    
    success_url = '/questions'
    
    
    
class QuestionDatail(DetailView):
    model = Question
    
    template_name = 'forum/question_details.html'
    
class QuestionUpdate(UpdateView):
    model = Question
    
    fields =  ['author', 'question', 'created_at', 'content', 'tags']
    
    template_name = 'forum/question_edit.html'
    
    success_url = '/questions'
    
    
    
class QuestionDelete(DeleteView):
    model = Question
    
    # template_name = 'forum/question_confirm_delete.html'
    
    success_url = '/questions'