pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Sharwaree2003/Ground_Station_Proj.git'
            }
        }

        stage('Backend Setup') {
            steps {
                sh '''
                cd backend
                source venv/bin/activate
                pip install -r requirements.txt || true
                '''
            }
        }

        stage('Frontend Build') {
            steps {
                sh '''
                cd frontend
                npm install
                npm run build
                '''
            }
        }

        stage('Restart Services') {
            steps {
                sh '''
                sudo systemctl restart groundstation-backend
                sudo systemctl restart groundstation-frontend
                '''
            }
        }
    }
}

