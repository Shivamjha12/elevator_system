from django.urls import path
from .views import ElevatorViewSet, ElevatorSystemViewSet

elevator_list = ElevatorViewSet.as_view({
    'get': 'list',
})
elevator_detail = ElevatorViewSet.as_view({
    'get': 'retrieve',
})
elevator_fetch_requests = ElevatorViewSet.as_view({
    'get': 'fetch_requests',
})
elevator_fetch_next_destination = ElevatorViewSet.as_view({
    'get': 'fetch_next_destination',
})
elevator_fetch_direction = ElevatorViewSet.as_view({
    'get': 'fetch_direction',
})
elevatorSystem_save_request = ElevatorSystemViewSet.as_view({
    'get': 'save_request',
})
elevatorSystem_assign_elevator = ElevatorSystemViewSet.as_view({
    'get': 'assign_elevator',
})
elevator_mark_maintenance = ElevatorViewSet.as_view({
    'post': 'mark_maintenance',
})
elevator_open_door = ElevatorViewSet.as_view({
    'post': 'open_door',
})
elevator_close_door = ElevatorViewSet.as_view({
    'post': 'close_door',
})
elevator_system_list = ElevatorSystemViewSet.as_view({
    'get': 'list',
})
elevator_system_initialize = ElevatorSystemViewSet.as_view({
    'post': 'initialize',
})
elevator_system_reset = ElevatorSystemViewSet.as_view({
    'post': 'reset',
})

urlpatterns = [
    path('elevator/', elevator_list, name='elevator-list'),
    path('elevator/<int:pk>/', elevator_detail, name='elevator-detail'),
    path('elevator/requests/<int:pk>/', elevator_fetch_requests, name='elevator-fetch-requests'),
    path('elevator/next-destination/<int:pk>/', elevator_fetch_next_destination, name='elevator-fetch-next-destination'),
    path('elevator/direction/<int:pk>/', elevator_fetch_direction, name='elevator-fetch-direction'),
    path('elevatorsystem/saverequest/<int:floor_no>', elevatorSystem_save_request, name='elevatorsystem-save-request'),
    path('elevatorsystem/assignnextrequest/', elevatorSystem_assign_elevator, name='elevatorsystem-assign_elevator'),
    path('elevator/mark-maintenance/<int:pk>/', elevator_mark_maintenance, name='elevator-mark-maintenance'),
    path('elevator/open-door/<int:pk>/', elevator_open_door, name='elevator-open-door'),
    path('elevator/close-door/<int:pk>/', elevator_close_door, name='elevator-close-door'),
    path('elevatorsystem/', elevator_system_list, name='elevator-system-list'),
    path('elevatorsystem/initialize/', elevator_system_initialize, name='elevator-system-initialize'),
    path('elevatorsystem/reset/', elevator_system_reset, name='elevator-system-reset'),
]
