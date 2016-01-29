from django import template
from efs.models import Sindhi_Question,Urdu_Question,Math_Question,English_Question

register = template.Library()

def selectQuestionCount(subject, oucomeid, qtype):
    
    latest_question_list=[]

    if(subject=='1'):
        latest_question_list = Sindhi_Question.objects.filter(learnig_outcome=oucomeid, type=qtype, question_verified=True) 
        
    if(subject=='2'):
        latest_question_list = Urdu_Question.objects.filter(learnig_outcome=oucomeid, type=qtype, question_verified=True) 
        
    if(subject=='3'):
        latest_question_list = Math_Question.objects.filter(learnig_outcome=oucomeid, type=qtype, question_verified=True) 
        
    if(subject=='4'):
        latest_question_list = English_Question.objects.filter(learnig_outcome=oucomeid, type=qtype, question_verified=True) 
        
    return latest_question_list.count()

@register.filter(name='total_questionEx')
def total_questionEx(learningOucome, subject):
    return selectQuestionCount(subject,learningOucome.id,'Exploratory')

@register.filter(name='total_questionCon')
def total_questionCon(learningOucome,subject):
    return selectQuestionCount(subject,learningOucome.id,'Confirmatory')