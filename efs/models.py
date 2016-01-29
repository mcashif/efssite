from django.db import models
from django.utils import timezone

# Create your models here.
#********************************************/
# Sindhi Model Start
#*******************************************/        
class Sindhi_LearningOutcome(models.Model): 
    
    GON = 'Grade-1'
    GTW = 'Grade-2'
    GTH = 'Grade-3'
    GFO = 'Grade-4'
    GFI=  'Grade-5'
    
    SINDHI_GRADE = (
        (GON, 'Grade-1'),
        (GTW, 'Grade-2'),
        (GTH, 'Grade-3'),
        (GFO, 'Grade-4'),
        (GFI, 'Grade-5'),
    ) 
     
     
    LIS = 'Listening'
    SPK= 'Speaking'
    RDI = 'Reading'
    WRI = 'Writing'
    CWR=  'Creative Writing'
    LAC='Language Cognition'
    TLS='The Life Skills'
    SPC='Speech'
    
    SINDHI_SKILL = (
        (LIS, 'Listening'),
        (SPK, 'Speaking'),
        (RDI, 'Reading'),
        (WRI, 'Writing'),
        (CWR, 'Creative Writing'),
        (LAC,'Language Cognition'),
        (TLS,'The Life Skills'),
        (SPC,'Speech'),
    ) 
    
    outcome_text= models.TextField(max_length=500)
    
    skill = models.CharField(max_length=16,
                                     choices=SINDHI_SKILL,
                                      default=LIS)
    
    grade = models.CharField(max_length=16,
                                     choices=SINDHI_GRADE,
                                      default=GON)
    
    midterm_exploratory =    models.IntegerField(default=1)
    midterm_confirmatory = models.IntegerField(default=1)
    
    final_exploratory = models.IntegerField(default=2)
    final_confirmatory = models.IntegerField(default=2)
    
    
    outcome_verified= models.BooleanField(default=False)
    
    
    def __str__(self):              # __unicode__ on Python 2
        #return 'SIN{num:06d}'.format(num=self.id)
        return self.outcome_text
        
    class Meta:
        verbose_name = 'Sindhi Learning Outcome'
    
             
class Sindhi_Question(models.Model):
    
    CON = 'Confirmatory'
    EXP = 'Exploratory'
    QUESTION_TYPE = (
        (CON, 'Confirmatory'),
        (EXP, 'Exploratory'),
    )
    
    LONG = 'Long'
    MEDIUM = 'Medium'
    SHORT = 'Short'

    QUESTION_DIFFICULTY = (
        (LONG, 'Long'),
        (MEDIUM, 'Medium'),
        (SHORT, 'Short'),
    )
        
    question_text= models.TextField(max_length=500)
    
    
    type = models.CharField(max_length=16,
                                     choices=QUESTION_TYPE,
                                      default=CON)
    
    duration = models.CharField(max_length=16,
                                     choices=QUESTION_DIFFICULTY,
                                      default=MEDIUM)
    
    qimage=models.ImageField(upload_to='sindhi', blank=True)
    
    correct_answer= models.CharField(max_length=200, default='')
    
    learnig_outcome = models.ForeignKey(
        Sindhi_LearningOutcome,
        on_delete=models.CASCADE,
    )

    question_verified= models.BooleanField(default=False)
    
    date_time=models.DateTimeField(default=timezone.now)
       
    question_author= models.CharField(max_length=16,
                                      default='Admin')
     
    #objects = QuestionRandomManager()
    
    def __str__(self):
        #return 'QUL1{num:06d}'.format(num=self.id)
        return self.question_text
    

    class Meta:
        verbose_name = 'Sindhi Question'


#********************************************/
# Urdu Model Start
#*******************************************/
class Urdu_LearningOutcome(models.Model): 
    
    GON = 'Grade-1'
    GTW = 'Grade-2'
    GTH = 'Grade-3'
    GFO = 'Grade-4'
    GFI=  'Grade-5'
    
    SINDHI_GRADE = (
        (GON, 'Grade-1'),
        (GTW, 'Grade-2'),
        (GTH, 'Grade-3'),
        (GFO, 'Grade-4'),
        (GFI, 'Grade-5'),
    ) 
     
     
    LIS = 'Listening'
    SPK= 'Speaking'
    RDI = 'Reading'
    WRI = 'Writing'
    CWR=  'Creative Writing'
    LAC='Language Cognition'
    TLS='The Life Skills'
    SPC='Speech'
    
    SINDHI_SKILL = (
        (LIS, 'Listening'),
        (SPK, 'Speaking'),
        (RDI, 'Reading'),
        (WRI, 'Writing'),
        (CWR, 'Creative Writing'),
        (LAC,'Language Cognition'),
        (TLS,'The Life Skills'),
        (SPC,'Speech'),
    ) 
    
    outcome_text= models.TextField(max_length=500)
    
    skill = models.CharField(max_length=16,
                                     choices=SINDHI_SKILL,
                                      default=LIS)
    
    grade = models.CharField(max_length=16,
                                     choices=SINDHI_GRADE,
                                      default=GON)
    
    midterm_exploratory =    models.IntegerField(default=1)
    midterm_confirmatory = models.IntegerField(default=1)
    
    final_exploratory = models.IntegerField(default=2)
    final_confirmatory = models.IntegerField(default=2)
    
    
    outcome_verified= models.BooleanField(default=False)
    
    
    def __str__(self):              # __unicode__ on Python 2
        #return 'SIN{num:06d}'.format(num=self.id)
        return self.outcome_text
        
    class Meta:
        verbose_name = 'Urdu Learning Outcome'
    
             
