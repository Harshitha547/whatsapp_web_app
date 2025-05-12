from flask import Flask, render_template, request
import pywhatkit

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    alert_type = 'info'
    if request.method == 'POST':
        phone = request.form['phone']
        text = request.form['text']
        hour = int(request.form['hour'])
        minute = int(request.form['minute'])

        try:
            pywhatkit.sendwhatmsg(phone, text, hour, minute)
            message = "✅ Message scheduled successfully!"
            alert_type = "success"
        except Exception as e:
            message = f"❌ Error: {e}"
            alert_type = "danger"

    return render_template('index.html', message=message, alert_type=alert_type)

if __name__ == '__main__':
    app.run(debug=True)
