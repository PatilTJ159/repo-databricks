pipeline {
    agent any

    environment {
        PYSPARK_PYTHON = "python3"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/PatilTJ159/repo-databricks.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'flake8 src/'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Run PySpark Job') {
            steps {
                sh 'spark-submit myfirst-test-notebook.py'
            }
        }

        
    }

    post {
        always {
            junit 'tests/test-results.xml'  // If using JUnit style reporting
        }
        failure {
            mail to: 'teju.patil1415@gmail.com',
                 subject: 'Build Failed',
                 body: 'Please check Jenkins job logs.'
        }
    }
}
