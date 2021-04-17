# Frontend for EduARd

To run pls use docker (might need sudo privilledes)
```
cd frontend
sudo docker build -t example:dev .
docker run -v ${PWD}:/app -v /app/node_modules -p 80:4200 --rm example:dev
```
