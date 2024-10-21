from django.views import generic

class PostView(generic.DetailView):
    template_name = 'post_detail.html'
    
    def get_object(self, queryset = None):
        from blog.models import Post
        
        slug = self.kwargs.get('slug')
        
        context = Post.objects.get(slug = slug)
        
        return context