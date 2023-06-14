# Elevator System API

This is the API documentation for the Elevator System project. It provides endpoints to manage elevators and elevator systems.

## Endpoints

### Get Elevator List

Retrieves a list of all elevators.

- **URL:** `/`
- **Method:** GET
- Return all the list of elevators in the elevator system.

### Get Elevator Detail

Retrieves details of a specific elevator.

- **URL:** `/elevator/{id}/`
- **Method:** GET
- Return the detail about elevator on the basis of elevator id passed.

### Fetch Elevator Requests

Fetches the requests made to a specific elevator.

- **URL:** `/elevator/requests/{id}/`
- **Method:** GET
- Return the Requests[] get by the particular elevator.

### Fetch Elevator Next Destination

Fetches the next destination floor of a specific elevator.

- **URL:** `/elevator/next-destination/{id}/`
- **Method:** GET
- Return the next floor/destionation which is in elevator system request queue.

### Fetch Elevator Direction

Fetches the current direction of a specific elevator.

- **URL:** `/elevator/direction/{id}/`
- **Method:** GET
- Return the Direction of Elevator `Up`,`Down` or `Stop` when elevator id is passed.

### Save Elevator Request

Saves a request for a specific floor in the elevator system.

- **URL:** `elevatorsystem/addrequest/{floor_no}/`
- **Method:** GET
- It saves the request passed by the user to the elevator system request queue.

### Assign Next Elevator Request

Assigns the next request to an available elevator.

- **URL:** `/elevatorsystem/assignnextrequest/`
- **Method:** GET
- This endpoints return the first request from request queue of elevator system and assign to particular elevator and return that elevtor id.

### Mark Elevator Maintenance

Marks a specific elevator as under maintenance.

- **URL:** `elevator/mark-maintenance/{id}/`
- **Method:** POST
- This endpoint help to mark a particular elevator as not operational on the basis of elevator_id passed.

### Open Elevator Door

Opens the door of a specific elevator.

- **URL:** `/elevator/open-door/{id}/`
- **Method:** POST
- Help to change the state of a particular elevator by changing the is_door_open field to True.

### Close Elevator Door

Closes the door of a specific elevator.

- **URL:** `/elevator/close-door/{id}/`
- **Method:** POST
- Help to change the state of a particular elevator by changing the is_door_open field to False.

### Initialize Elevator System

Initializes the elevator system with a specified number of elevators.

- **URL:** `/elevatorsystem/initialize/`
- **Method:** POST
- This endpoint takes two parameters as json, `num_elevators` and `no_floors` which help to initialize the elevator system. The num_elevators value means no.of elevators in elevator system and no_floors means no.of floors in the elevator system[The range in which elevator system serve service].

### Reset Elevator System

Resets the elevator system to its initial state.

- **URL:** `/elevatorsystem/reset/`
- **Method:** POST
- It just help to reset the whole system. After that we have to intialize the system again. 

## Conclusion

These are the available endpoints for the Elevator System API. Use them to interact with the elevators and manage the elevator systems efficiently.
