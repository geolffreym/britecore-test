from django.http import JsonResponse
from django.http import Http404
from django.views.generic import View, TemplateView
from .models import RiskModel

"""
From scratch endpoints
Can be improved with GraphQL
"""


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class RiskView(View):
    def get(self, request, *args, **kwargs):
        """
        Handle get request for endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # Get param risk_pk to handle risk
        risk_pk = kwargs.get('risk_pk')

        try:
            if risk_pk:
                # Try get the risk model with fields based on risk type
                risk_model = RiskModel.get_serialized_fields(
                    [risk_pk]
                )

                # If `RiskModel` exists then return the json data
                return JsonResponse(risk_model, safe=False)

        except RiskModel.DoesNotExist:
            raise Http404

        # If not risk passed return `all` risks
        return JsonResponse(RiskModel.get_serialized_fields(
            [risk.risk_type.pk for risk in RiskModel.objects.all()]
        ), safe=False)
