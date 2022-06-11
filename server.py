from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__) 

users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]



@app.route("/")
def test():
    return render_template("ht.html", first_name = "first_name", last_name = "last_name", users=users)


 # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.