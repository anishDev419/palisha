from django.views.generic import TemplateView
from products.models import Product


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        print(context["products"])
        for p in context["products"]:
            print("p",p)
        return context
