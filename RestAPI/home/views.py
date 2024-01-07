from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TimingTodoSerializer, TodoSeriazlier
from .views import*
from .models import TimingTodo, Todo
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.decorators import action




# Create your views here.

# Fuction Base View

@api_view(['GET', 'POST', 'PATCH'])
def get_home(request):
    if request.method == 'GET':
       return Response({
           'status':200,
           'message': 'Yes!  Django rest Framework is working!!',
           'method_called': 'You called GET method'  
       })
       
    elif request.method == 'POST':
        return Response({
           'status':200,
           'message': 'Yes!  Django rest Framework is working!!',
           'method_called': 'You called POST method'  
        
       })
        
    elif request.method == 'PATCH':
        return Response({
           'status':200,
           'message': 'Yes!  Django rest Framework is working!!',
           'method_called': 'You called PATCH method'  
        
       })
    elif request.method == 'PATCH':
        return Response({
           'status':400,
           'message': 'Yes!  Django rest Framework is working!!',
           'method_called': 'You called invalid method'  
        
       })
 
@api_view(['GET'])        
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSeriazlier(todo_objs, many = True)
    
    
    return Response({
        'status': True,
        'message' : 'Todo fetched',
        'data': serializer.data
    })
 
 
 
@api_view(['POST'])        
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSeriazlier(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
              'status': True,
              'message': 'success data',
              'data': serializer.data
                
            }) 
            
            
        return Response({
            'status': False,
            'message': 'invalid data',
            'data': serializer.errors
            
            })    
            
             
    except Exception as e:
        print(e)            
    return Response({
        'status': False,
        'massage': 'Something went wrong'
        })
    
    
@api_view(['PATCH'])        
def patch_todo(request): 
    
    try:   
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'massage': 'uid is required',
                'data': {}
            })
        obj = Todo.objects.get(uid = data.get('uid'))
        serializer = TodoSeriazlier(obj, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'success data',
                'data': serializer.data
                    
            }) 
             
        return Response({
            'status': False,
            'message': 'invalid data',
            'data': serializer.errors
            
        }) 
        
    except Exception as e:
        print(e)
             
    return Response({
        'status': False,
        'message': 'invalid uid',
        'data': {}
            
        })               
            
            
           
        
   # TodoSeriazlier
           
           
           
           
           
           
            
# class Base VIews   
class TodoView(APIView):
    
    def get(self, request):
        todo_objs = Todo.objects.all()
        serializer = TodoSeriazlier(todo_objs, many = True)
    
    
        return Response({
            'status': True,
            'message' : 'Todo fetched',
            'data': serializer.data
        })
    
    def post(self, request):
        try:
            data = request.data
            serializer = TodoSeriazlier(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                'status': True,
                'message': 'success data',
                'data': serializer.data
                
            }) 
                
            return Response({
            'status': False,
            'message': 'invalid data',
            'data': serializer.errors
            
            }) 
            
        except Exception as e:
             print(e)            
        return Response({
            'status': False,
            'massage': 'Something went wrong'
            })         
            
            
              
    
# Model Base Views

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSeriazlier
    
    
    @action(detail=False, methods=['GET'])
    def get_timig_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many = True)
        return Response({
            'status': True,
            'messgae': 'Timing todo fetched',
            'data': serializer.data
        })
        
        
    
    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request, pk):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'success data',
                    'data': serializer.data
                        
                })            
                
            return Response({
                'status': False,
                'message': 'invalid data',
                'data': serializer.errors
            
                }) 
                
        except Exception as e:
             print(e)            
        return Response({
            'status': False,
            'massage': 'Something went wrong'
            })         
                

