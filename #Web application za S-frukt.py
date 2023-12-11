from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for storing items
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form.get('item_name')
    items.append(item_name)
    return redirect(url_for('index'))

@app.route('/delete/<item_name>')
def delete_item(item_name):
    items.remove(item_name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host= "0.0.0.0",port = (), debug=True)