pipeline {
  agent {
    node {
      label 'POD_LABEL'
    }

  }
  stages {
    stage('Build Docker') {
      agent {
        node {
          label 'POD_LABEL'
        }

      }
      steps {
        sh 'docker build -t test .'
      }
    }

  }
}