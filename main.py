
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Search route
@app.route('/search', methods=['POST'])
def search():
    # Get user input
    destination = request.form.get('destination')
    
    # Generate a list of destinations
    destinations = ['Amsterdam', 'Rotterdam', 'The Hague', 'Utrecht', 'Eindhoven']
    
    # Return the list of destinations
    return render_template('destinations.html', destinations=destinations)

# Destinations route
@app.route('/destinations')
def destinations():
    # Get the list of destinations
    destinations = ['Amsterdam', 'Rotterdam', 'The Hague', 'Utrecht', 'Eindhoven']
    
    # Render the destinations page
    return render_template('destinations.html', destinations=destinations)

# Destination details route
@app.route('/destination_details/<destination>')
def destination_details(destination):
    # Get the destination details
    destination_details = {'name': destination, 'description': 'A beautiful city in the Netherlands.'}
    
    # Render the destination details page
    return render_template('destination_details.html', destination_details=destination_details)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
