pipeline {
  agent any
  stages {
    stage('Print') {
      steps {
        echo 'Hello There'
      }
    }
    stage('') {
      steps {
        parallel(
          "Print Even More": {
            echo 'Even More'
            
          },
          "Printing third time": {
            echo 'Hello'
            echo 'World'
            
          }
        )
      }
    }
  }
}