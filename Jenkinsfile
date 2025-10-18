pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/JBRECCSE/helloci.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover tests'
            }
        }

        stage('Deploy') {
            steps {
                bat 'deploy.bat'
            }
        }
    }
}
