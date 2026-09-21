// =============================================================================
// JENKINSFILE
// Pipeline for Test Impact Analyzer.
// Uses a Python virtual environment and explicit workspace paths.
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
                // Show what files are present - useful for debugging
                sh 'ls -la'
            }
        }
        
        // Stage 2: Create virtual environment and install dependencies
        stage('Install Dependencies') {
            steps {
                // Create the virtual environment
                sh 'python3 -m venv venv'
                
                // Install dependencies using the requirements.txt at the workspace root
                // We use ${WORKSPACE} to make the path explicit
                sh "${WORKSPACE}/venv/bin/pip install -r ${WORKSPACE}/requirements.txt"
            }
        }
        
        // Stage 3: Run the analyzer
        stage('Analyze Changes') {
            steps {
                // Show the analyzer is being called from the right folder
                sh 'pwd'
                sh 'ls -la scripts/'
                
                // Run the analyzer using the venv Python
                sh "${WORKSPACE}/venv/bin/python ${WORKSPACE}/scripts/run_analyzer.py --range HEAD~1..HEAD"
            }
        }
        
        // Stage 4: Run only the affected tests
        stage('Run Affected Tests') {
            steps {
                // Confirm the result file exists
                sh 'ls -la analyzer_result.json || echo "No result file yet"'
                
                // Run the selected tests
                sh "${WORKSPACE}/venv/bin/python ${WORKSPACE}/run_selected_tests.py"
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