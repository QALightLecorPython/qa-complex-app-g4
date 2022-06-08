#!groovy
//
// QA Complex App tests Runner

// Pipeline
pipeline {
  agent {
    label 'master'
  }
  options {
    timeout(time: 1, unit: 'HOURS')
    timestamps()
  } // options
  stages {
    stage('\u2776 Test') {
      steps {
        script {
          currentBuild.displayName = "#${env.BUILD_NUMBER} (${env.GIT_COMMIT.take(8)}) ${env.GIT_BRANCH}"
          sh '''
            python3.8 -m pip install -r requirements.txt
            python3.8 -m pytest tests/ -n 7
          '''
        } // script
      } // steps
    } // stage
  } // stages
  post {
    always {
      cleanWs()
    } // always
  } // post
} // pipeline

// vim: ft=groovy
// EOF
