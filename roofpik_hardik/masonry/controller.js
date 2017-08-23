  var app = angular.module('myApp', []);
  app.controller('myCtrl', function($scope, $timeout) {

      var elem = document.querySelector('.grid');
      var msnry = new Masonry(elem, {
          // options
          itemSelector: '.grid-item',
          percentPosition: true,
          gutter: 10
      });


      console.log('l');
      $scope.data = {};
      $scope.arrData = [];
      $scope.flag = 0;

      $scope.st = '-KnOYLXRTPyFYnziowpG';


      db.ref('posts').orderByKey().limitToFirst(15).once('value', function(snapshot) {
          $timeout(function() {
              $scope.data = snapshot.val();
              console.log($scope.data);
              for (var i in $scope.data) {
                  $scope.st = i;
                  // console.log($scope.data[i])
                  $scope.arrData.push($scope.data[i]);

              }
              console.log($scope.st);

          }, 0)

          $timeout(function() {
                  $('.grid').masonry({
                      itemSelector: '.grid-item',
                      
                  });

                  //$('.grid-item').masonry().masonry('destroy');


              }, 0)
              // $('.grid-item').masonry().masonry('destroy');
      });

      var getDataset = function() {
          db.ref('posts').orderByKey().startAt($scope.st).limitToFirst(15).once('value', function(snapshot) {
              $timeout(function() {
                  $scope.data = snapshot.val();
                  console.log($scope.data);
                  for (var i in $scope.data) {
                      $scope.st = i;
                      $scope.arrData.push($scope.data[i]);

                  }
                  console.log($scope.st);
              }, 0)

              $timeout(function() {
                      // $('.grid').masonry({
                      //     itemSelector: '.grid-item',
                      //     percentPosition: true
                      // });
                      // $('.grid-item').masonry().masonry('destroy');


                      $('.grid').masonry().masonry('reloadItems');

                  }, 500)
                  // $('.grid').masonry().masonry('destroy');

          });

      }






      window.addEventListener('scroll', function() {


          if (window.scrollY === document.body.scrollHeight - window.innerHeight) {
              if ($scope.flag != $scope.st) {
                  $scope.flag = $scope.st;
                  getDataset();


              }
          }
      });


  });
