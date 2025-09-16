from flask import Flask, render_template, request, redirect, url_for
import datetime

# Create Flask application instance
app = Flask(__name__)

# Configure secret key for forms (required for CSRF protection)
app.config['SECRET_KEY'] = 'f3ebcaae866b8c4839d1e5229b05d62e6ac99153675bb6ed'

@app.route('/')
def home():
    """
    Home route that displays the main greeting form
    """
    return render_template('index.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    """
    Route to handle form submission and display personalized greeting
    Accepts both GET and POST methods
    """
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '').strip()
        greeting_type = request.form.get('greeting_type', 'hello')
        
        # Validate input
        if not name:
            error_message = "Please enter your name!"
            return render_template('index.html', error=error_message)
        
        # Get current time for time-based greetings
        current_hour = datetime.datetime.now().hour
        
        # Determine time-based greeting
        if current_hour < 12:
            time_greeting = "Good morning"
        elif current_hour < 18:
            time_greeting = "Good afternoon"
        else:
            time_greeting = "Good evening"
        
        # Create greeting based on selected type
        greeting_messages = {
            'hello': f"Hello, {name}! Welcome to our Flask application!",
            'formal': f"Good day, {name}. It's a pleasure to meet you.",
            'casual': f"Hey there, {name}! How's it going?",
            'time_based': f"{time_greeting}, {name}! Hope you're having a great day!",
            'enthusiastic': f"🎉 Welcome, {name}! We're so excited to have you here! 🎉"
        }
        
        greeting_message = greeting_messages.get(greeting_type, greeting_messages['hello'])
        
        return render_template('greeting.html', 
                             name=name, 
                             greeting=greeting_message,
                             time_greeting=time_greeting)
    
    # If GET request, redirect to home
    return redirect(url_for('home'))

@app.route('/about')
def about():
    """
    About page route
    """
    return render_template('about.html')

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)