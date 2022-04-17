from app import app
if __name__=="__main__":
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
 
  app.run(port=7000)
  