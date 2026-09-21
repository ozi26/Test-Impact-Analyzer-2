// =============================================================================
// JENKINSFILE
// Pipeline for Test Impact Analyzer.
// Uses a Python virtual environment to isolate project dependencies.
// =============================================================================

pipeline {
    agent any
    
    environment {
        PYTHONIOENCODING = 'UTF-8'
        PYTHONPATH = "${WORKSPACE}"
    }
    
    stages {
        
        // Stage 1: Get the latest code from GitHub
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        // Stage 2: Create virtual environment and install dependencies
        stage('Install Dependencies') {
            steps {
                // Create an isolated Python environment in a folder called 'venv'
                // This avoids the "externally-managed-environment" error
                sh 'python3 -m venv venv'
                
                // Install our project's dependencies into the virtual environment
                // We call the pip inside 'venv' explicitly using its full path
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        
        // Stage 3: Run the analyzer to detect affected tests
        stage('Analyze Changes') {
            steps {
                // Use the Python inside 'venv' to run the analyzer
                sh './venv/bin/python scripts/run_analyzer.py --range HEAD~1..HEAD'
            }
        }
        
        // Stage 4: Run only the affected tests
        stage('Run Affected Tests') {
            steps {
                // Use the Python inside 'venv' to run the selected tests
                sh './venv/bin/python run_selected_tests.py'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution finished'
        }
        success {
            echo 'All affected tests passed!'
        }
        failure {
            echo 'Some tests failed. Check the logs.'
        }
    }
}