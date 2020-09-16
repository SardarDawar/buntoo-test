from .models import Friend_List


def friends(request):
    friends = None

    if request.user.is_authenticated:
        try:
            friends = Friend_List.objects.get(user=request.user).friend_name.all()
        except Exception as err:
          print(err)

    return {"friends": friends}
