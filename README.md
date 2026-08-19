1) The project consists of two sections: backend and frontend

2) The backend is built on Python 3.1.1 and PySpark 3.4.4
   a.input_data contains u.data and u.item from original dataset
   b.output_data is for movie_ranking_list.csv, the top 100 movies ranking
   c.tests folder contains unit-test .py files
    
3) The frontend is built with React Framework

4) The whole project is containerized with Docker, the version used here is 29.6.2

5) Steps to run the project:
   
   a.install Docker first and start Docker engine;
   
   b.then copy u.data and u.item from original dataset into backend/src/intput_data
   
   b.open a Terminal window, go to the directory of the project, 
     for example, "D:\workspace\eclipse-workspace\data_engineer_assignment"
     
   c.execute Bash "docker compose run --rm spark-backend"
   
   d.then run Bash "docker compose up --build frontend"
   
   e. Now we can open link "http://localhost:8080" in browser to check the movie web view.
      and the top 100 movies ranking csv file is in backend/output
 
   
Note: we need to run backend section first to get the movie data, then frontend.



   