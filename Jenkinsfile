/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh '''
                aws configure set aws_access_key_id ${{ secrets.AWS_ACCESS_KEY_ID }}
                aws configure set aws_secret_access_key ${{ secrets.AWS_SECRET_KEY_ID }}
                aws configure set default.region us-east-1
                aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 848215208608.dkr.ecr.us-east-1.amazonaws.com
                docker build -t flask_app .
                docker tag flask_app:latest 848215208608.dkr.ecr.us-east-1.amazonaws.com/flask_app:latest
                docker push 848215208608.dkr.ecr.us-east-1.amazonaws.com/flask_app:latest
                '''
            }
        }
    }
}
