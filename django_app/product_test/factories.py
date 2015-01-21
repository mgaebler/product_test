# coding: utf-8
import factory
from django.utils.timezone import now
from product_test import models
from datetime import timedelta

class BrandTestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand
    name = factory.Sequence(lambda n: "TestBrand #%s" % n)
    slug = factory.Sequence(lambda n: "test-brand-slug-%s" % n)
    logo = factory.django.ImageField(color='yellow')


class ProductTestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductTest
    title = factory.Sequence(lambda n: "TestTitle #%s" % n)
    slug = factory.Sequence(lambda n: "test-slug-%s" % n)
    hero_image = factory.django.ImageField(color='green', width=950, height=284)
    list_image = factory.django.ImageField(color='blue', width=310, height=210)
    logo = factory.django.ImageField(color='red', width=232, height=52)
    state = 'published'
    published_at = now() - timedelta(0, 60)

    custom_html = """
      <div class='test-class'>
        <h1>This headline color is green - H1</h1>
        <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. </p>
        <h2>This headline color is yellow - H2</h2>
        <p>Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. </p>
        <h3>This headline color is red - H3</h3>
        <p>Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. </p>
      </div>
    """

    custom_css = """
        div.test-class h1 {color: green};
        div.test-class h2 {color: yellow};
        div.test-class h3 {color: red};
    """

    brand = factory.SubFactory(BrandTestFactory)

