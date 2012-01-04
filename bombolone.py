# -*- coding: utf-8 -*-
"""
    bombolone.py
    ~~~~~~
    
    :copyright: (c) 2012 by Leonardo Zizzamia
    :license: BSD (See LICENSE for details)
"""
# Imports outside opentaste
from __future__ import with_statement
import re
from flask import request, session, g, redirect, url_for, abort, render_template
from jinja2 import contextfunction 

# Imports inside bombolone
from admin import (login_page, logout_page, admin_page, profile_page, pages_page, 
                    pages_content_page, languages_page)
from before import core_before_request, core_inject_user
from page import home_page, page_two_base, page_three_base, page_four_base, page_five_base
from shared import app, PORT

                  
@app.before_request
def before_request():
    return core_before_request()
    
@app.context_processor
def inject_user():
    return core_inject_user()

@app.route('/', methods=['POST', 'GET'])
def home():
    return home_page()
    
# ========================================================================	
# Pages zone

@app.route('/page_two/')
def page_two():
    return page_two_base()
    
@app.route('/page_three/')
def page_three():
    return page_three_base()
    
@app.route('/page_four/')
def page_four():
    return page_four_base()
    
@app.route('/page_five/')
def page_five():
    return page_five_base()
    
# ========================================================================	
# Admin zone
    
@app.route('/login/', methods=['POST', 'GET'])
def login():
    return login_page()
    
@app.route('/logout/')
def logout():
    return logout_page()
    
@app.route('/admin/')
def admin():
    return admin_page()
    
@app.route('/admin/profile/', methods=['POST', 'GET'])
def profile():
    return profile_page()
	
@app.route('/admin/pages/')
def pages():
    return pages_page()	
    
@app.route('/admin/pages/<_id>/', methods=['POST', 'GET'])
def pages_content(_id):
    return pages_content_page(_id)

@app.route('/admin/languages/')
def languages():
    return languages_page()
	
# ========================================================================	
# Error zone

@app.errorhandler(400)
def bad_request(error):
    """
    Raise if the browser sends something to the application the 
    application or server cannot handle.
    """
    return 'Raise if the browser sends something to the application the application or server cannot handle.', 400

@app.errorhandler(401)
def unauthorized(error):
    """Raise if the user is not authorized. Also used if you want 
    to use HTTP basic auth."""
    return 'Raise if the user is not authorized. Also used if you want to use HTTP basic auth.', 401

@app.errorhandler(404)
def not_found(error):
    """Raise if a resource does not exist and never existed."""
    return 'Raise if a resource does not exist and never existed.', 404
    
@app.errorhandler(408)
def request_timeout(error):
    """Raise to signalize a timeout."""
    return 'Raise to signalize a timeout.', 408
    
@app.errorhandler(413)
def request_too_large(error):
    """Like 413 but for too long URLs."""
    return 'Like 413 but for too long URLs.', 413
    
    
@app.errorhandler(500)
def bad_request(error):
    """
    Raise if the browser sends something to the application the 
    application or server cannot handle.
    """
    return 'Raise if the browser sends something to the application the application or server cannot handle.', 500
     
     
     
# ========================================================================	
# Jinja zone   
            
def sorted_thing(context, key):
	return sorted(key)
		
def int_thing(context, key):
	return int(key)

def str_thing(context, key):
	return str(key)

def unicode_thing(context, key):
	return unicode(key)
	
def type_thing(context, key):
	return type(key)
	
def len_thing(context, key):
	return len(key)
	
def enumerate_thing(context, key):	
	return enumerate(key)
	

# add some functions to jinja
app.jinja_env.globals['sorted'] = contextfunction(sorted_thing)  
app.jinja_env.globals['int'] = contextfunction(int_thing)   
app.jinja_env.globals['str'] = contextfunction(str_thing) 
app.jinja_env.globals['unicode'] = contextfunction(unicode_thing) 
app.jinja_env.globals['type'] = contextfunction(type_thing) 
app.jinja_env.globals['len'] = contextfunction(len_thing) 
app.jinja_env.globals['enumerate'] = contextfunction(enumerate_thing) 

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=PORT)