class Urdu_Question(models.Model):
    
    CON = 'Confirmatory'
    EXP = 'Exploratory'
    QUESTION_TYPE = (
        (CON, 'Confirmatory'),
        (EXP, 'Exploratory'),
    )
    
    LONG = 'Long'
    MEDIUM = 'Medium'
    SHORT = 'Short'

    QUESTION_DIFFICULTY = (
        (LONG, 'Long'),
        (MEDIUM, 'Medium'),
        (SHORT, 'Short'),
    )
        
    question_text= models.TextField(max_length=500)
    
    
    type = models.CharField(max_length=16,
                                     choices=QUESTION_TYPE,
                                      default=CON)
    
    duration = models.CharField(max_length=16,
                                     choices=QUESTION_DIFFICULTY,
                                      default=MEDIUM)
    
    qimage=models.ImageField(upload_to='sindhi', blank=True)
    
    correct_answer= models.CharField(max_length=200, default='')
    
    learnig_outcome = models.ForeignKey(
        Urdu_LearningOutcome,
        on_delete=models.CASCADE,
    )

    question_verified= models.BooleanField(default=False)
    
    date_time=models.DateTimeField(default=timezone.now)
       
    question_author= models.CharField(max_length=16,
                                      default='Admin')
     
    #objects = QuestionRandomManager()
    
    def __str__(self):
        #return 'QUL1{num:06d}'.format(num=self.id)
        return self.question_text
    

    class Meta:
        verbose_name = 'Urdu Question'

#********************************************/
# Math Model Start
#*******************************************/
class Math_LearningOutcome(models.Model): 
    
    GON = 'Grade-1'
    GTW = 'Grade-2'
    GTH = 'Grade-3'
    GFO = 'Grade-4'
    GFI=  'Grade-5'
    
    SINDHI_GRADE = (
        (GON, 'Grade-1'),
        (GTW, 'Grade-2'),
        (GTH, 'Grade-3'),
        (GFO, 'Grade-4'),
        (GFI, 'Grade-5'),
    ) 
     
     
    MTH='Using and Applying Mathamatics'
    NBR='Counting and Number Relationship'
    NFA='Number Facts'
    CAL='Calculations'
    GEO='Geomatry'
    MEA='Measure'
    DAT='Data Handling'
  
    
    MATH_SKILL = (
        (MTH, 'Using and Applying Mathamatics'),
        (NBR, 'Counting and Number Relationship'),
        (NFA, 'Number Facts'),
        (CAL, 'Calculations'),
        (GEO, 'Geomatry'),
        (MEA, 'Measure'),
        (DAT, 'Data Handling'),
    ) 
    
    outcome_text= models.TextField(max_length=500)
    
    skill = models.CharField(max_length=16,
                                     choices=MATH_SKILL,
                                      default=MTH)
    
    grade = models.CharField(max_length=16,
                                     choices=SINDHI_GRADE,
                                      default=GON)
    
    midterm_exploratory =    models.IntegerField(default=1)
    midterm_confirmatory = models.IntegerField(default=1)
    
    final_exploratory = models.IntegerField(default=2)
    final_confirmatory = models.IntegerField(default=2)
    
    
    outcome_verified= models.BooleanField(default=False)
    
    
    def __str__(self):              # __unicode__ on Python 2
        #return 'SIN{num:06d}'.format(num=self.id)
        return self.outcome_text
        
    class Meta:
        verbose_name = 'Math Learning Outcome'
    
             
