from rest_framework import serializers 
from .models import TimingTodo, Todo
import re 
from django.template.defaultfilters import slugify


class TodoSeriazlier(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    
    class Meta:
        model = Todo
        fields = ['todo_title', 'slug', 'todo_description', 'is_done', 'uid']
      # exclude = ['created_at']
      
      
    def get_slug(self, obj):
        
        return slugify(obj.todo_title)
      
      
        def validate(self, validated_data):
             if data:
                 todo_title = data
                 regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
                 
                 if len(todo_title) < 3:
                     raise serializers.ValidationError('todo title must be more than 3 character')
                 
                 
                 
                 if not regex.search(todo_title) == None:
                  raise serializers.ValidationError('todo_title cannot contain special character')
        
        
             return data   
           
class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSeriazlier()
    class Meta:
        model = TimingTodo
        exclude = ['created_at', 'updated_at']
#        depth = 1
                    