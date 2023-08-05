from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import AnswerForm

from django.utils import timezone


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


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        q = self.object
        context['answers'] = Answer.objects.filter(question=q)
        context['answer_form'] = AnswerForm
        return context

    def post(self, request, *args, **kwargs):
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            # Process the form data
            my_form =answer_form.save(commit=False)
            my_form.author = request.user
            my_form.created_at = timezone.now()
            
            # For example, you can save the form data to the database
            my_form.save()
            # Redirect to a success page or do any additional processing
            return redirect('/questions')

        context = self.get_context_data()
        context['answer_form'] = answer_form
        return self.render_to_response(context)


    
    
class QuestionUpdate(UpdateView):
    model = Question
    
    fields =  ['author', 'question', 'created_at', 'content', 'tags']
    
    template_name = 'forum/question_edit.html'
    
    success_url = '/questions'
    
    
    
class QuestionDelete(DeleteView):
    model = Question
    
    # template_name = 'forum/question_confirm_delete.html'
    
    success_url = '/questions'