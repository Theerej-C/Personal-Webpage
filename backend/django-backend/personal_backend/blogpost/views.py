from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import BlogSerializer, CommentSerializer, TagSerializer, CategorySerializer
from .models import BlogModel, Comment, Tag, Category

class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BlogModel.objects.filter(author_id=self.request.user.id)

    def create(self, request):
        data = request.data
        data['author_id'] = request.user.id
        data['author'] = request.user.username
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        blog_post = self.get_object()
        serializer = self.get_serializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        blog_post = self.get_object()
        blog_post.delete()
        return Response({"message": "Blog post deleted successfully"})

class BlogPostGlobalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        blog_id = self.request.query_params.get('blog_id')
        if blog_id:
            return Comment.objects.filter(blog_id=blog_id)
        return Comment.objects.all()

    def create(self, request):
        data = request.data
        comment_content = data['content']
        comment = Comment(content=comment_content, author_id=request.user.id)
        comment.save()
        blog_id = data['blog_id']
        blog = BlogModel.objects.get(id=blog_id)
        blog.comments.add(comment)
        serializer = self.get_serializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        comment = self.get_object()
        serializer = self.get_serializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        comment = self.get_object()
        comment.delete()
        return Response({"message": "Comment deleted successfully"})

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        blog_id = self.request.query_params.get('blog_id')
        if blog_id:
            return Tag.objects.filter(blog_id=blog_id)
        return Tag.objects.all()

    def create(self, request):
        data = request.data
        tag_name = data['name']
        tag = Tag(name=tag_name)
        tag.save()
        blog_id = data['blog_id']
        blog = BlogModel.objects.get(id=blog_id)
        blog.tags.add(tag)
        serializer = self.get_serializer(tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        blog_id = self.request.query_params.get('blog_id')
        if blog_id:
            return Category.objects.filter(blog_id=blog_id)
        return Category.objects.all()

    def create(self, request):
        data = request.data
        category_name = data['name']
        category = Category(name=category_name)
        category.save()
        blog_id = data['blog_id']
        blog = BlogModel.objects.get(id=blog_id)
        blog.categories.add(category)
        serializer = self.get_serializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)