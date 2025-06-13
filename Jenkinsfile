pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        SPARK_HOME = 'C:\\Users\\DELL\\Downloads\\spark-3.4.4-bin-hadoop3\\spark-3.4.4-bin-hadoop3'
        PYSPARK_PYTHON = "${WORKSPACE}\\venv\\Scripts\\python.exe"
        PYSPARK_TEST_SCRIPT = 'tests\\test_myfirsttestnotebook.py'
        JAVA_HOME = 'C:\\Program Files\\Java\\jdk-17' 
        PATH = "${env.PATH};${env.SPARK_HOME}\\bin;${env.JAVA_HOME}\\bin"
    }

    stages {

        stage('Clone Repo') {
            steps {
                echo 'Cloning the GitHub repository...'
                checkout scm
            }
        }

    stage('Setup Virtual Environment') {
        steps {
            echo 'Creating virtual environment...'
            bat 'python -m venv venv'
            bat 'call venv\\Scripts\\activate && pip install --upgrade pip'
            bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
            bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m venv venv'
            }
    }
        
        stage('Setup Python Env') {
            steps {
                bat '''
                python -m venv %VENV_DIR%
                call %VENV_DIR%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install flake8 pytest
                '''
            }
        }

        stage('Code Linting') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                flake8 . --config=.flake8
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                set SPARK_HOME=C:\\Users\\DELL\\Downloads\\spark-3.4.4-bin-hadoop3\\spark-3.4.4-bin-hadoop3
                set PYSPARK_PYTHON=venv\\Scripts\\python.exe
                set PATH=%SPARK_HOME%\\bin;%PATH%
                pytest tests/
                '''
            }
        }

        stage('Build Spark Job') {
            steps {
                echo 'Validating PySpark job...'
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                python myfirsttestnotebook.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the Spark job...'
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                set SPARK_HOME=C:\\Users\\DELL\\Downloads\\spark-3.4.4-bin-hadoop3\\spark-3.4.4-bin-hadoop3
                set PATH=%SPARK_HOME%\\bin;%PATH%
                set PYSPARK_PYTHON=%cd%\\venv\\Scripts\\python.exe
                %SPARK_HOME%\\bin\\spark-submit --master local myfirsttestnotebook.py
        
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat 'rmdir /S /Q %VENV_DIR%'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