class Math_Question(models.Model):
    
    CON = 'Confirmatory'
    EXP = 'Exploratory'
    QUESTION_TYPE = (
        (CON, 'Confirmatory'),
        (EXP, 'Exploratory'),
    )
    
    LONG = 'Long'
    MEDIUM = 'Medium'
    SHORT = 'Short'

    QUESTION_DIFFICULTY = (
        (LONG, 'Long'),
        (MEDIUM, 'Medium'),
        (SHORT, 'Short'),
    )
        
    question_text= models.TextField(max_length=500)
    
    
    type = models.CharField(max_length=16,
                                     choices=QUESTION_TYPE,
                                      default=CON)
    
    duration = models.CharField(max_length=16,
                                     choices=QUESTION_DIFFICULTY,
                                      default=MEDIUM)
    
    qimage=models.ImageField(upload_to='math', blank=True)
    
    correct_answer= models.CharField(max_length=200, default='')
    
    learnig_outcome = models.ForeignKey(
        Math_LearningOutcome,
        on_delete=models.CASCADE,
    )

    question_verified= models.BooleanField(default=False)
    
    date_time=models.DateTimeField(default=timezone.now)
       
    question_author= models.CharField(max_length=16,
                                      default='Admin')
     
    #objects = QuestionRandomManager()
    
    def __str__(self):
        #return 'QUL1{num:06d}'.format(num=self.id)
        return self.question_text
    

    class Meta:
        verbose_name = 'Math Question'

#********************************************/
# English Model Start
#*******************************************/
class English_LearningOutcome(models.Model): 
    
    GON = 'Grade-1'
    GTW = 'Grade-2'
    GTH = 'Grade-3'
    GFO = 'Grade-4'
    GFI=  'Grade-5'
    
    SINDHI_GRADE = (
        (GON, 'Grade-1'),
        (GTW, 'Grade-2'),
        (GTH, 'Grade-3'),
        (GFO, 'Grade-4'),
        (GFI, 'Grade-5'),
    ) 
     
     
    LIS = 'Listening'
    SPK= 'Speaking'
    RDI = 'Reading'
    WRI = 'Writing'
    WRITR='Writing Transcription'
    WRICMP='Writing Composition'
    WRICPR='Writing Comprehension'
    WRIGRM='Writing Grammer'
    CWR=  'Creative Writing'
    LAC='Language Cognition'
    TLS='The Life Skills'
  
    
    ENGLISH_SKILL = (
        (LIS, 'Listening and Understanding'),
        (SPK, 'Speaking'),
        (RDI, 'Reading and Thinking'),
        (WRITR, 'Writing Transcription'),
        (WRICMP, 'Writing Composition'),
        (WRICPR, 'Writing Comprehension'),
        (WRIGRM, 'Writing Grammer'),
        (CWR, 'Creative Writing'),
        (LAC,'Language Cognition'),
        (TLS,'The Life Skills'),
    )  
    
    outcome_text= models.TextField(max_length=500)
    
    skill = models.CharField(max_length=16,
                                     choices=ENGLISH_SKILL,
                                      default=LIS)
    
    grade = models.CharField(max_length=16,
                                     choices=SINDHI_GRADE,
                                      default=GON)
    
    midterm_exploratory =    models.IntegerField(default=1)
    midterm_confirmatory = models.IntegerField(default=1)
    
    final_exploratory = models.IntegerField(default=2)
    final_confirmatory = models.IntegerField(default=2)
    
    
    outcome_verified= models.BooleanField(default=False)
    
    
    def __str__(self):              # __unicode__ on Python 2
        #return 'SIN{num:06d}'.format(num=self.id)
        return self.grade+"|"+self.skill+"|"+self.outcome_text
        
    class Meta:
        verbose_name = 'English Learning Outcome'
    
             
class English_Question(models.Model):
    
    CON = 'Confirmatory'
    EXP = 'Exploratory'
    QUESTION_TYPE = (
        (CON, 'Confirmatory'),
        (EXP, 'Exploratory'),
    )
    
    LONG = 'Long'
    MEDIUM = 'Medium'
    SHORT = 'Short'

    QUESTION_DIFFICULTY = (
        (LONG, 'Long'),
        (MEDIUM, 'Medium'),
        (SHORT, 'Short'),
    )
        
    question_text= models.TextField(max_length=500)
    
    
    type = models.CharField(max_length=16,
                                     choices=QUESTION_TYPE,
                                      default=CON)
    
    duration = models.CharField(max_length=16,
                                     choices=QUESTION_DIFFICULTY,
                                      default=MEDIUM)
    
    qimage=models.ImageField(upload_to='english', blank=True)
    
    correct_answer= models.CharField(max_length=200, default='')
    
    learnig_outcome = models.ForeignKey(
        English_LearningOutcome,
        on_delete=models.CASCADE,
    )

    question_verified= models.BooleanField(default=False)
    
    date_time=models.DateTimeField(default=timezone.now)
       
    question_author= models.CharField(max_length=16,
                                      default='Admin')
     
    #objects = QuestionRandomManager()
    
    def __str__(self):
        #return 'QUL1{num:06d}'.format(num=self.id)
        return self.question_text
    

    class Meta:
        verbose_name = 'English Question'