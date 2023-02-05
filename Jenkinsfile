/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    environment {
        AWS_ACCESS_KEY_ID = credentials("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY = credentials("AWS_SECRET_KEY_ID")
        devops_key=credentials("devops.pem")
    }
    stages {
        stage('build') {
            steps {
                sh '''
                aws configure set aws_access_key_id ${AWS_ACCESS_KEY_ID}
                aws configure set aws_secret_access_key ${AWS_SECRET_ACCESS_KEY}
                aws configure set default.region us-east-1
                aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 848215208608.dkr.ecr.us-east-1.amazonaws.com
                docker build -t flask_app .
                docker tag flask_app:latest 848215208608.dkr.ecr.us-east-1.amazonaws.com/flask_app:latest
                docker push 848215208608.dkr.ecr.us-east-1.amazonaws.com/flask_app:latest
                '''
            }
        }
        def remote:
            remote.name = 'ip-10-0-0-36'
            remote.host = '18.233.62.82'
            remote.user = 'ubuntu'
            remote.allowAnyHosts = true
            remote.identityFile = ${devops_key}
        stage('Remote SSH') {
          sshCommand remote: remote, command: "ls -lrt"
          sshCommand remote: remote, command: "for i in {1..5}; do echo -n \"Loop \$i \"; date ; sleep 1; done"
        }
    }
}
