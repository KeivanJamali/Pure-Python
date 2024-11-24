from KPG import KPG

docs_path = r"D:\All Python\Pure-Python\P4\06-PromptEngineering\Project 2 - MyWebsiteAI\docs"
log_path = r"D:\All Python\Pure-Python\P4\06-PromptEngineering\Project 2 - MyWebsiteAI\RR"
user = KPG(api_key_groq="aa",
            api_key_openai="aa",
            model_name=KPG.models["Meta"][0],
            temp=0.2)
user.fit(documents_folder_path=docs_path,
            log_folder_path=log_path,
            user_id="k1")
q = "about life."
response = user.generate(query=q)