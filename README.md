# Zeotap_Assignment
In this project, I've used Python and Django to create an awesome solution that tackles the Zeotap challenge. 💻✨
Both applications are designed to solve real-world problems with efficient and scalable approaches. Dive into each one for a detailed walkthrough! 👇

[Go to Application 1: Rule Engine with AST](#🛠️-application-1-rule-engine-with-ast)

[Go to Application 2: Real-Time Data Processing System for Weather Monitoring](#🌦️-application-2-real-time-data-processing-system-for-weather-monitoring-with-rollups-and-aggregates)

## 🛠️ Application 1: Rule Engine with AST

Welcome to **Application 1: Rule Engine with AST**! This project allows users to dynamically create, evaluate, and manage rules using a simple UI built with Django. Follow the steps below to set up and run the application successfully.

## 🚀 Getting Started

### 1️⃣ Clone and Extract the Project
- Download the folder from the GitHub repository.
- Extract the folder into an empty directory of your choice.

### 2️⃣ Set Up Your Virtual Environment
To avoid dependency issues, it is recommended to create a virtual environment. Here's how:
1. Open the extracted folder in **VS Code**.
2. In the terminal, create the virtual environment:
   ```bash
   python -m venv env
   ```
3. Activate the virtual environment:
   ```bash
   .\env\Scripts\activate.ps1
   ```

### 3️⃣ Install Dependencies
Once inside the virtual environment, install Django:
```bash
pip install django
```

### 4️⃣ Navigate to the Project Directory
Change to the `myproject` directory where the `manage.py` file is located:
```bash
cd myproject
```

### 5️⃣ Migrate the Database
Apply database migrations using the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser (Optional)
You can create a superuser to manage the database via Django's admin panel: 
```bash
python manage.py createsuperuser
```
- Follow the prompts to add a username and password of your choice. To access the admin panel you can visit to http://127.0.0.1:8000/admin/ url and see database.

### 7️⃣ Start the Server
Finally, start the Django development server:
```bash
python manage.py runserver
```

## 🌐 Running the Application

1. Open the browser and visit the URL displayed in your terminal (typically `http://127.0.0.1:8000/`).
2. On the homepage, you'll be able to create rules (e.g., ` age > 30, "department": "Sales" ). After submitting a rule, you’ll see a success message with the rule ID.   
   
   ![Rule Created](https://github.com/user-attachments/assets/e5907e0d-194a-444a-9573-e7402a3c9555)

3. To view all rules, click on the link below the "Evaluate Rule" button. **view all rules**

   ![All Rules](https://github.com/user-attachments/assets/ce089089-565a-4cc0-8ece-20f810454cc7)

4. If you attempt to add a duplicate rule, an error will be displayed:

   ![Error](https://github.com/user-attachments/assets/3ecfd1ac-ad33-431e-8df6-494b8671ad69)

## 🧪 Testing the Rules

### ✅ Test Case - True Condition
Using the dummy JSON data (e.g., `{ "age": 35, "department": "Sales" }`), the rule will return `True` if the age is greater than the rule's age and the department matches.

![True Condition](https://github.com/user-attachments/assets/94100324-d192-42dc-b74f-60844112acd5)

### ❌ Test Case - False Condition
For a false case, if the age is smaller than the rule's age  (e.g., `{ "age": 15, "department": "Sales" }`), it will return `False`.

![False Condition](https://github.com/user-attachments/assets/d2bdb37b-902b-445a-87a7-7757f1af2a1e)

---

By following these steps, you can successfully create multiple rules and test them under different conditions.

## 📽️ Troubleshooting
If you face any issues during the setup, please refer to the project video tutorial for further assistance.

---

## 🌦️ Application 2: Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

Welcome to **Application 2: Real-Time Data Processing System for Weather Monitoring**! This project fetches real-time weather data, processes it, and provides rollups and aggregates for efficient monitoring. Follow the steps below to set up and run the project.

## 🚀 Getting Started

### 1️⃣ Clone and Extract the Project
- Download the folder from the GitHub repository.
- Extract the folder into an empty directory of your choice.

### 2️⃣ Set Up Your Virtual Environment
To avoid dependency issues, it is recommended to create a virtual environment. Here's how:
1. Open the extracted folder in **VS Code**.
2. In the terminal, create the virtual environment:
   ```bash
   python -m venv env
   ```
3. Activate the virtual environment:
   ```bash
   .\env\Scripts\activate.ps1
   ```

### 3️⃣ Install Dependencies
Once inside the virtual environment, install Django:
```bash
pip install django
```

### 4️⃣ Navigate to the Project Directory
Change to the `weather_monitor` directory where the `manage.py` file is located:
```bash
cd weather_monitor
```

### 5️⃣ Migrate the Database
Apply database migrations using the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser (Optional)
You can create a superuser to manage the system via Django's admin panel:
```bash
python manage.py createsuperuser
```
- Follow the prompts to add a username and password of your choice.

## 🌐 Real-Time Weather Monitoring

- The system retrieves real-time temperature data from **OpenWeatherAPI** every five minutes. To obtain the temperature of any metro city, simply click the corresponding city button, and the weather report will be displayed automatically.

![1](https://github.com/user-attachments/assets/69d2a8c6-8c6b-4451-a405-633d84c15658)

-The summary data is updated dynamically each time the page is refreshed. By clicking the View All Summary button, you can view a summary of the temperatures for the various cities displayed below.

![2](https://github.com/user-attachments/assets/346834a9-9e89-455c-9f0b-65f4e1004462)

---
- By clicking on the **Alerts** button we can know the Temperature is execced or not.

![alerts](https://github.com/user-attachments/assets/f2c073a9-1c58-4a0b-a4f6-1f6417608d40)

By following these steps, you can successfully set up and run the weather monitoring system with real-time data and efficient processing. 

## 📽️ Troubleshooting
If you face any issues during the setup, please refer to the project video tutorial for further assistance.

---

Feel free to enhance the project and explore its capabilities! 😊
