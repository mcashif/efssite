from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from efs.models import Sindhi_LearningOutcome,Sindhi_Question
from efs.models import Urdu_LearningOutcome,Urdu_Question
from efs.models import English_LearningOutcome,English_Question
from efs.models import Math_LearningOutcome,Math_Question
from django.template import loader
from django.views.generic import ListView
import random

#/*******************
#Global
#/*******************
gQuestionList= [] 
gSubjectName = ''
gGrade = ''
gTotalTime = ''
#/*******************
#Helper Functions
#/*******************

def selectNumberQuestion(ptype,val,final,mid):
    
    if(ptype=='0'):
        return val
    
    if(ptype=='1'):
        return final
         
    if(ptype=='2'):
        return mid
     
    return '0'
         
def selectGrade(grader):
    
    gradeSelect='Error'
    
    if(grader=='1'):
        gradeSelect='Grade-1'
        
    if(grader=='2'):
        gradeSelect='Grade-2'
        
    if(grader=='3'):
        gradeSelect='Grade-3'
        
    if(grader=='4'):
        gradeSelect='Grade-4'
        
    if(grader=='5'):
        gradeSelect='Grade-5'
        
    return gradeSelect

def selectOucome(subject,gradeSelect):
    
    latest_outcome_list=[]

    if(subject=='1'):
        latest_outcome_list = Sindhi_LearningOutcome.objects.filter(grade=gradeSelect, outcome_verified=True)
        
    if(subject=='2'):
        latest_outcome_list = Urdu_LearningOutcome.objects.filter(grade=gradeSelect, outcome_verified=True)
        
    if(subject=='3'):
        latest_outcome_list = Math_LearningOutcome.objects.filter(grade=gradeSelect, outcome_verified=True)
        
    if(subject=='4'):
        latest_outcome_list = English_LearningOutcome.objects.filter(grade=gradeSelect, outcome_verified=True)
        
    return latest_outcome_list

def selectQuestion(subject, oucomeid, qtype):
    
    latest_question_list=[]

    if(subject=='1'):
        latest_question_list = Sindhi_Question.objects.filter(learnig_outcome=oucomeid, type=qtype, question_verified=True) 
        
    if(subject=='2'):
        latest_question_list = Urdu_Question.objects.filter(learnig_outcome=oucomeid, type=qtype, question_verified=True) 
        
    if(subject=='3'):
        latest_question_list = Math_Question.objects.filter(learnig_outcome=oucomeid, type=qtype, question_verified=True) 
        
    if(subject=='4'):
        latest_question_list = English_Question.objects.filter(learnig_outcome=oucomeid, type=qtype, question_verified=True) 
        
    return latest_question_list

def selectSubjectName(subject):
    
    sujectName="Error"
    
    if(subject=='1'):
        sujectName="Sindhi"
        
    if(subject=='2'):
         sujectName="Urdu"
        
    if(subject=='3'):
         sujectName="Math"
        
    if(subject=='4'):
         sujectName="English"
        
    return sujectName

#/*******************
#System Functions
#/*******************
def logout(request):
    return HttpResponseRedirect('/logout')

def login(request):
    return HttpResponseRedirect('/login')

@login_required(login_url='/login/')
def index(request):
    template = loader.get_template('efs/index.html')
    return HttpResponse(template.render(request))
  
@login_required(login_url='/login/')
def logged_in(request):
    
    if request.user.is_superuser==True:
         return HttpResponseRedirect('/admin') 
    else:  
        if request.user.groups.all()[0].name[0].upper() == 'G':
            return HttpResponseRedirect('/efs/index')       
        else:
            return HttpResponseRedirect('/admin')                               
#/*******************
#Sindhi Section
#/*******************

@login_required(login_url='/login/')
def sindhi(request):
    isGM=False
    if request.user.groups.all()[0].name[0].upper() == 'G' and request.user.groups.all()[0].name[1].upper() == 'M':
        isGM=True
        
    template = loader.get_template('efs/sindhi.html')
    
    context = {
        'isGM': isGM,            
    }
    
    return HttpResponse(template.render(context,request))

#/*******************
#Urdu Section
#/*******************
@login_required(login_url='/login/')
def urdu(request):
    isGM=False
    if request.user.groups.all()[0].name[0].upper() == 'G' and request.user.groups.all()[0].name[1].upper() == 'M':
        isGM=True
        
    template = loader.get_template('efs/urdu.html')
    
    context = {
        'isGM': isGM,            
    }
    
    return HttpResponse(template.render(context,request))

