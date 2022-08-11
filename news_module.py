import requests

from speak_module import speak  

    
def get_news(): 
        # BBC news api 
        main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=3b651a51643045f7a8d0c4ee775c68de"
    
        # fetching data in json format 
        open_bbc_page = requests.get(main_url).json() 
    
        # getting all articles in a string article 
        article = open_bbc_page["articles"] 
    
        # empty list which will  
        # contain all trending news 
        results = [] 
        
        for ar in article: 
            results.append(ar["title"]) 
            
        for i in range(len(results)): 
            
            # printing all trending news 
            speak(str(i + 1) + " " +results[i])
            print(str(i + 1) + " " +results[i]) 
        speak("So these were the top news from today")