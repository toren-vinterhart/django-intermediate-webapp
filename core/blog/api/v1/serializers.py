from rest_framework import serializers
from blog.models import Post, Category
from accounts.models import Profile


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    # We can set items to read_only here or in Meta class
    # author = serializers.ReadOnlyField()
    # author = serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source='get_snippet') # get_snippet is a method in Post model
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True) # get_absolute_api_url is a method in Post model
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url') # method name must be get_{field_name} e.g. get_absolute_url if we don't set method_name
    # category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all()) # If we want show category name or other fields instead of category id we should do this
    # category = CategorySerializer() # We can use CategorySerializer to show all category fields

    class Meta:
        model = Post
        fields = ['id', 'author', 'image', 'title', 'content', 'snippet', 'relative_url', 'absolute_url', 'category', 'status', 'created_date', 'published_date' ]
        # exclude = ['status', 'updated_date']
        read_only_fields = ['author']

    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        # print(request.parser_context['kwargs'].get('pk'))
        obj_pk = request.parser_context.get('kwargs').get('pk')
        if obj_pk:
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)
        rep['category'] = CategorySerializer(instance.category, context={'request': request}).data
        # rep['name'] = 'Jack' # Everything we want to show can add in this way 
        return rep
    
    def create(self, validated_data):
        # validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        validated_data['author'] = Profile.objects.get(user=self.context.get('request').user)
        return super().create(validated_data)