pipeline {
    agent any
    
    environment {
        COMPOSE_PATH = '/home/ta/chatbot_helpdesk'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Start Services') {
            steps {
                script {
                    sh "cd ${COMPOSE_PATH} && docker-compose down"
                    sh "cd ${COMPOSE_PATH} && docker-compose pull"
                    sh "cd ${COMPOSE_PATH} && docker-compose up -d --build"
                }
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully and services have been deployed.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
