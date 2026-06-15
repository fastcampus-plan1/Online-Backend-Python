from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_str

def log_action(user, object, action_flag, change_message=''):
    """
    user: 로그를 기록할 사용자 객체
    object: 로그와 관련된 객체
    action_flag: 수행된 액션의 타입 (ADDITION, CHANGE, DELETION 중 하나)
    change_message: 액션에 대한 추가 메시지 또는 설명
    """
    LogEntry.objects.log_action(
        user_id=user.pk,
        content_type_id=ContentType.objects.get_for_model(object).pk,
        object_id=object.pk,
        object_repr=force_str(object),
        action_flag=action_flag,
        change_message=change_message
    )

def log_addition(user, object, change_message=''):
    log_action(user, object, ADDITION, change_message)

def log_change(user, object, change_message=''):
    log_action(user, object, CHANGE, change_message)

def log_deletion(user, object, change_message=''):
    log_action(user, object, DELETION, change_message)

