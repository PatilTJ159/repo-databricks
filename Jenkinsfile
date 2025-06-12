pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYSPARK_TEST_SCRIPT = 'tests\\test_myfirst_test_notebook.py'
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
                '''
            }
        }

        stage('Code Linting') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                flake8 .
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
                python myfirst_test_notebook.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the Spark job...'
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                spark-submit ^
                  --master local ^
                  --py-files dependencies.zip ^
                  src\\main_job.py
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
