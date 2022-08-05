import boto3
from flask import Flask, render_template
from flask import request
app = Flask(__name__)
def listbucket():
    s3 = boto3.resource('s3')

    my_bucket = s3.Bucket('tiger-mle-pg')

    l=[]

    for my_bucket_object in my_bucket.objects.filter(Prefix="home/sravan.kumar/"):
        if my_bucket_object.key !="home/sravan.kumar/":
            l.append(my_bucket_object.key)
    return l


@app.route('/')
def home():
    objectlist=listbucket()
    return render_template('home.html', bucketlist=objectlist)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085)

