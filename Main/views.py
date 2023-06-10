from rest_framework import viewsets
from rest_framework.response import Response
from .models import Elevator, ElevatorSystem
from .serializers import ElevatorSerializer, ElevatorSystemSerializer

class ElevatorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Elevator.objects.all()
        serializer = ElevatorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            queryset = Elevator.objects.get(elevator_id=pk)
        except Elevator.DoesNotExist:
            return Response("NO elevator exist with id"+ str(pk))
        serializer = ElevatorSerializer(queryset)
        return Response(serializer.data)

    def fetch_requests(self, request, pk):
        try:
            elevator = Elevator.objects.get(elevator_id=pk)
        except Elevator.DoesNotExist:
            return Response("No elevator found with id " + str(pk))
        return Response(elevator.requests)

    def fetch_next_destination(self, request):
        try:
            elevatorsys = ElevatorSystem.objects.get(elevatorsystem_id=0)
        except ElevatorSystem.DoesNotExist:
            return Response("No elevator Reuests found ")
        if elevatorsys.requests:
            return Response(elevatorsys.requests[0])
        else:
            return Response("No requests for the elevator")

    def fetch_direction(self, request, pk):
        elevator = Elevator.objects.get(elevator_id=pk)
        return Response(f"Current floor is {elevator.current_floor} and direction is {elevator.direction}")


    def mark_maintenance(self, request, pk):
        try:
            elevator = Elevator.objects.get(elevator_id=pk)
        except Elevator.DoesNotExist:
            return Response(f"Elevator does not exist with id {pk}")
        elevator.is_operational = False
        elevator.save()
        return Response("Elevator marked as not working")

    def open_door(self, request, pk):
        elevator = Elevator.objects.get(elevator_id=pk)
        elevator.open_door()
        return Response("Door opened")

    def close_door(self, request, pk):
        elevator = Elevator.objects.get(elevator_id=pk)
        elevator.close_door()
        return Response("Door closed")

class ElevatorSystemViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ElevatorSystem.objects.all()
        serializer = ElevatorSystemSerializer(queryset, many=True)
        return Response(serializer.data)

    def initialize(self, request):
        num_elevators = request.data.get('num_elevators')
        no_floor = request.data.get('no_floors')
        try:
            check_intializing = ElevatorSystem.objects.get(elevatorsystem_id=0)
        except ElevatorSystem.DoesNotExist:
           check_intializing = None
           
        if (num_elevators and no_floor is not None) and check_intializing is None:
            Elevator.initialize_elevators(num_elevators)
            ElevatorSystem.objects.create(elevatorsystem_id=0,num_floors=no_floor)
            return Response(f"{num_elevators} elevators initialized")
        else:
            if check_intializing is not None:
                return Response("Elevator System is already initialized")
            else:
                return Response("Invalid number of elevators")

    def reset(self, request):
        Elevator.objects.all().delete()
        ElevatorSystem.objects.all().delete()
        return Response("All elevator objects have been deleted")
    
    def save_request(self, request, floor_no):
        try:
            elevator = ElevatorSystem.objects.get(elevatorsystem_id=0)
        except:
            return Response("No elevator System exists try again after Intializing the system")
        if elevator is not None and floor_no <= elevator.num_floors and floor_no>=0:
            ElevatorSystem.add_request(floor_no)
            return Response("Request saved successfully")
        else:
            if floor_no > elevator.num_floors:
                return Response(f"floor no {floor_no} you request is invalid, {floor_no} floor is greater than top floor {elevator.num_floors}")
            return Response("Something went wrong")
        
    def assign_elevator(self,request):
        elevators = Elevator.objects.all()
        try:
            elevatorsystem = ElevatorSystem.objects.get(elevatorsystem_id=0)
        except ElevatorSystem.DoesNotExist:
            return Response("ElevatorSytem doesn't exist")
        
        request_list = elevatorsystem.requests
        size  = len(request_list)
        if size>=1:
            next_floor = request_list[0]
            elevatorsystem.requests.pop(0)
            response = elevatorsystem.assign_elevator(elevatorsystem,next_floor, elevators)
            elevatorsystem.save()
            return Response(response)
        else:
            return Response("There is no request currently in the elevator system")
        

