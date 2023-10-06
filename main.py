from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global c
    global e
    global data
    if request.method == 'POST':
        data = request.form.get('area')
        c = word_count(data)
        e = l_count(data)
        if c or e or data is not None:
            # print(c)
            return render_template('index.html', c=c, e=e, data=data)
        # c=c, e=e, data=data
    return render_template('base.html')


#word count
def word_count(s):
    s = s.split()
    return len(s)

#letter count - without spaces
def l_count(s):
    s = s.split()
    q = "".join(s)
    return len(q)
    

if __name__ == "__main__":
    app.run(debug=True)