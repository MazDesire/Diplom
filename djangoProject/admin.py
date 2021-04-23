
from django.contrib import admin
from djangoProject.models import Client
from djangoProject.models import Person
from djangoProject.models import ClientCategory
from djangoProject.models import IndPers
from djangoProject.models import Result
from djangoProject.models import IndPlan
from djangoProject.models import Programm
from djangoProject.models import ResTopic
from djangoProject.models import Topic
from djangoProject.models import Level
from djangoProject.models import Course
from djangoProject.models import Test
from djangoProject.models import AnswerTest
from djangoProject.models import VarAnsTest
from djangoProject.models import QuestionTest
from djangoProject.models import Form
from djangoProject.models import VarAnsForm
from djangoProject.models import AnswerForm
from djangoProject.models import Position
from djangoProject.models import PositionCategory

# Register your models here.

admin.site.register(Client)
admin.site.register(Person)
admin.site.register(ClientCategory)
admin.site.register(IndPers)
admin.site.register(Result)
admin.site.register(IndPlan)
admin.site.register(Programm)
admin.site.register(ResTopic)
admin.site.register(Topic)
admin.site.register(Level)
admin.site.register(Course)
admin.site.register(Test)
admin.site.register(AnswerTest)
admin.site.register(VarAnsTest)
admin.site.register(QuestionTest)
admin.site.register(Form)
admin.site.register(VarAnsForm)
admin.site.register(AnswerForm)
admin.site.register(Position)
admin.site.register(PositionCategory)
