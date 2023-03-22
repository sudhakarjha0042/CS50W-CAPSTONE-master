CS50w Capstone Projecr:
--------------
-------------
Distinctiveness and Complexity
------------------------------
### Overview:
NewsJunction is a web application built with Python/Django on the back-end and JavaScript on the front-end, which provides users with a comprehensive news experience. Users can browse and read news articles from various categories such as technology, sports, business, entertainment, and more. The application also offers a powerful search functionality to help users find specific news articles.

### Justification:
NewsJunction meets all the requirements for the CS50W final project. It is a highly distinctive project that stands out from other projects in the course because it is not a social network or e-commerce site. Instead, it is a fully functional news app. The app's complexity is evident in the integration of multiple APIs to retrieve news articles and the use of JavaScript to enhance the user experience.

The app is mobile-responsive, making it easy for users to access the news on the go. The application is also highly customizable, allowing users to personalize their news experience by selecting categories they are interested in.

In addition to these features, NewsJunction also incorporates a text-to-speech functionality that allows users to listen to articles instead of reading them. This feature caters to users who prefer to listen to news while doing other tasks or have visual impairments. Users can select their preferred language, and the app will read the article in the chosen language. This feature adds to the uniqueness of the app and enhances the user experience by making it more accessible.

In addition to the text-to-speech functionality, NewsJunction also offers a summarization feature that allows users to get a quick summary of any article they choose. This feature is particularly useful for users who want to quickly get an overview of an article without having to read the entire thing in their preferred language.

NewsJunction is a powerful news app. It is more complex than other projects in the course and offers a unique user experience. The use of APIs and JavaScript on the front-end make this app stand out.

This news web app satisfies the distinctiveness and complexity requirements for the final project in CS50W. It is distinct from other projects in the course as it is not a social network or e-commerce site, but rather a news app. The app is more complex than other projects as it integrates multiple APIs to retrieve news articles, allowing users to browse and search through a large database of articles. The app also incorporates JavaScript on the front-end to enhance the user experiences.

# Features:
1.  User Registration and Login: The app allows users to register an account and login to access various functionalities. It also offers an option to login using their Google account, making the process much simpler.

2.  Browse and Search News Articles: The app provides users with access to news articles from different categories and sources. Users can browse articles or use the search functionality to find specific articles.

3.  Article Summarization: NewsJunction offers a summarization feature that provides a summary of news articles as per the chosen language. If no language is selected, it defaults to English.

4.  Text to Speech: The app also provides a text-to-speech feature that allows users to listen to the full article as per the selected language. This feature is handy for users who want to listen to news while doing other tasks.

5.  Mobile-Responsive: The app is fully mobile-responsive, enabling users to access the news on their mobile devices.

6.  News Categories: The app offers news articles in various categories, including business, entertainment, health, science, sports, technology, and general news.
----------------------------------------------------------------------------
Installation and Setup:
----------------------

To run this app, you will need to have Python 3 and Django installed on your machine.

Then, follow these steps:

1.  Clone the repository
2.  Navigate to the project directory: `cd CS50W_Final`
3.  Install the required Python packages: `pip install -r requirements.txt`
4.  Run the server: `python manage.py runserver`
5.  Access the app in your web browser at `http://localhost:8000`
-----------------------------------------------------------------------------
# Front End:
### File Contents:
1.  `cs50w`:

    -   This is the main directory where the project files are located.
    -   It contains two subdirectories and one file.
    -   The two subdirectories are `CS50W_Final` and `__pycache__`.
    -   The file is `requirements.txt`.
    -   The purpose of this directory is to serve as a top-level container for the project.
2.  `CS50W_Final`:

    -   This subdirectory contains the main Django project files for `CS50W_Final`.
    -   It contains four files and one subdirectory.
    -   The files are `db.sqlite3`, `manage.py`, `README.md`, and `requirements.txt`.
    -   The subdirectory is `NewsJunction`.
    -   The purpose of this subdirectory is to contain the main project files for the Django project `CS50W_Final`.
3.  `CS50W_Final\CS50W_Final`:

    -   This subdirectory is the inner `CS50W_Final` folder, which is the root folder of the Django project.
    -   It contains five files and one subdirectory.
    -   The files are `asgi.py`, `settings.py`, `urls.py`, `wsgi.py`, and `__init__.py`.
    -   The subdirectory is `__pycache__`.
    -   The purpose of this subdirectory is to contain the main files of the Django project.
4.  `cs50w\CS50W_Final\NewsJunction`:

    -   This subdirectory contains the main application files for `NewsJunction`.
    -   It contains eight files and three subdirectories.
    -   The files are `admin.py`, `apps.py`, `models.py`, `tests.py`, `views.py`, `__init__.py`, and `static`, and `templates`.
    -   The subdirectories are `migrations`, `static`, and `templates`.
    -   The purpose of this subdirectory is to contain the main files of the Django application `NewsJunction`.


