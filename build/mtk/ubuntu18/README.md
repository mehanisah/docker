docker login harbor.swscm.stg.sony-asia.com
docker build -t harbor.swscm.stg.sony-asia.com/build/mtk:1 . --build-arg USERNAME=scm --build-arg USERPASSWD=so****
