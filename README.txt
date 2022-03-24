To run project on localhost
install requirements from requirements.txt
run command "python manage.py runserver" from project directory

project on heroku: https://thawing-castle-18399.herokuapp.com/
postman doc: https://documenter.getpostman.com/view/20179413/UVsTqMsn


Project contains two apps
First app "articles" generates simple page with articles and pages with comments for those articles.
"articles" also contains command to reset post upvotes count.
path to command: \articles\management\commands\clearvotes.py
command can be run by: "python manage.py clearvotes" from project directory


API are contained in app "api".
API are based on included in drf lib "generics"
Description of classes that inherits generics is in file "api.py"
Description of classes that inherits serializers is in file "serializers.py"
Models are imported from "articles" application



API to manage articles


method: GET
url: <HOST>/api
fields = ['id', 'title', 'link', 'author_name', 'date']
returns list of articles


method: POST
url: <HOST>/api/create
keys [title', 'link', 'author_name']
all keys are required


method: UPDATE
url: <HOST>/api/<article_id>
keys = ['title', 'link', 'author_name']


method: DELETE
url: <HOST>/api/<article_id>/delete


method: POST
url: <HOST>/api/<article_id>/upvote
upvotes chosen article


API to manage comments
comments can be managed only through connected article


method: GET
url: <HOST>/api/<article_id>/comments
fields = ['id', 'text', 'author_name', 'date']
returns list of comments for chosen article


method: POST
url: <HOST>/api/<article_id>/comments/create
keys ['text', 'author_name']
all keys are required


method: UPDATE
url: <HOST>/api/<article_id>/comments/<comment_id>/update
keys = ['title', 'link', 'author_name']
requires id in url both for article and comment


method: DELETE
url: <HOST>/api/<article_id>/comments/<comment_id>/delete
requires id in url both for article and comment




