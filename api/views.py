from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class health_check(APIView):
    def get(self, request ):
        return Response("if your are seeing this then , server is Up and Running",status=status.HTTP_200_OK)
    
class UserAPI(APIView):
    """The User API class is a view for handling API requests related to users."""

    def get(self, request):
        try:
            user_id = request.query_params.get('user_id')          

            if user_id:
                user = get_object_or_404(User, id=user_id)
                serializer = UserSerializer (user, many = False)
                
                user_data = serializer.data
                user_data['created'] = user.created
                user_data['is_active'] = user.is_active
                user_data['is_deleted'] = user.is_deleted

                return Response({
                "success": True,
                "message": f"User Details for {user.email}",
                "response": user_data,
                }, status=status.HTTP_200_OK)
            else:
                user = User.objects.all()
                serializer = UserSerializer(user, many = True)
                return Response({
                    "success": True,
                    "message": "All Users",
                    "response": serializer.data,
                }, status=status.HTTP_200_OK)

           
        except Exception as e:
            return Response(
                {"success": False, 
                "message": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "User created successfully",
                        "response": UserSerializer(user).data, 
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request):
        try:
            user_id = request.data.get('user_id')

            if not user_id:
                return Response(
                    {"success": False, "message": "No User ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user = get_object_or_404(User, id=user_id)

            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                user = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "User Updated successfully",
                        "response": UserSerializer(user).data,
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request):
        try:
            user_id = request.data.get('user_id')

            if not user_id:
                return Response(
                    {"success": False, "message": "No User ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user = get_object_or_404(User, id=user_id)
    
            user.delete()
    
            return Response(
                {"success": True, "message": "User Deleted successfully"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class WorkerAPI(APIView):
    """The Worker API class is a view for handling API requests related to Workers."""

    def get(self, request):
        try:
            worker_id = request.query_params.get('id')          

            if worker_id:
                worker = get_object_or_404(Worker, id=worker_id)
                serializer = WorkerSerializer (worker, many = False)
                
                worker_data = serializer.data
                worker_data['created'] = worker.created
                worker_data['is_active'] = worker.is_active
                worker_data['is_deleted'] = worker.is_deleted

                return Response({
                "success": True,
                "message": f"Worker Details for {worker.user}",
                "response": worker_data,
                }, status=status.HTTP_200_OK)
            else:
                workers = Worker.objects.all()
                serializer = WorkerSerializer(workers, many = True)
                return Response({
                    "success": True,
                    "message": "All Workers",
                    "response": serializer.data,
                }, status=status.HTTP_200_OK)

           
        except Exception as e:
            return Response(
                {"success": False, 
                "message": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            serializer = WorkerSerializer(data=request.data)
            if serializer.is_valid():
                worker = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Worker created successfully",
                        "response": WorkerSerializer(worker).data, 
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request):
        try:
            worker_id = request.data.get('id')

            if not worker_id:
                return Response(
                    {"success": False, "message": "No Worker ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            worker = get_object_or_404(Worker, id=worker_id)

            serializer = WorkerSerializer(worker, data=request.data, partial=True)
            if serializer.is_valid():
                worker = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Worker Updated successfully",
                        "response": WorkerSerializer(worker).data,
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request):
        try:
            worker_id = request.data.get('id')

            if not worker_id:
                return Response(
                    {"success": False, "message": "No Worker ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            worker = get_object_or_404(Worker, id=worker_id)
    
            worker.delete()
    
            return Response(
                {"success": True, "message": "Worker Deleted successfully"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class CompanyAPI(APIView):
    """The Company API class is a view for handling API requests related to Company."""

    def get(self, request):
        try:
            company_id = request.query_params.get('id')          

            if company_id:
                company = get_object_or_404(Company, id=company_id)
                serializer = CompanySerializer (company, many = False)
                
                company_data = serializer.data
                company_data['created'] = company.created
                company_data['is_active'] = company.is_active
                company_data['is_deleted'] = company.is_deleted

                return Response({
                "success": True,
                "message": f"Worker Details for {company.name}",
                "response": company_data,
                }, status=status.HTTP_200_OK)
            
            else:
                companys = Company.objects.all()
                serializer = CompanySerializer(companys, many = True)
                return Response({
                    "success": True,
                    "message": "All Companies",
                    "response": serializer.data,
                }, status=status.HTTP_200_OK)

           
        except Exception as e:
            return Response(
                {"success": False, 
                "message": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            serializer = CompanySerializer(data=request.data)
            if serializer.is_valid():
                company = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Company created successfully",
                        "response": CompanySerializer(company).data, 
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request):
        try:
            company_id = request.data.get('id')

            if not company_id:
                return Response(
                    {"success": False, "message": "No Company ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            company = get_object_or_404(Company, id=company_id)

            serializer = CompanySerializer(company, data=request.data, partial=True)
            if serializer.is_valid():
                company = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Company Updated successfully",
                        "response": CompanySerializer(company).data,
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request):
        try:
            company_id = request.data.get('id')

            if not company_id:
                return Response(
                    {"success": False, "message": "No Company ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            company = get_object_or_404(Company, id=company_id)
    
            company.delete()
    
            return Response(
                {"success": True, "message": "Company Deleted successfully"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
   
class BuildingAPI(APIView):
    """The Building API class is a view for handling API requests related to Building."""

    def get(self, request):
        try:
            building_id = request.query_params.get('id')          

            if building_id:
                building = get_object_or_404(Building, id=building_id)
                serializer = BuildingSerializer (building, many = False)
                
                building_data = serializer.data
                building_data['created'] = building.created
                building_data['is_active'] = building.is_active
                building_data['is_deleted'] = building.is_deleted

                return Response({
                "success": True,
                "message": f"Building Details for {building.name}",
                "response": building_data,
                }, status=status.HTTP_200_OK)
            
            else:
                buildings = Building.objects.all()
                serializer = BuildingSerializer(buildings, many = True)
                return Response({
                    "success": True,
                    "message": "All Buildings",
                    "response": serializer.data,
                }, status=status.HTTP_200_OK)

           
        except Exception as e:
            return Response(
                {"success": False, 
                "message": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            serializer = BuildingSerializer(data=request.data)
            if serializer.is_valid():
                building = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Building created successfully",
                        "response": BuildingSerializer(building).data, 
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request):
        try:
            building_id = request.data.get('id')

            if not building_id:
                return Response(
                    {"success": False, "message": "No Building ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            building = get_object_or_404(Building, id=building_id)

            serializer = BuildingSerializer(building, data=request.data, partial=True)
            if serializer.is_valid():
                building = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Building Updated successfully",
                        "response": BuildingSerializer(building).data,
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request):
        try:
            building_id = request.data.get('id')

            if not building_id:
                return Response(
                    {"success": False, "message": "No Building ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            building = get_object_or_404(Building, id=building_id)
    
            building.delete()
    
            return Response(
                {"success": True, "message": "Building Deleted successfully"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        


class OfficeAPI(APIView):
    """The Office API class is a view for handling API requests related to Office."""

    def get(self, request):
        try:
            office_id = request.query_params.get('id')          

            if office_id:
                office = get_object_or_404(Office, id=office_id)
                serializer = OfficeSerializer (office, many = False)
                
                office_data = serializer.data
                office_data['created'] = office.created
                office_data['is_active'] = office.is_active
                office_data['is_deleted'] = office.is_deleted

                return Response({
                "success": True,
                "message": f"Office Details for {office.id}",
                "response": office_data,
                }, status=status.HTTP_200_OK)
            
            else:
                offices = Office.objects.all()
                serializer = OfficeSerializer(offices, many = True)
                return Response({
                    "success": True,
                    "message": "All Offices",
                    "response": serializer.data,
                }, status=status.HTTP_200_OK)

           
        except Exception as e:
            return Response(
                {"success": False, 
                "message": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            serializer = OfficeSerializer(data=request.data)
            if serializer.is_valid():
                office = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Office created successfully",
                        "response": OfficeSerializer(office).data, 
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request):
        try:
            office_id = request.data.get('id')

            if not office_id:
                return Response(
                    {"success": False, "message": "No Office ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            office = get_object_or_404(Office, id=office_id)

            serializer = OfficeSerializer(office, data=request.data, partial=True)
            if serializer.is_valid():
                office = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Office Updated successfully",
                        "response": OfficeSerializer(office).data,
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request):
        try:
            office_id = request.data.get('id')

            if not office_id:
                return Response(
                    {"success": False, "message": "No Office ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            office = get_object_or_404(Office, id=office_id)
    
            office.delete()
    
            return Response(
                {"success": True, "message": "Office Deleted successfully"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class UserOfficeAPI(APIView):
    """The User Office API class is a view for handling API requests related to User Office."""

    def get(self, request):
        try:
            user_office_id = request.query_params.get('id')          

            if user_office_id:
                user_office = get_object_or_404(UserOffice, id=user_office_id)
                serializer = UserOfficeSerializer (user_office, many = False)
                
                user_office_data = serializer.data
                user_office_data['created'] = user_office.created
                user_office_data['is_active'] = user_office.is_active
                user_office_data['is_deleted'] = user_office.is_deleted

                return Response({
                "success": True,
                "message": f"User_office Details for {user_office.id}",
                "response": user_office_data,
                }, status=status.HTTP_200_OK)
            
            else:
                user_offices = UserOffice.objects.all()
                serializer = UserOfficeSerializer(user_offices, many = True)
                return Response({
                    "success": True,
                    "message": "All User offices",
                    "response": serializer.data,
                }, status=status.HTTP_200_OK)

           
        except Exception as e:
            return Response(
                {"success": False, 
                "message": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            serializer = UserOfficeSerializer(data=request.data)
            if serializer.is_valid():
                user_office = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "User Office created successfully",
                        "response": UserOfficeSerializer(user_office).data, 
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request):
        try:
            user_office_id = request.data.get('id')

            if not user_office_id:
                return Response(
                    {"success": False, "message": "No User_office ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user_office = get_object_or_404(UserOffice, id=user_office_id)

            serializer = UserOfficeSerializer(user_office, data=request.data, partial=True)
            if serializer.is_valid():
                user_office = serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "User_office Updated successfully",
                        "response": UserOfficeSerializer(user_office).data,
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"success": False, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request):
        try:
            user_office_id = request.data.get('id')

            if not user_office_id:
                return Response(
                    {"success": False, "message": "No User_office ID Provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user_office = get_object_or_404(UserOffice, id=user_office_id)
    
            user_office.delete()
    
            return Response(
                {"success": True, "message": "User_office Deleted successfully"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