### Working of homepage:
-   `{% load static %}`: This loads the static files for the website, including the CSS and JavaScript files.
-   `{% csrf_token %}`: This template tag generates a hidden input element with a CSRF token that will be used to validate the form data.
-   `{% if user.is_authenticated %}`: This checks if the user is already authenticated (i.e., logged in). If the user is authenticated, the page will display the content inside the `{% block body %}` tag.
-   `<nav class="navbar navbar-expand-lg navbar-dark bg-dark" style="border-bottom: 2px solid #fff;margin-bottom: 2px;">`: This creates a navigation bar that is styled with a dark background and white text.
-   `<a class="navbar-brand" href="/">`: This creates a link to the homepage of the website.
-   `<img src="/static/images/dark final logo.png" width="110px" height="20px" alt="News Junction" class="img-fluid">`: This displays the logo for the website, which is an image file located in the `static` folder.
-   `<ul class="navbar-nav me-auto mb-2 mb-lg-0 text-white">`: This creates a list of navigation links that will be displayed in the navigation bar.
-   `<li class="nav-item">`: This creates a list item for a navigation link.
-   `<a class="nav-link" href="#" onclick="fetchNews('World','news')">World News</a>`: This creates a hyperlink that will execute the `fetchNews()` function when clicked.
-   `<form class="d-flex" role="search">`: This creates a search form that will be displayed in the navigation bar.
-   `<input class="form-control me-2" id="searchInput" type="search" placeholder="Search" aria-label="Search">`: This creates an input field for the search form.
-   `<form action="{% url 'logout' %}?next=/" method="post">`: This creates a form for the logout button.
-   `<button class="btn btn-outline-light mx-2" type="submit" role="button" aria-pressed="true" class="btn btn btn-danger btn-lg btn-block">Logout</button>`: This creates a logout button that will be displayed in the navigation bar.

-   The JavaScript code is used to dynamically fetch news articles from an API based on the user's navigation and search input.
-   The `fetchNews` function is called when the user clicks on a navigation link or submits a search query. It takes in two parameters: `input`, which is the search query or category that the user is interested in, and `forwhat`, which indicates whether the search query is for news or search.
-   The function starts a timer to show a loading message to the user while the news articles are being fetched. If the articles take longer than 40 seconds to load, an error message is displayed instead.
-   The function then uses the `fetch` API to make an HTTP GET request to the News API, passing in the user's search query or category as a parameter.
-   The API response is then parsed as JSON and the relevant news articles are displayed on the page.
-   The `onclick` attribute on the navigation links and search button are set to call the `fetchNews` function with the relevant input parameters.
-   There are other JavaScript functions included on the page, such as `showToaster` which displays a success or error message to the user, and `logout` which logs the user out of their account.

Overall, the JavaScript code is responsible for fetching news articles from the News API in response to user actions, and updating the page dynamically to display the results. It also handles showing loading and error messages to the user as necessary.

Working of Login Page:
----------------------
The template is first loading some libraries, such as "socialaccount", "i18n", "account", and "socialaccount". These libraries are used to add functionality to the website such as authentication with social media accounts.

The code then creates an HTML document with a head and body section. In the head section, some metadata is defined such as the character encoding, the viewport, and the title of the page. In the body section, a container is created to hold the login form.

The login form is created using a Django form object, which is referred to as `form`. The `{{ form.as_p }}` statement will render the form as HTML, with each form field wrapped in a paragraph tag.

The form has an action attribute that is set to the URL for the login view. When the user submits the form, the data will be sent to the server using a POST request to the specified URL. The `{% csrf_token %}` template tag generates a security token that is required by Django to prevent cross-site request forgery attacks.

There is also a second form in the code that allows the user to sign in with their Google account. This form has an action attribute set to the URL for the Google authentication view. When the user clicks the "Sign in with Google" button, they will be redirected to the Google authentication page.

The code also includes some conditional statements that check if the user is authenticated or not. If the user is not authenticated, additional code could be added here to display a message or provide other options.

Overall, this code is using Django to create a login page for a website with a standard login form and the ability to authenticate with a Google account.


Working of Signup Page
----------------------
1.  `{% load %}` tags are used to load the required modules for the template to function. In this case, the `socialaccount`, `i18n`, and `account` modules are being loaded.
2.  The `<head>` section contains metadata and links to external stylesheets to be used in the document.
3.  The `<body>` section contains a form for user sign up.
4.  The `form` tag specifies that the method used to send the form data is `post`. This means that the data is submitted as an HTTP POST request to the URL specified in the `action` attribute of the form tag.
5.  `{% csrf_token %}` is a Django security feature that adds a hidden form field to the HTML form containing a token. This is to protect against CSRF (cross-site request forgery) attacks.
6.  `{{ form.as_p }}` is a Django template tag that renders the form fields as paragraphs.
7.  The `button` tag with `type="submit"` attribute is used to submit the form.
8.  There is a second form that allows the user to sign up with their Google account using the Google OAuth API. The `provider_login_url` is a Django Social Authentication tag that generates the URL for authenticating with the Google provider. The user can click the button to sign up using their Google account.
9.  The `if user.is_authenticated` condition is used to check if the user is not authenticated. If the user is not authenticated, they will see a message asking them to sign in.
10. The `text-muted` class sets the text color to light gray.
11. The `&copy;` character is used to display the copyright symbol.
-------------------
Back End:
--------
## views.py:
This is the views.py file of a Django web application that displays news articles from Google News using the `gnews` package.

