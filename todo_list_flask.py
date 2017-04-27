'''
Created on Apr 10, 2017
Copyright (c) 2016-2017 Teodoro Montanaro

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
@author: tmontanaro
'''


from flask import Flask, url_for, render_template, request, redirect
import db_interaction
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    # if no address is given, redirect to the index page
    return redirect(url_for('index'))

@app.route('/index.html')
def index():
    #get the ordered list from the database
    tasks_list = db_interaction.get_sorted_tasks_list()
    return render_template('index.html', tasks_list=tasks_list)


@app.route('/insert_task.html', methods=['POST'])
def insert_task():
    # check for parameter received by POST method
    if ('description' in request.form and request.form['description']!=''):
        #get description (the task)
        description = request.form['description']
        #insert the new task in the database
        db_interaction.db_insert_task(description)

    # redirect to the home page
    return redirect(url_for('index'))

@app.route('/delete_task.html', methods=['GET'])
def delete_task():

    # check for parameter received by GET method
    if 'id_task' in request.args:
        #get the id of the task we want to remove
        id_task = request.args.get('id_task')
        # remove the item from the db
        db_interaction.db_remove_task_by_id(id_task)

    # redirect to the home page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
