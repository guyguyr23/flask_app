/* Requires the Docker Pipeline plugin */
pipeline {
    agent {         docker {
            image 'maven:3.5.0'
            args '--user=root'
        } }
    
    stages {
        stage('build') {
            steps {
                sh 'docker build -t my_image .'
            }
        }
    }
}
