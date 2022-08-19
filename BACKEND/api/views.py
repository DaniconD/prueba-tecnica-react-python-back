from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Community
import json

# Create your views here.
class CommunityView(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def get(self, request, id=0):
    if(id>0):
      communities=list(Community.objects.filter(id=id).values())
      if len(communities) > 0:
        community=communities[0]
        data={'message':"Success", 'community':community}
      else:
        data={'message':"Community not found..."}
      return JsonResponse(data)
    else:
      communities=list(Community.objects.values())
      if len(communities)>0:
        data={'message':"Success", 'communities':communities}
      else:
        data={'message':"Communities not found..."}
      return JsonResponse(data)

  def post(self, request):
    # print(request.body)
    jd=json.loads(request.body)
    # print(jd)
    Community.objects.create(name=jd['name'],category=jd['category'],parent_community=jd['parent_community'],short_description=jd['short_description'],description=jd['description'],)
    data={'message':"Success"}
    return JsonResponse(data)
  
  def put(self, request, id):
    jd=json.loads(request.body)
    communities=list(Community.objects.filter(id=id).values())
    if len(communities) > 0:
      community=Community.objects.get(id=id)
      community.name=jd['name']
      community.category=jd['category']
      community.parent_community=jd['parent_community']
      community.short_description=jd['short_description']
      community.description=jd['description']
      community.save()
      data={'message':"Success"}
    else:
      data={'message':"Community not found..."}
    return JsonResponse(data)

  
  def delete(self, request, id):
    communities=list(Community.objects.filter(id=id).values())
    if len(communities) > 0:
      Community.objects.filter(id=id).delete()
      data={'message':"Success"}
    else:
      data={'message':"Community not found..."}
    return JsonResponse(data)

  