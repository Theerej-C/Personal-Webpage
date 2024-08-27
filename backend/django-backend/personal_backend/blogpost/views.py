from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogPostSerializer
from .models import BlogModel,Comment
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
class BlogPostCRUDAPI(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        # Retrieve all blog posts
        blog_posts = BlogModel.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        # content = data['content']
        data['author_id'] = request.user.id
        data['author'] = request.user.username
        serializer = BlogPostSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def update(self,request):
         data = request.data
         id = data['id']
         blog_post = BlogModel.objects.get(id=id)
         serializer = BlogPostSerializer(blog_post, data=data)
         if(serializer.is_valid()):
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors)
    def delete(self,request):
        id = request.data['id']
        blog_post = BlogModel.objects.get(id=id)
        if (blog_post):
            blog_post.delete()
            return Response({"message": "Blog post deleted successfully"})
        else:
            return Response({"message": "Blog post not found"})

class BlogPostComments(APIView):
    def get(self,request):
        blog_id = request.data['id']
        # Retrieve all blog post comments
        blog = BlogModel.objects.get(id=id)
        comments = blog.comments.all()
        return Response(comments)
    def post(self,request):
        data = request.data
        comment_content = data['content']
        comment = Comment(content=comment_content,author_id=request.user.id)
        blog_id = data['blog_id']
        blog = BlogModel.objects.get(id=blog_id)
        blog.comments.add(comment)
        return Response({"message":"Comment added"})
blogpost_crud_api = BlogPostCRUDAPI.as_view()
        