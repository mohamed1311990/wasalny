pipeline {
  agent any
  stages {
     stage("checkout") {
                 steps {
        git 'https://github.com/mohamed1311990/wasalny.git'
         }
     }
      stage("Build docker image") {
        steps { echo  'build the image' }
      }
  }
}
