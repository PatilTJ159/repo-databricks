pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        SPARK_HOME = 'C:\\Users\\DELL\\Downloads\\spark-4.0.0-bin-hadoop3'
        PYSPARK_PYTHON = "${WORKSPACE}\\venv\\Scripts\\python.exe"
        PYSPARK_TEST_SCRIPT = 'tests\\test_myfirsttestnotebook.py'
    }

    stages {

        stage('Clone Repo') {
            steps {
                echo 'Cloning the GitHub repository...'
                checkout scm
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
                call %VENV_DIR%\\Scripts\\activate
                pytest %PYSPARK_TEST_SCRIPT%
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
                set SPARK_HOME=C:\\Users\\DELL\\Downloads\\spark-4.0.0-bin-hadoop3
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
