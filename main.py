
from website import create_app

app = create_app()
#this is the entry point to the actual python app
if __name__=='__main__':
    app.run(debug=True) #this changes the code when you make changes 