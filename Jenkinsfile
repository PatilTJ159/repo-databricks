pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYSPARK_TEST_SCRIPT = 'tests/test_myfirst-test-notebook.py'
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
                sh '''
                python3 -m venv $VENV_DIR
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Code Linting') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                flake8 src/
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                pytest $PYSPARK_TEST_SCRIPT
                '''
            }
        }

        stage('Build Spark Job') {
            steps {
                echo 'Validating PySpark job...'
                sh '''
                source $VENV_DIR/bin/activate
                python src/main_job.py --dry-run
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the Spark job...'
                // Example: copy to HDFS, submit to cluster, etc.
                sh '''
                spark-submit \
                  --master yarn \
                  --deploy-mode cluster \
                  --py-files dependencies.zip \
                  src/main_job.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf $VENV_DIR'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
