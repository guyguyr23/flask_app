/* Requires the Docker Pipeline plugin */
pipeline {
    agent {         docker {
            image 'ubuntu:latest'
            args '--user=root'
        } }
    
    stages {
        stage('build') {
            steps {
                sh 'export FLASK_APP=app'
                sh 'export FLASK_ENV=development'
            }
        }
    }
}
