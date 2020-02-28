from django import template
from ..models import Topic, BigTopic


register = template.Library()


@register.simple_tag()
def get_list_by_big_topic(id):
    topic_list = Topic.objects.filter(big_topic_id=id)
    return topic_list

