pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Start Services') {
            steps {
                script {
                    // Use the workspace directory for Docker Compose commands
                    sh "docker compose -f ${WORKSPACE}/docker-compose.yml down"
                    sh "docker compose -f ${WORKSPACE}/docker-compose.yml up -d --build"
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
