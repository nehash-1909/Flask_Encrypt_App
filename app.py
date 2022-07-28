from flask import Flask, render_template, request, flash
import rsa

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
	flash("Enter the string you want to encrypt..!!")
	return render_template("index.html")

@app.route("/encrypt", methods=['POST', 'GET'])
def encrypt_algo():
	publicKey, privateKey = rsa.newkeys(512)
 
	# this is the string that we will be encrypting
	message = str(request.form['name_input'])
 
	# rsa.encrypt method is used to encrypt
	# string with public key string should be
	# encode to byte string before encryption
	# with encode method
	encMessage = rsa.encrypt(message.encode(),
                         publicKey)
	flash("Encrypt message " +  str(encMessage))
	return render_template("index.html")
