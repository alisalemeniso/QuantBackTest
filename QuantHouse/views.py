from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class MobileAverage(APIView):
    def post(self, request, *args, **kwargs):
        try:
            list = request.data.get("inputList")
            N = request.data.get("averageNbr")
            if len(list)<N:
                return Response({'error': False, 'result': None},
                                status=HTTP_200_OK)
            mobile_avgs = []
            list_sum= [0]
            for i in range(len(list)):
                list_sum.append(list_sum[i] + list[i])
                if i+1 >= N:
                    mobile_ave = (list_sum[i+1] - list_sum[i+1 - N]) / N
                    mobile_avgs.append(mobile_ave)
            return Response({'error': False, 'result': mobile_avgs},
                            status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': True, 'error_msg': 'Server Error'})
