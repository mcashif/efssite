from import_export.admin import ImportExportModelAdmin
from efs.models import Sindhi_LearningOutcome,Sindhi_Question
from efs.models import Urdu_LearningOutcome,Urdu_Question
from efs.models import English_LearningOutcome,English_Question
from efs.models import Math_LearningOutcome,Math_Question
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

#**************************************************************/
# Common Functions
#**************************************************************/
def verify_selected_questions(modeladmin, request, queryset):
     
        queryset.update(question_verified=True)
        verify_selected_questions.short_description = 'Mark as Varified'
        
def unverify_selected_questions(modeladmin, request, queryset):
     
        queryset.update(question_verified=False)
        unverify_selected_questions.short_description = 'Mark as Un-Varified'
        
def verify_selected_outcome(modeladmin, request, queryset):
     
        queryset.update(outcome_verified=True)
        verify_selected_outcome.short_description = 'Mark as Varified'
        
     
def unverify_selected_outcome(modeladmin, request, queryset):   


        queryset.update(outcome_verified=False)
        unverify_selected_outcome.short_description = 'Mark as Un-Varified'
        

        

#**************************************************************/
# User Admin Functions
#**************************************************************/ 
class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin,self).__init__(*args, **kwargs)
        UserAdmin.list_display = ['username','email','first_name','last_name','is_active' ,'efs_user']

    # Function to count objects of each user from another Model (where user is FK)
    def efs_user(self, obj):
        
        if(obj.is_staff==True):
            return 'EFS User'
        else:
            return 'Non EFS User'



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)        
#**************************************************************/
# Sindhi Admin Functions
#**************************************************************/    
class SindhiQuestionAdmin(ImportExportModelAdmin):
    fields = ['learnig_outcome','question_text','type','duration','qimage','correct_answer'] 
    list_display = ('question_text', 'type','getGrade','question_verified')
    list_filter = ('question_verified', 'type','duration','learnig_outcome__skill', 'learnig_outcome__grade')
    search_fields = ['question_text']
    
    actions = [verify_selected_questions, unverify_selected_questions]
    
    def getGrade(self, obj):
        return obj.learnig_outcome.grade
      
    pass

class SindhiQuestionInline(admin.StackedInline):
    model = Sindhi_Question
    fields = ['learnig_outcome','question_text','type','duration','qimage','correct_answer'] 
    extra = 3
   
class SindhiOutComeAdmin(ImportExportModelAdmin):
    list_display = ('outcome_text', 'skill', 'grade','outcome_verified')
    list_filter = ('skill', 'grade')
    fieldsets = [
        (None,               {'fields': ['outcome_text']}),  
        ('Skill information', {'fields': ['skill']}),    
        ('Grade information', {'fields': ['grade']}),
        ('Midterm Exloratory weight', {'fields': ['midterm_exploratory']}),
        ('Midterm Confirmatory weight', {'fields': ['midterm_confirmatory']}),
        ('Final Exloratory weight', {'fields': ['final_exploratory']}),
        ('Final Confirmatory weight', {'fields': ['final_confirmatory']}),
    ]
    
    actions = [verify_selected_outcome, unverify_selected_outcome]
    
    inlines = [SindhiQuestionInline]

admin.site.register(Sindhi_Question,SindhiQuestionAdmin)
admin.site.register(Sindhi_LearningOutcome, SindhiOutComeAdmin) 
#**************************************************************/
# Urdu Admin Functions
#**************************************************************/
class UrduQuestionAdmin(ImportExportModelAdmin):
    fields = ['learnig_outcome','question_text','type','duration','qimage','correct_answer'] 
    list_display = ('question_text', 'type','getGrade','question_verified')
    list_filter = ('question_verified', 'type','duration','learnig_outcome__skill', 'learnig_outcome__grade')
    search_fields = ['question_text']
    
    actions = [verify_selected_questions, unverify_selected_questions]
    
    def getGrade(self, obj):
        return obj.learnig_outcome.grade
      
    pass

class UrduQuestionInline(admin.StackedInline):
    model = Urdu_Question
    fields = ['learnig_outcome','question_text','type','duration','qimage','correct_answer'] 
    extra = 3
   
