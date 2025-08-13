from dotenv import load_dotenv
load_dotenv()
from graph.graph import app

if __name__=="__main__":
    print("Today: CRAG")
    print(app.invoke(input={"question": "Who is keivan jamali?"}))