1.  `news(request, country_code)`:

    This function is used to fetch the top news articles based on the country code or topic passed as a parameter. If the user is not authenticated, the function will return a response with an error message, otherwise, it will fetch news articles from Google News API and store them in the database or retrieve them if already stored.

    The function follows the below steps:

    -   Check if the user is authenticated or not, and return an error response if not authenticated.

    -   If the country code is "World", the function will fetch the top news articles from Google News API for the English language and return a JSON response containing a list of the 10 most recent articles with their title, link, summary, and image.

    -   If the country code is "India", the function will fetch the top news articles from Google News API for the English language and India as the country and return a JSON response containing a list of the 10 most recent articles with their title, link, summary, and image.

    -   If the country code is not "World",the function will fetch the top news articles for the specified topic and return a JSON response containing a list of the 10 most recent articles with their title, link, summary, and image.

2.  `search_news(request, query)`:

    This function is used to search for news articles containing the query passed as a parameter. If the user is not authenticated, the function will return a response with an error message, otherwise, it will fetch news articles from Google News API and store them in the database or retrieve them if already stored.

    The function follows the below steps:

    -   Check if the user is authenticated or not, and return an error response if not authenticated.

    -   Fetch the news articles containing the query passed as a parameter from Google News API for the English language and return a JSON response containing a list of the 10 most recent articles with their title, link, summary, and image.

    -   If the news article is not already stored in the database, then it will store it in the database for future retrieval. The function checks if the news article is already present in the database and fetches it if it exists.

In both functions, the `@login_required` decorator is used to ensure that only authenticated users can access the view. If a user is not authenticated, it returns an error message.

3.  `index` view: Renders the homepage of the NewsJunction website.

4.  `text_to_audio` view:

    -   Requires authentication
    -   Accepts POST requests with a JSON object containing a selectedLanguage and link
    -   Extracts the text content from the provided URL using the newspaper3k package and then summarizes the text using the Hugging Face Pegasus model.
    -   Translates the summary text into the selected language using the Google Translate API.
    -   Converts the translated text into speech using the gTTS package.
    -   Returns a JSON response containing the summary text and a link to the generated audio file.
5.  `get_summarization`: Accepts a text string as input and summarizes the text using the Hugging Face Pegasus model.

6.  `translate_text`: Accepts a text string and a destination language as input and translates the text into the specified language using the Google Translate API.

7.  `convert_text_to_speech`: Accepts a text string and a language as input, converts the text into speech using the gTTS package, and saves the resulting audio file to the NewsJunction/static directory.

8.  `get_image`: Accepts a URL as input, extracts the top image from the webpage using the newspaper3k package, and returns the URL of the extracted image.

9.  `ReadFull` view:

    -   Requires authentication
    -   Accepts POST requests with a JSON object containing a selectedLanguage and link
    -   Extracts the full text content from the provided URL using the newspaper3k package.
    -   Translates the text into the selected language using the Google Translate API.
    -   Converts the translated text into speech using the gTTS package.
    -   Returns a JSON response containing the full text and a link to the generated audio file.


The view uses the `NewsArticle` model to store news articles in the database. If an article with the same link already exists in the database, it uses the stored article instead of making a new API call.

The view uses the `gtts` and `googletrans` packages to generate a spoken summary and a translation of the summary for each article.
This news web app is built with a focus on simplicity and ease-of-use for the user.The app also includes error handling to gracefully handle API errors or other issues that may arise during use.


## models.py files:
Models in the app There are 2 models for the web application's database.

1.  Summary - Holds the summary information of news articles.

    -   title: A character field that holds the title of the news article.
    -   link: A URL field that holds the link of the news article.
    -   summaries: A text field that holds the summary of the news article.
    -   image_url: A URL field that holds the image of the news article.
    -   created_at: A DateTime field that automatically sets the creation time of the news article summary.
    -   updated_at: A DateTime field that automatically updates the time when the news article summary was last updated.
2.  NewsArticle - Holds the information of news articles.

    -   title: A character field that holds the title of the news article.
    -   link: A URL field that holds the link of the news article.
    -   summary: A text field that holds the summary of the news article.
    -   image: A URL field that holds the image of the news article.

These models are used to store the information of the news articles and their summaries for the web application.

known Bugs
-------------------
1.  It can be frustrating to have to enter two search queries at times, which could be improved for a smoother user experience.
2.  Occasionally, the response time may be slower than usual, causing delays in accessing information.
3.  Users have reported that fetching queries or news takes too long at times, leading to inconvenience. Improving the loading speed could enhance the user experience.

Contact Us:
-----------
If you have any questions or feedback about this news web app, please do not hesitate to contact me at my email: [jhas0042@gmail.com].By Sudhakar Jha