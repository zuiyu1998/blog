from .models import BigTopic


def nva_context(request):
    big_topic_list = BigTopic.objects.all().order_by('id')
    return {
        'big_topic_list': big_topic_list,
    }