from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        from blog.models import Post
        
        context = super().get_context_data(**kwargs)
        
        posts = Post.objects.filter(status=1).order_by('-created_on')
        
        context['posts'] = posts
        
        return context