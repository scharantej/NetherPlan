## Flask Application Design for Travel Planner Project

### HTML Files
- **home.html**: The main page of the application, where users can enter their travel preferences and search for destinations.
- **destinations.html**: The page that displays a list of destinations that match the user's criteria.
- **destination_details.html**: The page that displays detailed information about a specific destination, including its name, description, and attractions.

### Routes
- **home**: The home page route, which renders the `home.html` file.
- **search**: The search route, which handles user input and returns a list of destinations that match their criteria.
- **destinations**: The destinations route, which renders the `destinations.html` file and passes a list of destinations as a variable.
- **destination_details**: The destination details route, which handles the request for a specific destination and renders the `destination_details.html` file, passing the destination information as a variable.