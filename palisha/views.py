from django.views.generic import TemplateView
from products.models import Product, ProductImage


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context["products"] = products
        context["carousel"] = []

        for product in products:
            product_image = ProductImage.objects.filter(product=product, is_thumbnail=True).first()
            context["carousel"].append({'product_name': product.name, 'product_image': product_image.image.url})
            print('product_image.image.url: ', product_image.image.url)


        # context["carousel"] = Product.objects.all()
        # products = context["products"]
        # print(context["products"])

        return context
