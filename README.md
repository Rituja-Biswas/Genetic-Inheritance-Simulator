# Genetic-Inheritance-Simulator
The primary objective of this project is to use machine learning to simulate and analyze Mendel's pea plant experiments. It highlights how artificial intelligence can be applied to simulate and analyze classical biological concepts, showcasing interdisciplinary research.


# how to run:
  - open command prompt
  - make sure list of dependencies required to run the project is installed
  - run the application : python app.py
  - go to: http://127.0.0.1:5000

# To check for port conflicts on the system (specifically port 5000):
  - netstat -ano | findstr :5000
  - This will show you if any process is using port 5000. If a process is using it
  - Identify the Process Using the Port: If the port is in use, we can find the associated process by using the PID:
        - tasklist /fi "PID eq ##enter_the_PID## "
  - To stop the process, run:
      - taskkill /PID ##PID## /F


