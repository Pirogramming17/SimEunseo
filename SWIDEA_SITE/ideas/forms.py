from sre_parse import Verbose
from django import forms
from .models import Idea, Tool
        
class IdeaForm(forms.ModelForm):
    #tool = forms.ModelChoiceField(queryset=Tool.objects.all())
    def __init__(self, *args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['image'].required = True
        self.fields['description'].required = True
        self.fields['interest'].required = True
        self.fields['tool_choice'].required = True
        
        new_choices = []
        tool = Tool.objects.all()
        for t in tool:
            temp = []
            temp.append(t.name)
            temp.append(t.name)
            temp = tuple(temp)
            new_choices.append(temp)
        new_choices = tuple(new_choices)
        
        self.fields['tool_choice'] = forms.ChoiceField(choices=new_choices, label="예상 개발 툴")
    class Meta:
        model = Idea
        fields = ('name','image','description','interest','tool_choice')
    
class ToolForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ToolForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['type'].required = True
        self.fields['description'].required = True
        
    class Meta:
        model = Tool
        fields = ['name', 'type', 'description']