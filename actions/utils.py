from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import datetime
from .models import Action


def create_action(user,verb,target=None):
    # 检查最后一分钟内的相同的动作
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user_id=user.id,verb=verb,created__gte=last_minute)

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions =similar_actions.filter(target_ct=target_ct,target_id=target.id)

    if not similar_actions:
        #最后一分钟找不到相似的记录
        action = Action(user=user,verb=verb,target=target)
        action.save()
        return True
    return False
