from django.shortcuts import render
from.models import Book,BuyBook,Comment
from.serializers import BookSerializer,BuySerializer,CommentSerializerr

from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.

class Create(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        book_name = request.data.get('book_name')
        image = request.data.get('image')
        price = request.data.get('price')

        data = {
            "author":request.user.id,
            "book_name":book_name,
            "image":image,
            "price":price
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"created"
                }
            )
        return Response(serializer.errors)
    
class BookList(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    
class BookDetails(APIView):

    permission_classes = [IsAuthenticated]


    def get(self,request,id):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
class Update(APIView):

    permission_classes = [IsAuthenticated]

    def put(self,request,id):

        book = Book.objects.get(id=id)
        if request.user == book.author:
            
            if 'book_name' in request.data:
                book.book_name=request.data.get('book_name')    
            if 'image' in request.data:
                book.title=request.data.get('image')   
            if 'title' in request.data:
                book.price=request.data.get('price')
            book.save()

            return Response(
                    {
                        "message":"Updated",    
                    }
                 )
        return Response(
             {
                "message":"You have no permission" 
             }
         )
    def delete(self,request,id):
        book = Book.objects.get(id=id)
        if request.user == book.author:
            book.delete()
            return Response(
                {
                'message':"Book deleted successfully"
                }
            )
        return Response(
            {
               'message':"You have no permission" 
            }
        )

class Search(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        search = request.data.get('search')
        if search:
            result = Book.objects.filter(book_name__icontains=search)
            if result.count()>0:
                serializer = BookSerializer(result,many=True)
                return Response(
                   serializer.data
                )
            return Response(
                {
                    "message":"No result found"
                }
            )
        
class Buy(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,id):
        quantity = request.data.get('quantity')
        book = Book.objects.get(id=id)
        data = {
            "user":request.user.id,
            "book":book.id,
            "quantity":quantity,
            "amount":int(book.price) * int(quantity)
        }
        if request.user != book.author:
            serializer = BuySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        
        return Response(
            {
                "message":"You are the author of this book"
            }
        )
    
class History(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        books = BuyBook.objects.filter(user=request.user)
        serializer = BuySerializer(books,many=True)
        return Response(serializer.data)
    
class Comments(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request,id):
        cmnt = request.data.get('comment')
        book = Book.objects.get(id=id)
        data = {
            "user":request.user.id,
            "book":book.id,
            "comment":cmnt
        }
        if request.user!=book.author:
            serializer = CommentSerializerr(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response(
            {
                "message":"Your the author of this book"
            }
        )



