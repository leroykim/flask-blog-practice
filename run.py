# Refer the page below for ci command
# https://pythonhosted.org/Flask-CI/
# > set FLASK_APP=hello
# > flask run
# Auto reload
# > set FLASK_DEBUG=1
from flaskblog import app  # it will import __init__.py file from the package

if __name__ == '__main__':
    app.run(debug=True)

'''
> python
>>> from flaskblog import db
>>> db.create_all()
'''
'''
>>> from flaskblog import db
>>> db.create_all()
>>> from flaskblog import User, Post
>>> user_1 = User(username='Leroy', email='L@demo.com', password='password')
>>> db.session.add(user_1)
>>> user_2 = User(username='JaneDoe', email='jd@demo.com', password='password')
>>> db.session.add(user_2)
>>> db.session.commit()
>>> User.query.all()
[User('Leroy', 'L@demo.com), 'default.jpg, User('JaneDoe', 'jd@demo.com), 'default.jpg]
>>> User.query.first()
User('Leroy', 'L@demo.com), 'default.jpg
>>> User.query.filter_by(username='Leroy').all()
[User('Leroy', 'L@demo.com), 'default.jpg]
>>> user = User.query.filter_by(username='Leroy').first()
>>> user.id
1
>>> user = User.query.get(1)
>>> user
User('Leroy', 'L@demo.com), 'default.jpg
>>> user.posts
[]
'''
'''
>>> post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
>>> post_2 = Post(title='Blog 2', content='Second Post Content!', user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.add(post_2)
>>> db.session.commit()
>>> user.posts
[Post('Blog 1', '2020-03-17 17:19:27.983161), Post('Blog 2', '2020-03-17 17:19:27.997123)]
>>> for post in user.posts:
...     print(post.title)
...
Blog 1
Blog 2
>>> post = Post.query.first()
>>>
>>> post
Post('Blog 1', '2020-03-17 17:19:27.983161)
>>> post.user_id
1
>>> post.author
User('Leroy', 'L@demo.com), 'default.jpg
'''
'''
>>> db.drop_all()
>>> db.create_all()
>>> User.query.all()
[]
>>> Post.query.all()
[]
'''
