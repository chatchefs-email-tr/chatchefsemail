from flask import Flask, request, redirect
import logging

app = Flask(__name__)

@app.route('/logo1.png')
def track_open():
    user_email = request.args.get('email')
    logging.info(f"Email opened by: {user_email}")
    return app.send_static_file('mainlogo.png')  # Send a 1x1 pixel image

@app.route('/officialurl')
def track_click():
    user_email = request.args.get('email')
    redirect_url = request.args.get('redirectUrl')
    logging.info(f"Link clicked by: {user_email}")
    return redirect(redirect_url)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