class UrduOutComeAdmin(ImportExportModelAdmin):
    list_display = ('outcome_text', 'skill', 'grade','outcome_verified')
    list_filter = ('skill', 'grade')
    fieldsets = [
        (None,               {'fields': ['outcome_text']}),  
        ('Skill information', {'fields': ['skill']}),    
        ('Grade information', {'fields': ['grade']}),
        ('Midterm Exloratory weight', {'fields': ['midterm_exploratory']}),
        ('Midterm Confirmatory weight', {'fields': ['midterm_confirmatory']}),
        ('Final Exloratory weight', {'fields': ['final_exploratory']}),
        ('Final Confirmatory weight', {'fields': ['final_confirmatory']}),
    ]
    
    actions = [verify_selected_outcome, unverify_selected_outcome]
    
    inlines = [UrduQuestionInline]  
    
admin.site.register(Urdu_Question,UrduQuestionAdmin)
admin.site.register(Urdu_LearningOutcome, UrduOutComeAdmin) 
#**************************************************************/
# English Admin Functions
#**************************************************************/ 
class EnglishQuestionAdmin(ImportExportModelAdmin):
    fields = ['learnig_outcome','question_text','type','duration','qimage','correct_answer'] 
    list_display = ('question_text', 'type','getGrade','question_verified')
    list_filter = ('question_verified', 'type','duration','learnig_outcome__skill', 'learnig_outcome__grade')
    search_fields = ['question_text']
    
    actions = [verify_selected_questions, unverify_selected_questions]
    
    def getGrade(self, obj):
        return obj.learnig_outcome.grade
      
    pass

class EnglishQuestionInline(admin.StackedInline):
    model = English_Question
    fields = ['learnig_outcome','question_text','type','duration','qimage','correct_answer'] 
    extra = 3
   
class EnglishOutComeAdmin(ImportExportModelAdmin):
    list_display = ('outcome_text', 'skill', 'grade','outcome_verified')
    list_filter = ('skill', 'grade')
    fieldsets = [
        (None,               {'fields': ['outcome_text']}),  
        ('Skill information', {'fields': ['skill']}),    
        ('Grade information', {'fields': ['grade']}),
        ('Midterm Exloratory weight', {'fields': ['midterm_exploratory']}),
        ('Midterm Confirmatory weight', {'fields': ['midterm_confirmatory']}),
        ('Final Exloratory weight', {'fields': ['final_exploratory']}),
        ('Final Confirmatory weight', {'fields': ['final_confirmatory']}), 
    ]
    
    actions = [verify_selected_outcome, unverify_selected_outcome]
    
    inlines = [EnglishQuestionInline]
    
admin.site.register(English_Question,EnglishQuestionAdmin)
admin.site.register(English_LearningOutcome, EnglishOutComeAdmin) 
#**************************************************************/
# Math Admin Functions
#**************************************************************/ 
class MathQuestionAdmin(ImportExportModelAdmin):
    fields = ['learnig_outcome','question_text','type','duration','qimage','correct_answer'] 
    list_display = ('question_text', 'type','getGrade','question_verified')
    list_filter = ('question_verified', 'type','duration','learnig_outcome__skill', 'learnig_outcome__grade')
    search_fields = ['question_text']
    
    actions = [verify_selected_questions, unverify_selected_questions]
    
    def getGrade(self, obj):
        return obj.learnig_outcome.grade
      
    pass

class MathQuestionInline(admin.StackedInline):
    model = Math_Question
    fields = ['learnig_outcome','question_text','type','duration','qimage','correct_answer'] 
    extra = 3
   
class MathOutComeAdmin(ImportExportModelAdmin):
    list_display = ('outcome_text', 'skill', 'grade','outcome_verified')
    list_filter = ('skill', 'grade')
    fieldsets = [
        (None,               {'fields': ['outcome_text']}),  
        ('Skill information', {'fields': ['skill']}),    
        ('Grade information', {'fields': ['grade']}),
        ('Midterm Exloratory weight', {'fields': ['midterm_exploratory']}),
        ('Midterm Confirmatory weight', {'fields': ['midterm_confirmatory']}),
        ('Final Exloratory weight', {'fields': ['final_exploratory']}),
        ('Final Confirmatory weight', {'fields': ['final_confirmatory']}),
    ]
    
    actions = [verify_selected_outcome, unverify_selected_outcome]
    
    inlines = [MathQuestionInline]
    

admin.site.register(Math_Question,MathQuestionAdmin)
admin.site.register(Math_LearningOutcome, MathOutComeAdmin)