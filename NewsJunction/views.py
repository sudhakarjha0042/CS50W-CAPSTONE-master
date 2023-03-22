from django.shortcuts import render
import requests
from .models import *
from django.shortcuts import render
from gtts import gTTS
from googletrans import Translator
from gnews import GNews
from django.http import JsonResponse
from newspaper import Article
from pathlib import Path
import json
from django.contrib.auth.decorators import login_required

BASE_DIR = Path(__file__).resolve().parent.parent


@login_required
def news(request,country_code):
    if not request.user.is_authenticated:
        response = JsonResponse({'error': 'User not authenticated'})
        response.status_code = 401
        response['Location'] = '/login/' 
        return response
    else:
        image = None
        if country_code == "World":
            google_news = GNews(language='en', max_results=10)
            world_news = google_news.get_top_news()
            summaries_list = []
            for article in world_news:
                link = article['url']
                stored_article = NewsArticle.objects.filter(link=link).first()
                if stored_article:
                    summaries_list.append({'title': stored_article.title, 'link': stored_article.link, 'summary': stored_article.summary,'image': stored_article.image})
                else:
                    title = article['title']
                    text = article["description"]
                    description = text.replace("View Full Coverage on Google News", "")
                    image = get_image(link)
                    new_article = NewsArticle(title=title, link=link, summary=description, image=image)
                    new_article.save()
                    summaries_list.append({'title': title, 'link': link, 'summary': description,'image': image})
            
            return JsonResponse(summaries_list, safe=False)
        else:
            google_news = GNews(language='en', max_results=10)
            topic_news = google_news.get_news_by_topic(f'{country_code}')
            summaries_list = []
            for article in topic_news:
                link = article['url']
                stored_article = NewsArticle.objects.filter(link=link).first()
                if stored_article:
                    summaries_list.append({'title': stored_article.title, 'link': stored_article.link, 'summary': stored_article.summary,'image': stored_article.image})
                else:
                    title = article['title']
                    text = article["description"]
                    description = text.replace("View Full Coverage on Google News", "")
                    image = get_image(link)
                    new_article = NewsArticle(title=title, link=link, summary=description, image=image)
                    new_article.save()
                    summaries_list.append({'title': title, 'link': link, 'summary': description,'image': image})     
            return JsonResponse(summaries_list, safe=False)        


@login_required
def search_news(request,query):
    if not request.user.is_authenticated:
        response = JsonResponse({'error': 'User not authenticated'})
        response.status_code = 401
        response['Location'] = '/login/'  
        return response
    else:
        google_news = GNews(language='en',max_results=10)
        India_news = google_news.get_news(query)
        summaries_list = []
        for article in India_news:
            link = article['url']
            stored_article = NewsArticle.objects.filter(link=link).first()
            if stored_article:
                summaries_list.append({'title': stored_article.title, 'link': stored_article.link, 'summary': stored_article.summary,'image': stored_article.image})
            else:
                title = article['title']
                text = article["description"]
                description = text.replace("View Full Coverage on Google News", "")
                image = get_image(link)
                new_article = NewsArticle(title=title, link=link, summary=description, image=image)
                new_article.save()
                summaries_list.append({'title': title, 'link': link, 'summary': description,'image': image})
        return JsonResponse(summaries_list, safe=False)       

 
  
def convert_text_to_speech(text, language):
    if not text:
        default_text = "No text found in article"
        tts = gTTS(text=default_text, lang=language, slow=False)
        tts.save(str(BASE_DIR) + "/NewsJunction/static/audio.mp3")
    else:
        try:
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save(str(BASE_DIR) + "/NewsJunction/static/audio.mp3")
        except AssertionError:
            return JsonResponse({'error': 'Failed to generate audio'})
  
def translate_text(text, dest_language):
    if not text:
        text="No text found in article"
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_language).text
    return translated_text

