pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/YOURUSERNAME/car-devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t yourdockerhubusername/carworld .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push yourdockerhubusername/carworld'
            }
        }

        stage('Deploy Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}
