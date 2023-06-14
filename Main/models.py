from django.db import models
from django.contrib.postgres.fields import ArrayField


class Elevator(models.Model):
    elevator_id = models.IntegerField(primary_key=True)
    current_floor = models.IntegerField(default=0)
    direction = models.CharField(max_length=20,default="Stop")
    is_running = models.BooleanField(default=False)
    is_door_open = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    is_operational = models.BooleanField(default=True)
    requests = ArrayField(models.IntegerField(), default=list)

    def __str__(self):
        return f"Elevator {self.elevator_id}"
    

    def move_up(self):
        self.current_floor += 1
        self.direction = "Up"
        self.save()

    def move_down(self):
        self.current_floor -= 1
        self.direction = "Down"
        self.save()

    def open_door(self):
        self.is_door_open = True
        self.save()

    def close_door(self):
        self.is_door_open = False
        self.save()

    def start(self):
        self.is_running = True
        self.save()

    def stop(self):
        self.is_running = False
        self.save()
        
    def add_request(self, floor):
        self.requests.append(floor)
        self.save()

    @classmethod
    def initialize_elevators(cls, num_elevators):
        for elevator_id in range(num_elevators):
            cls.objects.create(elevator_id=elevator_id)


class ElevatorSystem(models.Model):
    num_floors = models.IntegerField(default=10)
    elevatorsystem_id = models.AutoField(primary_key=True)
    requests = ArrayField(models.IntegerField(), default=list)
    
    def __str__(self):
        return f"ElevatorSystem {self.elevatorsystem_id}"
    
    @classmethod
    def assign_elevator(cls,elevatorsystem,floor_no, elevators):
        if floor_no < 0 or floor_no >= elevatorsystem.num_floors:
            return f"Invalid floor number. Please provide a floor between 0 and {elevatorsystem.num_floors - 1}."

        optimal_elevator = None
        min_distance = float('inf')

        for elevator in elevators:
            distance = abs(elevator.current_floor - floor_no)
            if elevator.is_operational and not elevator.is_running and distance < min_distance :
                optimal_elevator = elevator
                min_distance = distance

        if optimal_elevator is not None:
            optimal_elevator.start()

            while optimal_elevator.current_floor != floor_no:
                if optimal_elevator.current_floor < floor_no:
                    optimal_elevator.move_up()
                elif optimal_elevator.current_floor > floor_no:
                    optimal_elevator.move_down()

            optimal_elevator.requests.append(floor_no)
            optimal_elevator.stop()

            return f"Elevator {optimal_elevator.elevator_id} is assigned to floor {floor_no}"
        else:
            return "No available elevator to assign"
    
    
    # @classmethod
    # def assign_elevator(self, elevatorsystem,floor_no, elevators):
    #     if floor_no < 0 or floor_no >= elevatorsystem.num_floors:
    #         return f"Invalid floor number. Please provide a floor between 0 and {elevatorsystem.num_floors - 1}."

    #     optimal_elevator = None
    #     min_distance = float('inf')

    #     for elevator in elevators:
    #         distance = abs(elevator.current_floor - floor_no)
    #         if not elevator.is_running and distance < min_distance:
    #             optimal_elevator = elevator
    #             min_distance = distance

    #     if optimal_elevator is not None:
    #         optimal_elevator.start()

    #         while optimal_elevator.current_floor != floor_no:
    #             if optimal_elevator.current_floor < floor_no:
    #                 optimal_elevator.move_up()
    #             elif optimal_elevator.current_floor > floor_no:
    #                 optimal_elevator.move_down()

    #         optimal_elevator.add_request(floor_no)
    #         optimal_elevator.stop()

    #         return f"Elevator {optimal_elevator.elevator_id} is assigned to floor {floor_no}"
    #     else:
    #         return "No available elevator to assign"

        
    @classmethod
    def add_request(self, floor):
        new_requests = ElevatorSystem.objects.get(elevatorsystem_id=0)
        print(new_requests,"_---__--___---_-----_-_-_-___-----------------------")
        new_requests.requests.append(floor)
        print(new_requests,"_---__--___---_-----_-_-_-___-----------------------")
        new_requests.save()
    
    def remove_request(self):
        new_list = self.requests
        element=new_list.pop(0)
        self.requests = new_list
        self.save()
        return element