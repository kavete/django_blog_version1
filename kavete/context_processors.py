from kavete.models import Tag


def get_all_tags(request):
    all_tags = Tag.objects.all().order_by('?')[:10]
    return {
        'all_tags': all_tags
    }
