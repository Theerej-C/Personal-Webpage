
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer,CommentSerializer,CategorySerializer,TagSerializer
from .models import BlogModel,Comment,Tag,Category
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
class BlogPostCRUDAPI(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        # Retrieve all blog for specific user
        user_id = request.user.id
        blog_posts = BlogModel.objects.filter(author_id=user_id)
        serializer = BlogSerializer(blog_posts, many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        # content = data['content']
        data['author_id'] = request.user.id
        data['author'] = request.user.username
        serializer = BlogSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def update(self,request):
        try:
            data = request.data
            id = data['blog_id']
            blog_post = BlogModel.objects.get(id=id)
            if blog_post:
                serializer = BlogSerializer(blog_post, data=data)
                if(serializer.is_valid()):
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            else:
                return Response({"error": "Blog post not found"})
        except Exception as e:
            return Response({"error":str(e)})
    def delete(self,request):
        id = request.data['id']
        blog_post = BlogModel.objects.get(id=id)
        if (blog_post):
            blog_post.delete()
            return Response({"message": "Blog post deleted successfully"})
        else:
            return Response({"message": "Blog post not found"})

class BlogPostGlobalRetrival(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        data = BlogModel.objects.all()
        serializer = BlogSerializer(data,many=True)
        return Response(serializer.data)

class BlogPostComments(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        blog_id = request.query_params.get('blog_id')
        if blog_id:
            blog = BlogModel.objects.get(id=blog_id)
            comments = blog.comments.all()
            serailizer = CommentSerializer(comments,many=True)
            return Response(serailizer.data)
        else:
            return Response({"message": "Blog post id is required"})
    def post(self, request):
        data = request.data
        comment_content = data['content']
        comment = Comment(content=comment_content, author_id=request.user.id)
        comment.save()
        blog_id = data['blog_id']
        blog = BlogModel.objects.get(id=blog_id)
        blog.comments.add(comment)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    def put(self,request):
        comment_id = request.data['id']
        comment = Comment.objects.get(id=comment_id)
        data = request.data['content']
        comment['content'] = data
        serializer = CommentSerializer(comment,data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request):
        comment_id = request.data['id']
        comment = Comment.objects.get(id=comment_id)
        if comment:
            comment.delete()
            return Response({"message": "Comment deleted successfully"})
        else:
            return Response({"message": "Comment not found"})
        

class TagsCrudOperations(APIView):
    def get(self,request):
        try:
            blog_id = request.query_param.get('blog_id')
            blog = BlogModel.objects.get(id=blog_id)
            tags = blog.tags.all()
            serializer = TagSerializer(tags,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": "Blog post id is required"})
    def post(self,request):
        try:
            data = request.data
            tag_name = data['name']
            tag = Tag(name=tag_name)
            blog_id = data['blog_id']
            tag.save()
            blog = BlogModel.objects.get(id=blog_id)
            tag = Tag(name=tag_name)
            blog.tags.add(tag)
            serializer = TagSerializer(tag)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": "Blog post id and tag name are required"})
class CategoriesCrudOperation(APIView):
    def get(self,request):
        try:
            blog_id = request.query_param.get('blog_id')
            blog = BlogModel.objects.get(id=blog_id)
            categories = blog.categories.all()
            serializer = CategorySerializer(categories,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": "Blog post id is required"})
    def post(self,request):
        try:
            data = request.data
            category_name = data['name']
            category = Category(name=category_name)
            blog_id = data['blog_id']
            category.save()
            blog = BlogModel.objects.get(id=blog_id)
            category = Category(name=category_name)
            blog.categories.add(category)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": "Blog post id and category name are required"})
        
                
blogpost_crud_api = BlogPostCRUDAPI.as_view()
blogpost_comment_api = BlogPostComments.as_view()
blogpost_retrival_global_api = BlogPostGlobalRetrival.as_view()
        