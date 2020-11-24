from rest_framework import serializers
from .models import Article


'''
Our SnippetSerializer class is replicating a lot of information that's also
contained in the Snippet model. It would be nice if we could keep our code a
bit more concise.

In the same way that Django provides both Form classes and ModelForm classes,
 REST framework includes both Serializer classes, and ModelSerializer classes.

Let's look at refactoring our serializer using the ModelSerializer class.
Open the file snippets/serializers.py again, and replace the SnippetSerializer
 class with the following.
'''

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']

'''
python manage.py shell

from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))
'''


"""
The first thing we need to get started on our Web API is to provide a way of
serializing and deserializing the snippet instances into representations such
as json. We can do this by declaring serializers that work very similar to
Django's forms. Create a file in the snippets directory named serializers.py
and add the following.
"""

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     author = serializers.CharField(max_length=200)
#     email = serializers.EmailField(max_length=200)
#     date = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         """
#         Create and return a new 'Article' instance, given the validated data.
#         """
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing 'Article' instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.code)
#         instance.email = validated_data.get('email', instance.linenos)
#         instance.date = validated_data.get('date', instance.language)
#         instance.save()
#         return instance
#


'''
working with serializers

python manage.py shell

Okay, once we've got a few imports out of the way, let's create a couple of code snippets to work with.

from api_basic.models import Article
from api_basic.serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

a = Article(title='First Article', author='shahriar', email='shahriar@gmail.com')
a.save()

b = Article(title='Second Article', author='john', email='john@gmail.com')
b.save()

We've now got a few snippet instances to play with. Let's take a look at serializing one of those instances.

serializer = ArticleSerializer(a)
serializer.data
# {'title': 'First Article', 'author': 'shahriar', 'email': 'shahriar@gmail.com', 'date': '2020-11-24T02:46:26.578608Z'}

At this point we've translated the model instance into Python native datatypes. To finalize the serialization process we render the data into json.

content = JSONRenderer().render(serializer.data)
content
# b'{"title":"First Article","author":"shahriar","email":"shahriar@gmail.com","date":"2020-11-24T02:46:26.578608Z"}'

We can also serialize querysets instead of model instances. To do so we simply add a many=True flag to the serializer arguments.

serializer = ArticleSerializer(Article.objects.all(), many=True)
serializer.data
# [OrderedDict([('title', 'First Article'), ('author', 'shahriar'), ('email', 'shahriar@gmail.com'), ('date', '2020-11-24T02:46:26.578608Z')]), OrderedDict([('title', 'Second Article'), ('author', 'john'), ('email', 'john@gmail.com'), ('date', '2020-11-24T02:48:16.252149Z')])]
'''
