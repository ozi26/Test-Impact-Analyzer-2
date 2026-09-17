// =============================================================================
// JENKINSFILE
// Pipeline definition for Test Impact Analyzer.
// Jenkins reads this file and executes each stage automatically.
// =============================================================================

pipeline {
    // Run on any available Jenkins agent
    agent any
    
    // Environment variables
    environment {
        PYTHONIOENCODING = 'UTF-8'  // Prevent encoding issues
    }
    
    stages {
        
        // Stage 1: Get the latest code
        stage('Checkout') {
            steps {
                // Pull the code from the Git repository configured in Jenkins
                checkout scm
            }
        }
        
        // Stage 2: Install Python dependencies
        stage('Install Dependencies') {
            steps {
                // Install packages from requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }
        
        // Stage 3: Run the Test Impact Analyzer
        stage('Analyze Changes') {
            steps {
                // Detect changes and identify affected tests
                // This creates analyzer_result.json
                sh 'python scripts/run_analyzer.py --range HEAD~1..HEAD'
            }
        }
        
        // Stage 4: Execute ONLY the selected tests
        stage('Run Affected Tests') {
            steps {
                // Read analyzer_result.json and run affected tests
                sh 'python run_selected_tests.py'
            }
        }
    }
    
    // Actions after pipeline completes
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