#/*******************
#Math Section
#/*******************
@login_required(login_url='/login/')
def math(request):
    isGM=False
    if request.user.groups.all()[0].name[0].upper() == 'G' and request.user.groups.all()[0].name[1].upper() == 'M':
        isGM=True
        
    template = loader.get_template('efs/math.html')
    
    context = {
        'isGM': isGM,            
    }
    
    return HttpResponse(template.render(context,request))

#/*******************
#English Section
#/*******************
@login_required(login_url='/login/')
def english(request):
    
    isGM=False
    if request.user.groups.all()[0].name[0].upper() == 'G' and request.user.groups.all()[0].name[1].upper() == 'M':
        isGM=True
        
    template = loader.get_template('efs/english.html')
    
    context = {
        'isGM': isGM,            
    }
    
    return HttpResponse(template.render(context,request))

#/*******************
#English Section
#/*******************
@login_required(login_url='/login/')  
def outcomelist(request,subject,grader):
    errorText='0'

    latest_outcome_list=selectOucome(subject,selectGrade(grader))
    

    
    if(len(latest_outcome_list)==0):
        errorText="Error Reported" 
        template = loader.get_template('efs/error.html')
        context = {
            'errorText': errorText,            
        }       
        return HttpResponse(template.render(context, request))
        
    else:  
        template = loader.get_template('efs/outcomelist.html')
        context = {
            'latest_outcome_list': latest_outcome_list,
            'subject': subject,
            'grader': grader,
        }
        return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def generatepaper(request,subject,grader,ptype):
    
    latest_outcome_list=selectOucome(subject,selectGrade(grader))
    
    gQuestionList[:] = []
    totalTime=0   
      
    for outcome in latest_outcome_list:
        numberofQuestionsE= selectNumberQuestion(ptype,request.POST.get("e"+str(outcome.id)),outcome.final_exploratory,outcome.midterm_exploratory)
        question_listE=selectQuestion(subject,outcome.id,'Exploratory')      
        totalquestionE=question_listE.count()
        if(int(numberofQuestionsE)>0):
            if(totalquestionE>=int(numberofQuestionsE)):
                randomListE = random.Random().sample(range(0,totalquestionE),int(numberofQuestionsE))
                for randomindexE in randomListE:
                    if (question_listE[randomindexE].question_verified):
                        gQuestionList.append(question_listE[randomindexE])
                        
                        if (question_listE[randomindexE].duration=='Long'):
                            totalTime=totalTime+1
                            
                        if (question_listE[randomindexE].duration=='Medium'):
                            totalTime=totalTime+1.5
                            
                        if (question_listE[randomindexE].duration=='Short'):
                            totalTime=totalTime+2
                

    for outcome in latest_outcome_list:
            numberofQuestionsC= selectNumberQuestion(ptype,request.POST.get("c"+str(outcome.id)),outcome.final_confirmatory,outcome.midterm_confirmatory)
            question_listC=selectQuestion(subject,outcome.id,'Confirmatory')     
            totalquestionC=question_listC.count()
            if(int(numberofQuestionsC)>0):
                if(totalquestionC>=int(numberofQuestionsC)):
                    randomListC = random.Random().sample(range(0,totalquestionC),int(numberofQuestionsC))
                    for randomindexC in randomListC:
                        if (question_listC[randomindexC].question_verified):
                            gQuestionList.append(question_listC[randomindexC])
                            
                            if (question_listC[randomindexC].duration=='Long'):
                                totalTime=totalTime+1
                                
                            if (question_listC[randomindexC].duration=='Medium'):
                                totalTime=totalTime+1.5
                                
                            if (question_listC[randomindexC].duration=='Short'):
                                totalTime=totalTime+2
                        
    
    random.shuffle(gQuestionList) 
    
    
    gSubjectName = selectSubjectName(subject)
    gGrade = selectGrade(grader)
    gTotalTime = totalTime
     
    
    if(len(gQuestionList)==0):
        errorText='No Questions to Show......'
        
        template = loader.get_template('efs/error.html')
        context = {
            'errorText': errorText,            
        }
            
        return HttpResponse(template.render(context, request))
        
    else:    
        
        template = loader.get_template('efs/generatedpaper.html')
        context = {
            'gTotalTime': gTotalTime,
            'gQuestionList': gQuestionList,
            'gSubjectName': gSubjectName,
            'gGrade': gGrade,          
        }
            
        return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def generateanswers(request):
    
    template = loader.get_template('efs/generatedanswer.html')
    context = {
            'gTotalTime': gTotalTime,
            'gQuestionList': gQuestionList,
            'gSubjectName': gSubjectName, 
            'gGrade': gGrade,
    }
    
    return HttpResponse(template.render(context, request))