pipeline {
    agent any

    environment {
        PYTHON_CMD = 'py' // Use Python launcher on Windows
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/JBRECCSE/helloci.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Upgrade pip
                bat "${env.PYTHON_CMD} -m pip install --upgrade pip"
                // Install dependencies if any
                bat "${env.PYTHON_CMD} -m pip install -r requirements.txt"
            }
        }

        stage('Test') {
            steps {
                bat "${env.PYTHON_CMD} -m unittest discover tests"
            }
        }

        stage('Deploy') {
            steps {
                bat 'deploy.bat'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'Build and deploy succeeded!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
