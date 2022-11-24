pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Ashish1227/IMT2020073_Lab6.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x function.py"
                sh "./function.py"
            }
        }
        stage('Test Code 1') {
            steps {
                sh "chmod u+x test1.py"
                sh "./test1.py"
            }
        }
        stage('Test Code 2') {
            steps {
                sh "chmod u+x test2.py"
                sh "./test2.py"
            }
        }
        stage('Stage') {
            steps {
                echo 'This is staging environment'
            }
        }
        stage('Deploy') {
            steps {
                echo 'This is deployment stage'
            }
        }
        stage('Monitor') {
            steps {
                echo 'This is monitoring stage'
            }
        }
        
    } 
}
