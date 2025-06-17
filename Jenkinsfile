pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        SPARK_HOME = 'C:\\Users\\DELL\\Downloads\\spark-3.4.4-bin-hadoop3\\spark-3.4.4-bin-hadoop3'
        JAVA_HOME = 'C:\\Program Files\\Java\\jdk-17'
        PYSPARK_PYTHON = "${WORKSPACE}\\venv\\Scripts\\python.exe"
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
                bat '''
                "C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m venv %VENV_DIR%
                call %VENV_DIR%\\Scripts\\activate
                pip install --upgrade pip
                if exist requirements.txt (
                    pip install -r requirements.txt
                ) else (
                    echo requirements.txt not found
                    exit /b 1
                )
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
                call %VENV_DIR%\\Scripts\\activate
                set SPARK_HOME=%SPARK_HOME%
                set PYSPARK_PYTHON=%cd%\\venv\\Scripts\\python.exe
                set PATH=%SPARK_HOME%\\bin;%PATH%
                pytest test/tests/
                '''
            }
        }

        stage('Build Spark Job') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                python notebooktptest.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the Spark job...'
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                set SPARK_HOME=%SPARK_HOME%
                set PATH=%SPARK_HOME%\\bin;%PATH%
                set PYSPARK_PYTHON=%cd%\\venv\\Scripts\\python.exe
                %SPARK_HOME%\\bin\\spark-submit --master local notebooktptest.py
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
