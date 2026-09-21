// =============================================================================
// JENKINSFILE
// Pipeline for Test Impact Analyzer.
// Updated to use python3 and pip3 (required on Linux systems).
// =============================================================================

pipeline {
    agent any
    
    environment {
        PYTHONIOENCODING = 'UTF-8'
    }
    
    stages {
        
        // Stage 1: Get the latest code from GitHub
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        // Stage 2: Install Python dependencies
        stage('Install Dependencies') {
            steps {
                // Use pip3 (not pip) on Linux
                sh 'pip3 install -r requirements.txt'
            }
        }
        
        // Stage 3: Run the analyzer to detect affected tests
        stage('Analyze Changes') {
            steps {
                // Use python3 (not python) on Linux
                // For the first build, compare HEAD with the previous commit
                // If there's no previous commit, this will show no changes
                sh 'python3 scripts/run_analyzer.py --range HEAD~1..HEAD'
            }
        }
        
        // Stage 4: Run only the affected tests
        stage('Run Affected Tests') {
            steps {
                sh 'python3 run_selected_tests.py'
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