from django.shortcuts import render
from .models import Question, Answer
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
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        q = self.object
        context['answers'] = Answer.objects.filter(
            question=q
        )

        return context

    
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