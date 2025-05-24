pipeline {
    agent any
    environment {
        // Thay bằng thông tin server triển khai
        DEPLOY_SERVER = 'your-server-ip'
        DEPLOY_USER = 'your-username'
        DEPLOY_PATH = '/path/to/deploy'
        // Nếu dùng AWS, thêm AWS credentials
        AWS_CREDENTIALS = credentials('aws-credentials-id')
    }
    stages {
        stage('Checkout') {
            steps {
                // Lấy mã nguồn từ GitHub
                git branch: 'main', url: 'https://github.com/mjjyv/flask_project.git'
            }
        }
        stage('Build') {
            steps {
                // Cài đặt dependencies
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Chạy kiểm thử
                sh 'source venv/bin/activate && pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                // Triển khai lên server qua SSH
                sshagent(credentials: ['ssh-credentials-id']) {
                    sh """
                    scp -r . ${DEPLOY_USER}@${DEPLOY_SERVER}:${DEPLOY_PATH}
                    ssh ${DEPLOY_USER}@${DEPLOY_SERVER} '
                        cd ${DEPLOY_PATH} &&
                        source venv/bin/activate &&
                        pip install -r requirements.txt &&
                        nohup python3 app.py &'
                    """
                }
                // Nếu dùng AWS Elastic Beanstalk, thay bằng:
                // sh 'eb deploy'
            }
        }
    }
    post {
        always {
            // Gửi thông báo qua email hoặc Slack (tùy chọn)
            echo 'Pipeline completed.'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}