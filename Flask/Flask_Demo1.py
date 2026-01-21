from flask import Flask

app=Flask(__name__) #object created 

@app.route('/hello') #This si the API url

def hello():
    return "Hello Eagles"

@app.route('/welcome')

def welcome():
    return "Welcome to social Eagles Community"

#main function to trigger the functions 

if __name__=='__main__':
    app.run(debug=True)






#######################################################################################3

# I see the issue clearly 👍. In Flask, only functions that are decorated with @app.route(...) are exposed as endpoints.
# In your code, you decorated hello() with @app.route('/'), so Flask knows to call it when someone visits the root URL /. But welcome() has no route decorator, so Flask doesn’t know when to run it — it just sits there unused.
