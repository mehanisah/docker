docker build -t harbor.swscm.stg.sony-asia.com/app/flask-sample-app:1.0 .
docker run -d -p 5000:5000 docker build harbor.swscm.stg.sony-asia.com/app/flask-sample-app:1.0 

