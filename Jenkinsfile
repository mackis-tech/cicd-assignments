pipeline {
    agent any

    environment {
        VENV_DIR = "/mnt/g/tech/ubuntu-ansible/myansible"
        VENV_NEW = "/mnt/g/tech/ubuntu-ansible/"
        VENV_NEW_NAME = "myansible"
        VENV_DIR_NEW = "${VENV_NEW}${VENV_NEW_NAME}"
        DEPLOY_DIR = "/mnt/g/tech/git-projects/deploy-env/fastapi"
    }

    stages {
        stage('Checkout') {
            steps {
                cd $DEPLOY_DIR
                pwd
                echo "🔄 Checking out the latest code..."
                git credentialsId 'github-token', url: 'https://github.com/your-username/fastapi-demo.git'
            }
        }

        stage('Set-up Python Environment') {
            steps {
                sh '''
                if [ -d $VENV_DIR ]; then
                    echo "✅ Virtual environment already exists. Skipping setup."
                else
                    echo "🔧 Creating virtual environment..."
                    cd $VENV_NEW
                    python3 -m venv $VENV_NEW_NAME
                    echo "✅ Virtual environment created."
                    source $VENV_DIR_NEW/bin/activate
                    echo "🔧 Installing dependencies..."
                    pip install --upgrade pip
                    pip install -r requirements.txt
                fi
        '''
            }
        }

        /*stage('Run Tests') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    pytest
                '''
            }
        }*/
        stage('Stop Previous Uvicorn') {
            steps {
                sh '''
                    pkill -f "uvicorn main:app" || echo "No existing uvicorn process found."
                '''
            }
        }

        stage('Start FastAPI App') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    nohup uvicorn web-app:app --host 0.0.0.0 --port 8000 &
                '''
            }
        }
        stage('Health Check') {
            steps {
                sh '''
                    sleep 3
                    curl --fail http://localhost:8000 || (echo "App did not start!" && exit 1)
                '''
            }
        }
    }
}