@login_required
def summary(request):
    if not request.user.is_authenticated:
        response = JsonResponse({'error': 'User not authenticated'})
        response.status_code = 401
        response['Location'] = '/login/' 
        return response
    else:

        result=None
        text=None
        if request.method == 'POST':
            data = request.body
            data = json.loads(data)
            selectedLanguage = data['selectedLanguage']
            link = data['link']
        try:
            summary_obj = Summary.objects.filter(link=link).first()
            if summary_obj:
                result = summary_obj.summaries
            else:
                response = requests.get(link)
                html_content = response.text

                article = Article(link, language='en')
                article.set_html(html_content)
                article.parse()
                text = article.text
                if text ==None:
                    text="no text found in article"
                result=get_summarization(text)
                summary_obj = Summary(title=link, link=link, summaries=result)
                summary_obj.save()
        except requests.exceptions.MissingSchema:
            result = "Invalid URL"
        except requests.exceptions.ConnectionError:
            result = "Unable to connect to the website"
        translated_text = translate_text(result,selectedLanguage )
        convert_text_to_speech(translated_text, selectedLanguage)
        audio_file = "/static/audio.mp3"
        data = {'summary': translated_text, 'audio_file': audio_file}
        return JsonResponse(data)



def get_summarization(text):
    summary_text = None
    API_URL = "https://api-inference.huggingface.co/models/google/pegasus-cnn_dailymail"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": text,
    })
    summary_text = output[0]["summary_text"]
    return summary_text


def get_image(url):
    try:
        response = requests.get(url)
        html_content = response.text
        article = Article(url, language='en')
        article.set_html(html_content)
        article.parse()
        image_url = article.top_image
        if image_url==None:
            return
        else:    
            return image_url
    except requests.exceptions.MissingSchema:
        return "Invalid URL"
    except requests.exceptions.ConnectionError:
        return "Unable to connect to the website"

def index(request):
    return render(request, 'NewsJunction/index.html')


@login_required
def ReadFull(request):
    if not request.user.is_authenticated:
        response = JsonResponse({'error': 'User not authenticated'})
        response.status_code = 401
        response['Location'] = '/login/'  # Set the "Location" header
        return response
    else:
        result=None
        if request.method == 'POST':
            data = request.body
            data = json.loads(data)
            selectedLanguage = data['selectedLanguage']
            link = data['link']
        try:
                response = requests.get(link)
                html_content = response.text
                article = Article(link, language='en')
                article.set_html(html_content)
                article.parse()
                result = article.text
        except requests.exceptions.MissingSchema:
            result = "Invalid URL"
        except requests.exceptions.ConnectionError:
            result = "Unable to connect to the website"
        translated_text = translate_text(result,selectedLanguage )
        convert_text_to_speech(translated_text, selectedLanguage)
        audio_file = "/static/audio.mp3"
        data = {'summary': translated_text, 'audio_file': audio_file}
        return JsonResponse(data)

def getSummary(request):
    translated_text=None
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        selectedLanguage = data['selectedLanguage']
        selectedFeature = data['selectedFeature']
        input = data['input']
        if input.startswith("https:"):
            try:
                response = requests.get(input)
                html_content = response.text
                article = Article(input, language='en')
                article.set_html(html_content)
                article.parse()
                results = article.text
            except requests.exceptions.MissingSchema:
                results = "Invalid URL"
            except requests.exceptions.ConnectionError:
                results = "Unable to connect to the website"
            if(selectedFeature=="Summarize"):
                result=get_summarization(results)  
                translated_text = translate_text(result,selectedLanguage ) 
                print(result)
                convert_text_to_speech(translated_text, selectedLanguage)
                audio_file = "/static/audio.mp3"
                data = {'summary': translated_text, 'audio_file': audio_file}
                return JsonResponse(data)
            else:
                result=results   
                translated_text = translate_text(result,selectedLanguage )
                convert_text_to_speech(translated_text, selectedLanguage)
                audio_file = "/static/audio.mp3"
                data = {'summary': "", 'audio_file': audio_file}
                return JsonResponse(data)

        else:
            if(selectedFeature=="Summarize"):
                result=get_summarization(input)
                translated_text=translate_text(result,selectedLanguage)
                convert_text_to_speech(translated_text, selectedLanguage)
                audio_file = "/static/audio.mp3"
                data = {'summary': translated_text, 'audio_file': audio_file}
                return JsonResponse(data)
            else:
                translated_text=translate_text(input,selectedLanguage)
                convert_text_to_speech(translated_text, selectedLanguage)
                audio_file = "/static/audio.mp3"
                data = {'summary': "", 'audio_file': audio_file}
                return JsonResponse(data)